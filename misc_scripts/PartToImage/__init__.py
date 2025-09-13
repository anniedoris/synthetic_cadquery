

import os 
import sys
import glob
from pathlib import Path
from tqdm import tqdm
from pathlib import Path
import re
import h5py
import argparse

from OCC.Extend.DataExchange import read_step_file
from OCC.Display.OCCViewer import Viewer3d
from OCC.Core.Prs3d import Prs3d_Drawer, Prs3d_LineAspect
from OCC.Core.Quantity import Quantity_Color, Quantity_TOC_RGB
from OCC.Core.Aspect import Aspect_TOL_SOLID, Aspect_TypeOfLine
from OCC.Core.Quantity import Quantity_Color, Quantity_TOC_RGB
from OCC.Core.Aspect import Aspect_TOL_SOLID, Aspect_TypeOfLine
from OCC.Extend.ShapeFactory import scale_shape, get_boundingbox

import random 

from OCC.Core.Graphic3d import (
    Graphic3d_NOM_BRASS,
    Graphic3d_NOM_BRONZE,
    Graphic3d_NOM_COPPER,
    Graphic3d_NOM_GOLD,
    Graphic3d_NOM_PEWTER,
    Graphic3d_NOM_PLASTER,
    Graphic3d_NOM_PLASTIC,
    Graphic3d_NOM_SILVER,
    Graphic3d_NOM_STEEL,
    Graphic3d_NOM_STONE,
    Graphic3d_NOM_SHINY_PLASTIC,
    Graphic3d_NOM_SATIN,
    Graphic3d_NOM_METALIZED,
    Graphic3d_NOM_NEON_GNC,
    Graphic3d_NOM_CHROME,
    Graphic3d_NOM_ALUMINIUM,
    Graphic3d_NOM_OBSIDIAN,
    Graphic3d_NOM_NEON_PHC,
    Graphic3d_NOM_JADE,
    Graphic3d_NOM_CHARCOAL,
    Graphic3d_NOM_WATER,
    Graphic3d_NOM_GLASS,
    Graphic3d_NOM_DIAMOND,
    Graphic3d_NOM_TRANSPARENT)

from PIL import Image
import re 
import json


from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox
from OCC.Core.gp import gp_Pnt, gp_Vec, gp_Trsf
from OCC.Core.BRepBndLib import brepbndlib_Add
from OCC.Core.Bnd import Bnd_Box
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_Transform
from OCC.Core.BRep import BRep_Tool
from OCC.Core.STEPControl import STEPControl_Reader
from OCC.Core.IFSelect import IFSelect_RetDone
from OCC.Core.BRepGProp import brepgprop_VolumeProperties
from OCC.Core.GProp import GProp_GProps
from OCC.Core.STEPControl import STEPControl_Reader
from OCC.Core.IFSelect import IFSelect_RetDone
from OCC.Core.gp import gp_Vec, gp_Pnt, gp_Trsf
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_Transform
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Fuse, BRepAlgoAPI_Common
from OCC.Core.TopoDS import TopoDS_Shape

import trimesh

from OCC.Extend.DataExchange import read_stl_file

def read_python_file(filepath):
    """
    Reads the contents of a Python (.py) file and returns it as a string.

    Args:
        filepath (str): Path to the .py file.

    Returns:
        str: Contents of the file as a single string.
    """
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    return content


def load_obj_file(filename: str) -> TopoDS_Shape:
    """Load an OBJ file and return a shape."""
    # Load the .obj file
    mesh = trimesh.load(filename)

    # Export to .stl
    mesh.export('output.stl')

    shape = read_stl_file('output.stl')
    if shape is None:
        raise Exception(f"Error: Cannot read OBJ file {filename}.")
    return shape

def load_py_file(filename: str) -> TopoDS_Shape:
    """Load a Python file and return a shape."""

    code = read_python_file(filename)
    code += "\ncq.exporters.export(result, 'output.step')\n"
    
    # Load the .py file
    exec(code)

    return load_step_file('output.step')

