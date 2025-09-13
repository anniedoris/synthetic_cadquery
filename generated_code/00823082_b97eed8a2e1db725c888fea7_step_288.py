import cadquery as cq

# Define dimensions
length = 10.0
width = 3.0  
thickness = 2.0

# Create the rectangular prism
result = (
    cq.Workplane("XY")
    .box(length, width, thickness)
    .transformed(rotate=cq.Vector(15, 10, 0))  # Rotate to create diagonal orientation
)