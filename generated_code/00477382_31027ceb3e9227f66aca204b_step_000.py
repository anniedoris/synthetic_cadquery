import cadquery as cq

# Define dimensions
diameter = 10.0
length = 50.0

# Create a cylinder with the specified dimensions
result = cq.Workplane("XY").circle(diameter/2).extrude(length)

# Rotate to create the diagonal orientation
result = result.rotate((0, 0, 0), (1, 0, 0), 30)
result = result.rotate((0, 0, 0), (0, 1, 0), 15)