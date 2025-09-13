import cadquery as cq

# Define dimensions
length = 10.0
width = 6.0
thickness = 2.0

# Create the rectangular prism (flat plate)
result = cq.Workplane("XY").box(length, width, thickness)