import cadquery as cq

# Define cylinder dimensions
radius = 2.0
height = 3.0

# Create a solid cylinder
result = cq.Workplane("XY").circle(radius).extrude(height)