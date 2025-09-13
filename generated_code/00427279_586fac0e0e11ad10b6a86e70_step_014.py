import cadquery as cq

# Define dimensions
width = 100.0
height = 60.0
thickness = 5.0

# Create a rectangular plate and tilt it by rotating around the X-axis
result = (
    cq.Workplane("XY")
    .box(width, height, thickness)
    .rotate((0, 0, 0), (1, 0, 0), 30)  # Tilt the plate by 30 degrees around X-axis
)

# Alternative approach using transformed for more precise control
# result = (
#     cq.Workplane("XY")
#     .box(width, height, thickness)
#     .transformed(rotate=cq.Vector(30, 0, 0))
# )