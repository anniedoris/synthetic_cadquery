import cadquery as cq

# Create a cylinder with specified dimensions
# Using reasonable dimensions for a rod/col
radius = 1.0
length = 5.0

# Create the cylinder aligned with the Z-axis
result = cq.Workplane("XY").circle(radius).extrude(length)

# Rotate to achieve diagonal orientation
# Rotate 45 degrees around X-axis and 30 degrees around Y-axis
result = result.rotate((0, 0, 0), (1, 0, 0), 45)
result = result.rotate((0, 0, 0), (0, 1, 0), 30)