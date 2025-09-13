import cadquery as cq

# Define dimensions for the cylinder
radius = 2.0
height = 4.0

# Create a solid cylinder
result = cq.Workplane("XY").circle(radius).extrude(height)