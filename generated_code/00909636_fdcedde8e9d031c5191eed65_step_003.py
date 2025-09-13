import cadquery as cq

# Define dimensions for the cylinder
diameter = 20.0
height = 80.0

# Create a cylinder with the specified dimensions
result = cq.Workplane("XY").circle(diameter/2).extrude(height)