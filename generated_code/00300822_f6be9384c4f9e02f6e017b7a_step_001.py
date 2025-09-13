import cadquery as cq

# Create a square cross-section (2x2) and extrude it along a diagonal path
# We'll create a 10x2x2 rectangular prism first, then rotate it
result = (
    cq.Workplane("XY")
    .box(10, 2, 2)  # length=10, width=2, height=2
    .rotate((0, 0, 0), (1, 1, 0), 45)  # Rotate around the diagonal to achieve the diagonal orientation
)