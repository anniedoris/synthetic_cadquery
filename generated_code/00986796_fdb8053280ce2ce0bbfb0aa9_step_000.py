import cadquery as cq

# Define dimensions
width = 10.0
depth = 10.0
height = 50.0

# Create the rectangular prism (column)
result = cq.Workplane("front").box(width, depth, height)