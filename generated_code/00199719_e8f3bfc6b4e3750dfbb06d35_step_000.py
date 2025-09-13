import cadquery as cq

# Define dimensions
radius = 2.0
thickness = 0.5

# Create a flat circular disk/cylinder
result = cq.Workplane("XY").circle(radius).extrude(thickness)