def load_step_file(filename : str) -> TopoDS_Shape:
    """Load a STEP file and return the shape."""
    step_reader = STEPControl_Reader()
    status = step_reader.ReadFile(filename)
    if status != IFSelect_RetDone:
        raise Exception("Error: Cannot read STEP file.")
    # Transfer the roots and get the shape
    step_reader.TransferRoots()
    shape = step_reader.OneShape()
    return shape


def remove_bg(image_path):
    # Replace 'path_to_your_image.jpg' with the correct path to your image
    image = Image.open(image_path)

    # Convert image to RGBA (if not already in this mode)
    image = image.convert("RGBA")

    # Make white (and shades of white) pixels transparent
    datas = image.getdata()
    new_data = []
    for item in datas:
        if item[0] > 200 and item[1] > 200 and item[2] > 200:  # Adjust these values if necessary
            new_data.append((255, 255, 255, 0))  # Making white pixels transparent
        else:
            new_data.append(item)

    image.putdata(new_data)
    image.save(image_path, "PNG")


def convert_part_to_image(file_name, view_type, save_path, b_rep_name, resolution_height=224*2, resolution_width=224*2, rotation_angle=None, scale=None, remove_bg=False):
    
    file_type = None

    if ".obj" in file_name:
        shape = load_obj_file(file_name)
        file_type = "obj"
    elif ".step" in file_name:
        shape = load_step_file(file_name)
        file_type = "step"
    elif ".py" in file_name:
        shape = load_py_file(file_name)
        file_type = "py"
    else:
        raise ValueError("Unrecognized file type")

    # Initialize the offscreen renderer
    offscreen_renderer = Viewer3d()
    if view_type == "iso":
        offscreen_renderer.View_Iso()
    elif view_type == "front": 
        offscreen_renderer.View_Front()
    elif view_type == "rear": 
            offscreen_renderer.View_Rear()
    elif view_type == "left": 
            offscreen_renderer.View_Left()
    elif view_type == "right": 
            offscreen_renderer.View_Right()
    elif view_type == "top": 
            offscreen_renderer.View_Top()
    elif view_type == "bottom": 
            offscreen_renderer.View_Bottom()
    else: 
        raise Exception("please choose: top, bottom, front, rear, left, right, iso")


    # scale the shape 
    if scale is not None:
        shape = scale_shape(shape, fx=scale[0], fy=scale[1], fz=scale[2])

    # offscreen renderer
    if file_type == "obj":
        print("Found OBJ")
        offscreen_renderer.Create(draw_face_boundaries=False)
    else:
        offscreen_renderer.Create()
    offscreen_renderer.SetModeShaded()

    # Display the shape
    # Graphic3d_NOM_TRANSPARENT, Graphic3d_NOM_SILVER
    # drawer = Prs3d_Drawer()
    # drawer.SetDisplayEdges(False)
    # offscreen_renderer.Context.SetDefaultDrawer(drawer)
    offscreen_renderer.DisplayShape(shape, update=True, material=Graphic3d_NOM_SILVER, transparency=0.0)
    offscreen_renderer.View.SetBackgroundColor(0, 1, 1, 1)
    
    # Fit the entire shape in the view
    offscreen_renderer.View.FitAll(0.5)

    # Set a high resolution for the renderer
    high_resolution_width = resolution_height
    high_resolution_height = resolution_width
    offscreen_renderer.SetSize(high_resolution_width, high_resolution_height)                

    # Rotate the view
    if rotation_angle is not None: 
        rotation_x = random.randint(-180, 180)  # Random integer between -180 and 180 degrees
        rotation_y = random.randint(-180, 180)
        rotation_z = random.randint(-180, 180)
        offscreen_renderer.View.Rotate(rotation_x, rotation_y, rotation_z)

    # Render and save the image in high resolution
    offscreen_renderer.View.Dump(save_path)
    if remove_bg:
        remove_bg(save_path)
