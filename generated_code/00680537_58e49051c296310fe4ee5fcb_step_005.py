import cadquery as cq

# Create a cylinder with length much greater than diameter
# This creates a "rod-like" cylinder as described
length = 10.0
diameter = 2.0
radius = diameter / 2.0

# Create the cylinder centered at origin
cylinder = cq.Workplane("XY").circle(radius).extrude(length)

# Rotate the cylinder to give it an angled orientation
# Rotate around the X-axis by 30 degrees and Y-axis by 45 degrees
result = cylinder.rotate((0, 0, 0), (1, 0, 0), 30).rotate((0, 0, 0), (0, 1, 0), 45)

# Alternatively, we could use a more precise approach with a transformation:
# Create the cylinder first
# cylinder = cq.Workplane("XY").circle(radius).extrude(length)
# Then apply a transformation to achieve the desired angle
# result = cylinder.rotate((0, 0, 0), (1, 1, 1), 45)