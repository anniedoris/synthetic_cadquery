import cadquery as cq

# Define dimensions
width = 10.0
depth = 10.0
height = 10.0
chamfer_size = 1.0

# Create the base rectangular block
result = cq.Workplane("XY").box(width, depth, height)

# Add chamfer to the top edges
# Select the top faces and apply chamfer to their edges
result = (
    result.faces(">Z")
    .edges()
    .chamfer(chamfer_size)
)

# Alternative approach: Create chamfered top face explicitly
# result = (
#     cq.Workplane("XY")
#     .box(width, depth, height)
#     .faces(">Z")
#     .workplane()
#     .rect(width - 2*chamfer_size, depth - 2*chamfer_size, forConstruction=True)
#     .vertices()
#     .chamfer(chamfer_size)
# )