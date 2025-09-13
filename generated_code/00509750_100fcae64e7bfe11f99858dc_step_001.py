import cadquery as cq

# Define dimensions
length = 100.0
width = 30.0
height = 20.0
hole_diameter = 10.0
hole_offset = 15.0  # Distance from the edge along the width

# Create the rectangular block
result = cq.Workplane("XY").box(length, width, height)

# Add the circular cutout on the top face
result = (
    result.faces(">Z")
    .workplane()
    .center(0, hole_offset)
    .circle(hole_diameter / 2)
    .cutThruAll()
)