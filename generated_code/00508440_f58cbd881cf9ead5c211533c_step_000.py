import cadquery as cq

# Define cylinder parameters
diameter = 2.0
radius = diameter / 2.0
length = 10.0

# Create a cylinder aligned with the Z-axis
cylinder = cq.Workplane("XY").circle(radius).extrude(length)

# Rotate and translate to create the diagonal orientation
# Rotate around X-axis to tilt the cylinder diagonally
# Then translate to position it from upper left to lower right
result = (
    cylinder
    .rotate((0, 0, 0), (1, 0, 0), 30)  # Tilt the cylinder
    .translate((0, 0, length/2))  # Position it properly
)

# Alternative approach using a more precise diagonal orientation
# Create the cylinder aligned along a diagonal vector
result = (
    cq.Workplane("XY")
    .center(0, 0)
    .circle(radius)
    .extrude(length)
    .rotate((0, 0, 0), (1, 1, 0), 45)  # Rotate around Y axis to get diagonal
    .translate((-length/2, -length/2, 0))  # Position appropriately
)

# Simpler approach - create a cylinder aligned with Z, then rotate it
result = (
    cq.Workplane("XY")
    .circle(radius)
    .extrude(length)
    .rotate((0, 0, 0), (0, 1, 0), 45)  # Rotate 45 degrees around Y
    .rotate((0, 0, 0), (1, 0, 0), 30)  # Additional rotation for diagonal effect
    .translate((0, 0, length/2))
)