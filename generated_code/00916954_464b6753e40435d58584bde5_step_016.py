import cadquery as cq

# Define cylinder parameters
diameter = 10.0
length = 50.0

# Create the cylinder
result = cq.Workplane("XY").circle(diameter/2).extrude(length)

# Rotate to create diagonal orientation
# Using a transformation to rotate the cylinder
result = result.rotate((0, 0, 0), (1, 1, 1), 45)