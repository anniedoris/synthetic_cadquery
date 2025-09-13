import cadquery as cq

# Define dimensions
length = 80.0
height = 60.0
thickness = 10.0
hole_diameter = 22.0

# Create a box based on the dimensions
result = (
    cq.Workplane("XY")
    .box(length, height, thickness)
    .faces(">Z")
    .workplane()
    .hole(hole_diameter)
)