import cadquery as cq

# Define dimensions
box_length = 100.0
box_width = 100.0
box_height = 100.0
lid_thickness = 5.0
hinge_width = 3.0
hinge_height = 15.0

# Create the base box
box = cq.Workplane("XY").box(box_length, box_width, box_height)

# Create the lid
lid = cq.Workplane("XY", origin=(0, 0, box_height)).box(box_length, box_width, lid_thickness)

# Create the hinge
# Position the hinge at the midpoint of one side of the lid and box
hinge = cq.Workplane("XY", origin=(box_length/2 - hinge_width/2, -box_width/2, box_height)).box(hinge_width, hinge_height, lid_thickness)

# Combine the box and lid
result = box.union(lid).union(hinge)

# Add a slight gap to allow the lid to open
# This is a simplified representation - in a real model you might want to use
# constraints or assemblies to properly model the hinge mechanism