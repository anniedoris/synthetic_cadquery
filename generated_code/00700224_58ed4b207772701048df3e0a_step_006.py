import cadquery as cq

# Define dimensions
diameter = 2.0
length = 10.0
radius = diameter / 2.0

# Create the cylinder
result = (
    cq.Workplane("XY")
    .circle(radius)
    .extrude(length)
    .rotate((0, 0, 0), (1, 1, 0), 45)  # Rotate 45 degrees around the X+Y axis for diagonal orientation
)