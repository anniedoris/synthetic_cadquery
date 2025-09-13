import cadquery as cq

# Create a simple cube with side length 2.0
result = cq.Workplane("front").box(2.0, 2.0, 2.0)