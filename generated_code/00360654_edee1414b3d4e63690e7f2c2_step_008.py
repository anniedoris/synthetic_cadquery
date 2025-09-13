import cadquery as cq

# Define dimensions for the rectangular prism
length = 10.0
width = 6.0
height = 3.0

# Create a rectangular prism (cuboid)
result = cq.Workplane("front").box(length, width, height)