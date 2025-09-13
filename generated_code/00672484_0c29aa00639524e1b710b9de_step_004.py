import cadquery as cq

# Create a rectangular prism (flat bar) that's elongated
# Dimensions: length >> width >> thickness
length = 100.0
width = 20.0
thickness = 5.0

# Create the base rectangle and extrude it
result = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(thickness)
    .rotate((0, 0, 0), (1, 0, 0), 30)  # Rotate to create diagonal orientation
    .rotate((0, 0, 0), (0, 1, 0), 15)  # Additional rotation for 3D effect
)

# Add some visual enhancements to indicate 3D perspective
# Create a slightly smaller rectangle at the back to simulate perspective
result = (
    result.faces(">Z")
    .workplane(offset=thickness * 0.8)
    .rect(length * 0.8, width * 0.8)
    .extrude(thickness * 0.2)
)