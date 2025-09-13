import cadquery as cq

# Define dimensions
diameter = 20.0
height = diameter / 3.0  # One-third of diameter as described

# Create the cylinder
result = cq.Workplane("XY").circle(diameter/2).extrude(height)