import cadquery as cq

# Define dimensions
length = 50.0
width = 30.0
thickness = 5.0

# Create the base rectangular prism
result = cq.Workplane("XY").box(length, width, thickness)

# Add top surface cutout with keyway
# Center cutout on top face
result = (
    result.faces(">Z")
    .workplane()
    .center(0, 0)
    .circle(6.0)
    .moveTo(0, -6.0)
    .lineTo(0, 6.0)
    .cutThruAll()
)

# Add left side cutout with keyway
# Center cutout on left face
result = (
    result.faces("<X")
    .workplane()
    .center(0, 0)
    .circle(6.0)
    .moveTo(0, -6.0)
    .lineTo(0, 6.0)
    .cutThruAll()
)

# Add right side cutout with keyway
# Center cutout on right face
result = (
    result.faces(">X")
    .workplane()
    .center(0, 0)
    .circle(6.0)
    .moveTo(0, -6.0)
    .lineTo(0, 6.0)
    .cutThruAll()
)

# Add a slight tilt to the object to give isometric appearance
# Rotate around the Y-axis to tilt the object
result = result.rotate((0, 0, 0), (0, 1, 0), 15)