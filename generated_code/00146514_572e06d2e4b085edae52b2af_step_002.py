import cadquery as cq

# Define dimensions
length = 100.0
diameter = 10.0
chamfer_length = 2.0

# Create the cylindrical shaft
result = (
    cq.Workplane("XY")
    .circle(diameter / 2.0)
    .extrude(length)
    .faces(">Z")
    .chamfer(chamfer_length)
)

# Alternative approach with fillet instead of chamfer
# result = (
#     cq.Workplane("XY")
#     .circle(diameter / 2.0)
#     .extrude(length)
#     .faces(">Z")
#     .fillet(diameter / 4.0)
# )