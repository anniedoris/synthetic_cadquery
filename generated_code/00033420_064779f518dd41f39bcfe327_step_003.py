import cadquery as cq

# Define cylinder dimensions
radius = 10.0
height = 50.0

# Create a solid cylinder with flat circular top and bottom
result = cq.Workplane("XY").circle(radius).extrude(height)