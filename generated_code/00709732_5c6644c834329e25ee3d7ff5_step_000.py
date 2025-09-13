import cadquery as cq

# Create a simple cube with equal dimensions
result = cq.Workplane("front").box(2.0, 2.0, 2.0)