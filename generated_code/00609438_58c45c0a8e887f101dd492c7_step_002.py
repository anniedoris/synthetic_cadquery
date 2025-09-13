import cadquery as cq

# Define dimensions
length = 10.0
width = 6.0
height = 2.0

# Create the rectangular prism
result = cq.Workplane("XY").box(length, width, height)