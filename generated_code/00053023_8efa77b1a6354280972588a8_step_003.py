import cadquery as cq

# Define dimensions
length = 10.0
width = 10.0
height = 15.0

# Create the base rectangular prism
result = cq.Workplane("XY").box(length, width, height)

# Remove the top face to create an open box
result = result.faces(">Z").shell(-0.1)