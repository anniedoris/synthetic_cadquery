import cadquery as cq

# Define dimensions
length = 100.0
width = 60.0
thickness = 5.0

# Create the rectangular prism (flat plate)
result = cq.Workplane("front").box(length, width, thickness)