import cadquery as cq

# Dimensions
length = 100.0
width = 30.0
thickness = 2.0

# Stand dimensions
stand_width = 5.0
stand_depth = 5.0
stand_height = 3.0

# Create the main plate
result = cq.Workplane("XY").box(length, width, thickness)

# Add stands to the short ends (2 on each end)
# First short end (at negative width/2)
result = (
    result.faces("<Y")
    .workplane(offset=-stand_depth/2)
    .rect(length - 2*stand_width, stand_depth, forConstruction=True)
    .vertices()
    .rect(stand_width, stand_depth)
    .extrude(stand_height)
)

# Second short end (at positive width/2)
result = (
    result.faces(">Y")
    .workplane(offset=-stand_depth/2)
    .rect(length - 2*stand_width, stand_depth, forConstruction=True)
    .vertices()
    .rect(stand_width, stand_depth)
    .extrude(stand_height)
)

# Add stands to the long sides (4 on each side)
# First long side (at negative length/2)
result = (
    result.faces("<X")
    .workplane(offset=-stand_depth/2)
    .rect(stand_depth, width - 2*stand_width, forConstruction=True)
    .vertices()
    .rect(stand_depth, stand_width)
    .extrude(stand_height)
)

# Second long side (at positive length/2)
result = (
    result.faces(">X")
    .workplane(offset=-stand_depth/2)
    .rect(stand_depth, width - 2*stand_width, forConstruction=True)
    .vertices()
    .rect(stand_depth, stand_width)
    .extrude(stand_height)
)

# Add triangular markings near stands
# Markings on the top surface
result = (
    result.faces(">Z")
    .workplane()
    .pushPoints([
        (-length/2 + stand_width/2, -width/2 + stand_width/2),  # Bottom left stand
        (-length/2 + stand_width/2, width/2 - stand_width/2),   # Top left stand
        (length/2 - stand_width/2, -width/2 + stand_width/2),   # Bottom right stand
        (length/2 - stand_width/2, width/2 - stand_width/2),    # Top right stand
        (-length/2 + stand_width/2, -width/2 + stand_width/2 + 10),  # Middle left
        (-length/2 + stand_width/2, width/2 - stand_width/2 - 10),   # Middle left
        (length/2 - stand_width/2, -width/2 + stand_width/2 + 10),   # Middle right
        (length/2 - stand_width/2, width/2 - stand_width/2 - 10),    # Middle right
    ])
    .polygon(3, 2.0)  # Triangle with radius 2.0
    .cutThruAll()
)

# Alternative approach for cleaner triangle markings
# Remove previous markings and create more precise ones
result = (
    result.faces(">Z")
    .workplane()
    .pushPoints([
        (-length/2 + stand_width/2, -width/2 + stand_width/2),  # Bottom left stand
        (-length/2 + stand_width/2, width/2 - stand_width/2),   # Top left stand
        (length/2 - stand_width/2, -width/2 + stand_width/2),   # Bottom right stand
        (length/2 - stand_width/2, width/2 - stand_width/2),    # Top right stand
        (-length/2 + stand_width/2 + 10, -width/2 + stand_width/2 + 5),  # Middle left
        (-length/2 + stand_width/2 + 10, width/2 - stand_width/2 - 5),   # Middle left
        (length/2 - stand_width/2 - 10, -width/2 + stand_width/2 + 5),   # Middle right
        (length/2 - stand_width/2 - 10, width/2 - stand_width/2 - 5),    # Middle right
    ])
    .moveTo(0, 0)
    .lineTo(-1.0, 1.732)  # Triangle pointing up
    .lineTo(1.0, 1.732)
    .close()
    .cutThruAll()
)