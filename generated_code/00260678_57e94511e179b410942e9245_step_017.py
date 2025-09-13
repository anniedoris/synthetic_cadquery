import cadquery as cq

# Define the dimensions of the rectangular prism
length = 10.0
width = 6.0
height = 4.0

# Create a rectangular prism with the specified dimensions
result = cq.Workplane("XY").box(length, width, height)