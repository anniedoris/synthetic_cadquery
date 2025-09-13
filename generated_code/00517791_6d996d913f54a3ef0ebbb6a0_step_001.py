import cadquery as cq

# Define cylinder dimensions
diameter = 2.0
height = 2.0
radius = diameter / 2.0

# Create a right circular cylinder with flat top and bottom
result = cq.Workplane("XY").circle(radius).extrude(height)