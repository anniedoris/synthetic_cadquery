import cadquery as cq

# Define dimensions for the rectangular prism
length = 10.0
width = 5.0
height = 3.0

# Create a solid rectangular prism (box)
result = cq.Workplane("XY").box(length, width, height)