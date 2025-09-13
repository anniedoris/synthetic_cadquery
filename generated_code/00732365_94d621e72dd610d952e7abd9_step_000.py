import cadquery as cq

# Define dimensions for the rectangular prism
width = 4.0
height = 3.0
depth = 2.0

# Create the rectangular prism
result = cq.Workplane("XY").box(width, height, depth)