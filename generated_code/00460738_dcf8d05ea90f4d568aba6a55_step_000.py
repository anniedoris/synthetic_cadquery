import cadquery as cq

# Create a simple rectangular prism (cuboid)
result = cq.Workplane("front").box(4.0, 3.0, 2.0)