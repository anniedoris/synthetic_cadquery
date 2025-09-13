import cadquery as cq

# Dimensions
plate_length = 100.0
plate_width = 40.0
plate_thickness = 5.0
cutout_length = 80.0
cutout_width = 30.0
block_length = 75.0
block_width = 25.0
block_thickness = plate_thickness
hole_diameter = 3.0
hole_offset = 10.0

# Create the bottom plate
bottom_plate = cq.Workplane("XY").box(plate_length, plate_width, plate_thickness)

# Create the rectangular cutout in the bottom plate
cutout = (
    cq.Workplane("XY")
    .center(0, 0)
    .rect(cutout_length, cutout_width)
    .extrude(plate_thickness + 0.1)  # Slightly longer to ensure full cut
)
bottom_plate = bottom_plate.cut(cutout)

# Add holes to the bottom plate
hole_positions = [
    (-hole_offset, hole_offset),
    (hole_offset, hole_offset),
    (-hole_offset, -hole_offset),
    (hole_offset, -hole_offset)
]
for pos in hole_positions:
    bottom_plate = (
        bottom_plate.faces(">Z")
        .workplane()
        .center(pos[0], pos[1])
        .hole(hole_diameter)
    )

# Create the top plate (offset vertically)
top_plate = cq.Workplane("XY").box(plate_length, plate_width, plate_thickness)
top_plate = top_plate.translate((0, 0, plate_thickness + 1))  # Vertical offset

# Create the rectangular cutout in the top plate
cutout_top = (
    cq.Workplane("XY")
    .center(0, 0)
    .rect(cutout_length, cutout_width)
    .extrude(plate_thickness + 0.1)
)
top_plate = top_plate.cut(cutout_top)

# Add holes to the top plate
for pos in hole_positions:
    top_plate = (
        top_plate.faces(">Z")
        .workplane()
        .center(pos[0], pos[1])
        .hole(hole_diameter)
    )

# Create the insert block
insert_block = cq.Workplane("XY").box(block_length, block_width, block_thickness)
insert_block = insert_block.translate((0, 0, plate_thickness + 1))  # Position at top plate level

# Create the vertical connection between plates (T-shaped structure)
# Create a vertical section connecting the plates
vertical_connection = (
    cq.Workplane("XY")
    .center(0, 0)
    .rect(plate_length, 5.0)  # Width of connection
    .extrude(plate_thickness + 1)  # Height to connect both plates
)
# Position it to connect the plates at one end
vertical_connection = vertical_connection.translate((0, (plate_width - 5.0) / 2, 0))

# Combine all parts
result = bottom_plate.union(top_plate).union(insert_block).union(vertical_connection)