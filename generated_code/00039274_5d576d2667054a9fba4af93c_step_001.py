import cadquery as cq

# Define dimensions
diameter = 20.0
thickness = 5.0

# Create a cylindrical disk/puck
result = cq.Workplane("XY").circle(diameter/2).extrude(thickness)