import cadquery as cq

# Define the dimensions of the rectangular prism
length = 10.0
width = 8.0
height = 4.0

# Create a rectangular prism (box) with the specified dimensions
result = cq.Workplane("front").box(length, width, height)