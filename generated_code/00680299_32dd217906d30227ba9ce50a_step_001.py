import cadquery as cq

# Define dimensions
diameter = 10.0
length = 50.0

# Create a cylinder with the specified dimensions
# We'll orient it diagonally by rotating it
result = (
    cq.Workplane("XY")
    .circle(diameter / 2.0)
    .extrude(length)
    .rotate((0, 0, 0), (1, 1, 0), 30)  # Rotate to give 3D perspective
)