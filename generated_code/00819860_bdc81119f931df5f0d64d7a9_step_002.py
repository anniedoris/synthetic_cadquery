import cadquery as cq

# Define dimensions
height = 10.0
width = 5.0
depth = 5.0

# Create the rectangular prism
result = cq.Workplane("XY").box(width, depth, height)