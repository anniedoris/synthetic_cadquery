import cadquery as cq

# Create a simple cube with side length of 2.0
# The cube is oriented with one corner facing the viewer to create perspective
result = cq.Workplane("front").box(2.0, 2.0, 2.0)