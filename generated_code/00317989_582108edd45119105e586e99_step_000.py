import cadquery as cq

# Define dimensions
length = 4.0
width = 2.0
height = 1.5

# Create a rectangular prism (box)
result = cq.Workplane("front").box(length, width, height)