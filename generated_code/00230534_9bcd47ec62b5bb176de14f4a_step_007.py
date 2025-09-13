import cadquery as cq

# Define the dimensions of the cylinder
diameter = 20.0
height = 50.0

# Create a cylindrical pillar
result = cq.Workplane("XY").circle(diameter/2).extrude(height)