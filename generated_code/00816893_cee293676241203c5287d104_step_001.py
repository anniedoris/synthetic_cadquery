import cadquery as cq

# Define dimensions for the rectangular brick
length = 10.0
width = 6.0
height = 3.0

# Create the rectangular prism
result = cq.Workplane("XY").box(length, width, height)