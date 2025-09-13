import cadquery as cq

# Define dimensions
length = 10.0
width = 6.0
thickness = 1.0

# Create a rectangular prism (block) with the specified dimensions
result = cq.Workplane("XY").box(length, width, thickness)