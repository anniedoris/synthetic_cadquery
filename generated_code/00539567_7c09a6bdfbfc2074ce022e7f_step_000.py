import cadquery as cq

# Define dimensions
horizontal_length = 50.0
horizontal_width = 10.0
horizontal_thickness = 5.0

vertical_height = 30.0
vertical_width = 10.0
vertical_thickness = 5.0

cutout_length = 20.0
cutout_width = 8.0

# Create the base plate (horizontal section)
result = cq.Workplane("XY").box(horizontal_length, horizontal_width, horizontal_thickness)

# Create the vertical section
result = (
    result.faces(">Z")
    .workplane()
    .moveTo(horizontal_length/2 - vertical_width/2, 0)
    .box(vertical_width, vertical_height, vertical_thickness)
)

# Create the cutout in the horizontal section
result = (
    result.faces("<Z")
    .workplane()
    .moveTo(0, 0)
    .rect(cutout_length, cutout_width)
    .cutThruAll()
)

# The cutout is centered in the horizontal section, so we need to adjust the position
# Let's recreate with proper positioning
result = cq.Workplane("XY").box(horizontal_length, horizontal_width, horizontal_thickness)

# Add the vertical section
result = (
    result.faces(">Z")
    .workplane()
    .moveTo(horizontal_length/2 - vertical_width/2, horizontal_width/2 - vertical_height/2)
    .box(vertical_width, vertical_height, vertical_thickness)
)

# Create the cutout in the horizontal section (centered)
result = (
    result.faces("<Z")
    .workplane()
    .moveTo(0, 0)
    .rect(cutout_length, cutout_width)
    .cutThruAll()
)