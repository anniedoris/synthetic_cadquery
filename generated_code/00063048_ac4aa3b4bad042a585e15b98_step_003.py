import cadquery as cq

# Define dimensions for the rectangular plate
length = 100.0
width = 60.0
thickness = 5.0

# Create a rectangular plate (box) with the specified dimensions
result = cq.Workplane("XY").box(length, width, thickness)