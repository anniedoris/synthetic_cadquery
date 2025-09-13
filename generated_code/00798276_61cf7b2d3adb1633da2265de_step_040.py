import cadquery as cq

# Define cylinder dimensions
diameter = 20.0
height = 30.0

# Create a simple cylindrical solid
result = cq.Workplane("XY").circle(diameter/2).extrude(height)