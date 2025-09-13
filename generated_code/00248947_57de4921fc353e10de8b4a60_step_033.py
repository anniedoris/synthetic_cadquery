import cadquery as cq

# Define cylinder dimensions
radius = 5.0
height = 50.0

# Create a cylindrical rod/shaft
result = cq.Workplane("XY").circle(radius).extrude(height)