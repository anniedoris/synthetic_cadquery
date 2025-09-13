import cadquery as cq

# Define dimensions
length = 10.0
width = 4.0
thickness = 1.0

# Create the cuboid
result = cq.Workplane("XY").box(length, width, thickness)