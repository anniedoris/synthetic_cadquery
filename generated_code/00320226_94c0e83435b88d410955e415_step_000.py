import cadquery as cq

# Define dimensions
length = 100.0
width = 50.0
height = 20.0

# Create the base rectangular prism
result = cq.Workplane("XY").box(length, width, height)

# Create the elevated section on the right side
elevated_width = 30.0
elevated_height = 5.0
elevated_offset = 10.0

result = (
    result.faces(">Z")
    .workplane(offset=height)
    .rect(elevated_width, width - elevated_offset, forConstruction=True)
    .vertices()
    .rect(elevated_width, elevated_height)
    .extrude(elevated_height)
)

# Create the three rounded rectangular cutouts on the left side
cutout_width = 8.0
cutout_height = 12.0
cutout_spacing = 15.0
cutout_offset = 15.0

result = (
    result.faces(">Z")
    .workplane()
    .pushPoints([
        (-length/2 + cutout_offset, -width/2 + cutout_spacing),
        (-length/2 + cutout_offset, 0),
        (-length/2 + cutout_offset, width/2 - cutout_spacing)
    ])
    .rect(cutout_width, cutout_height)
    .cutThruAll()
)

# Create the circular indentation near bottom right corner
result = (
    result.faces(">Z")
    .workplane()
    .moveTo(length/2 - 15, -width/2 + 10)
    .circle(3.0)
    .cutThruAll()
)

# Create the "MARIO" text engraving
# This is a simplified approach - in reality, you'd need to import or define
# the specific font geometry for accurate text rendering
text_depth = 2.0
text_offset_x = -length/2 + 20
text_offset_y = -width/2 + 10

# Create a simple approximation of the text by adding a rectangular cutout
result = (
    result.faces(">Z")
    .workplane()
    .moveTo(text_offset_x, text_offset_y)
    .rect(60, 15)
    .cutBlind(-text_depth)
)

# Add some details to make the text more visible - a simple rectangle
result = (
    result.faces(">Z")
    .workplane()
    .moveTo(text_offset_x + 10, text_offset_y + 3)
    .rect(40, 9)
    .cutBlind(-text_depth * 0.8)
)

# Add a small rectangular feature to indicate the "O" in MARIO
result = (
    result.faces(">Z")
    .workplane()
    .moveTo(text_offset_x + 40, text_offset_y + 2)
    .rect(8, 8)
    .cutBlind(-text_depth * 0.8)
)

# Add a circular feature to indicate the "O" in MARIO
result = (
    result.faces(">Z")
    .workplane()
    .moveTo(text_offset_x + 44, text_offset_y + 6)
    .circle(2.5)
    .cutBlind(-text_depth * 0.8)
)

# Add the raised rectangular section
result = (
    result.faces(">Z")
    .workplane(offset=height)
    .rect(elevated_width, elevated_height)
    .extrude(elevated_height)
)