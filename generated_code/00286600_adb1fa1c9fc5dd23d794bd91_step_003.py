import cadquery as cq

# Define dimensions
diameter = 10.0
height = 50.0

# Create a cylindrical shape with flat ends
result = cq.Workplane("XY").circle(diameter/2).extrude(height)