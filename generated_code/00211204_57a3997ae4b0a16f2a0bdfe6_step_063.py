import cadquery as cq

# Define dimensions
length = 10.0
width = 6.0
thickness = 2.0

# Create a rectangular prism (box)
result = cq.Workplane("front").box(length, width, thickness)