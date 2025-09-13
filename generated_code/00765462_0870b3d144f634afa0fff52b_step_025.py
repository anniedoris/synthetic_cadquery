import cadquery as cq

# Define dimensions
length = 100.0
width = 50.0
thickness = 5.0

# Create the rectangular plate
result = cq.Workplane("XY").box(length, width, thickness)