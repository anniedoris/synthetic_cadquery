import cadquery as cq

# Dimensions
length = 100.0
width = 20.0
thickness = 3.0

# L-shaped section dimensions
l_length = 30.0
l_width = 20.0

# Create the base rectangular section
result = cq.Workplane("XY").box(length, width, thickness)

# Add the two rectangular slots near the left end
slot_width = 8.0
slot_height = 4.0
slot_offset = 10.0

result = (
    result.faces(">Z")
    .workplane()
    .moveTo(-length/2 + slot_offset, 0)
    .rect(slot_width, slot_height)
    .cutThruAll()
    .moveTo(slot_width + 2, 0)
    .rect(slot_width, slot_height)
    .cutThruAll()
)

# Add multiple circular holes along the length
hole_diameter = 3.0
hole_spacing = 15.0

for i in range(5):
    result = (
        result.faces(">Z")
        .workplane()
        .moveTo(-length/2 + 40 + i * hole_spacing, 0)
        .circle(hole_diameter/2)
        .cutThruAll()
    )

# Create the L-shaped section
# First, create a workplane on the right face of the main rectangle
result = (
    result.faces(">Y")
    .workplane(offset=thickness)
    .rect(l_length, l_width)
    .extrude(l_width)
)

# Add the large circular hole in the L-shaped section
result = (
    result.faces(">Z")
    .workplane()
    .moveTo(l_length/2 - 5, l_width/2 - 5)
    .circle(6.0)
    .cutThruAll()
)

# Add rectangular cutout below the circular hole
cutout_width = 8.0
cutout_height = 6.0
result = (
    result.faces(">Z")
    .workplane()
    .moveTo(l_length/2 - 5, l_width/2 - 15)
    .rect(cutout_width, cutout_height)
    .cutThruAll()
)

# Add smaller holes along the edges of the L-shaped section
hole_diameter_small = 2.0

# Holes along the vertical part of L-shape
for i in range(3):
    result = (
        result.faces("<Y")
        .workplane(offset=-thickness)
        .moveTo(l_length/2 - 5, l_width/2 - 10 + i * 5)
        .circle(hole_diameter_small/2)
        .cutThruAll()
    )

# Holes along the horizontal part of L-shape
for i in range(2):
    result = (
        result.faces("<X")
        .workplane()
        .moveTo(l_length/2 - 10 + i * 10, l_width/2 - 5)
        .circle(hole_diameter_small/2)
        .cutThruAll()
    )

# Ensure the connection between the two parts is solid by removing any internal faces
# and making sure the geometry is watertight
result = result.faces("<Y").workplane().rect(l_length, l_width).extrude(-thickness)

# Final result
result = result