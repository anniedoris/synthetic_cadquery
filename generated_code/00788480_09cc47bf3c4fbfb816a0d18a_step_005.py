import cadquery as cq

# Define dimensions
length = 10.0
width = 6.0
height = 4.0

# Create a rectangular prism (cuboid)
result = cq.Workplane("XY").box(length, width, height)