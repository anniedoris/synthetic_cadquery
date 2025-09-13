import cadquery as cq

# Define dimensions
plate_length = 100.0
plate_width = 40.0
plate_thickness = 5.0

# Define cut-out dimensions
cutout_width = plate_width / 3.0
cutout_height = 15.0
cutout_spacing = 10.0

# Create the base plate
result = cq.Workplane("XY").box(plate_length, plate_width, plate_thickness)

# Create cut-outs in two rows
# First row
result = (
    result.faces(">Z")
    .workplane()
    .rect(plate_length, plate_width, forConstruction=True)
    .vertices()
    .rect(cutout_width, cutout_height)
    .cutBlind(-plate_thickness)
)

# Second row (offset by half the cutout width)
result = (
    result.faces(">Z")
    .workplane()
    .rect(plate_length, plate_width, forConstruction=True)
    .vertices()
    .rect(cutout_width, cutout_height)
    .cutBlind(-plate_thickness)
)

# Alternative approach: more precise cut-out placement
result = cq.Workplane("XY").box(plate_length, plate_width, plate_thickness)

# Create the cut-outs in two rows
# Row 1: three cut-outs evenly spaced
row1_y_positions = [-plate_width/2 + cutout_width/2 + cutout_spacing,
                    0,
                    plate_width/2 - cutout_width/2 - cutout_spacing]

for y_pos in row1_y_positions:
    result = (
        result.faces(">Z")
        .workplane(offset=0, centerOption="CenterOfBoundBox")
        .center(0, y_pos)
        .rect(cutout_width, cutout_height)
        .cutBlind(-plate_thickness)
    )

# Row 2: same positions but offset in Y direction to create second row
for y_pos in row1_y_positions:
    result = (
        result.faces(">Z")
        .workplane(offset=0, centerOption="CenterOfBoundBox")
        .center(0, y_pos + plate_width/3)
        .rect(cutout_width, cutout_height)
        .cutBlind(-plate_thickness)
    )

# Simplified approach - just create the pattern properly
result = cq.Workplane("XY").box(plate_length, plate_width, plate_thickness)

# Create two rows of three cutouts each
cutout_positions = [
    (-plate_length/3, -plate_width/3),
    (0, -plate_width/3),
    (plate_length/3, -plate_width/3),
    (-plate_length/3, plate_width/3),
    (0, plate_width/3),
    (plate_length/3, plate_width/3)
]

for x, y in cutout_positions:
    result = (
        result.faces(">Z")
        .workplane()
        .center(x, y)
        .rect(cutout_width, cutout_height)
        .cutBlind(-plate_thickness)
    )