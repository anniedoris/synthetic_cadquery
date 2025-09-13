import cadquery as cq

# Create a simple vertical rod/line
# Define dimensions
length = 10.0
width = 2.0
height = 2.0

# Create the rod
result = cq.Workplane("XY").box(width, height, length)