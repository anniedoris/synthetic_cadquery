import cadquery as cq

# Define cylinder dimensions
radius = 2.0
height = 4.0

# Create a cylinder with the specified radius and height
result = cq.Workplane("XY").circle(radius).extrude(height)