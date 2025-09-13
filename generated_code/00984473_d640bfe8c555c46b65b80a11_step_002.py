import cadquery as cq

# Define dimensions
length = 4.0
width = 3.0
height = 2.0

# Create the rectangular prism
result = cq.Workplane("XY").box(length, width, height)