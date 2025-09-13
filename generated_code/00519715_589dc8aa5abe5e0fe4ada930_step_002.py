import cadquery as cq

# Define dimensions
plate_length = 100.0
plate_width = 60.0
plate_thickness = 5.0

# Cut-out dimensions
cutout_length = 40.0
cutout_width = 20.0
cutout_offset = 10.0

# Arm dimensions
arm_length = 30.0
arm_width = 20.0
arm_thickness = plate_thickness

# Hole dimensions
hole_diameter = 4.0
large_hole_diameter = 12.0

# Create the main plate with cut-out
result = cq.Workplane("XY").box(plate_length, plate_width, plate_thickness)

# Create the cut-out section
cutout_x = (plate_length - cutout_length) / 2
cutout_y = (plate_width - cutout_width) / 2
result = (
    result.faces(">Z")
    .workplane()
    .rect(cutout_length, cutout_width)
    .cutBlind(-plate_thickness)
)

# Create the L-shaped arm
# Move to the bottom right corner and create the arm
arm_x = plate_length / 2 - arm_length / 2
arm_y = -plate_width / 2 + arm_width / 2

# Create the vertical part of the arm
result = (
    result.faces(">Z")
    .workplane()
    .move(plate_length / 2 - arm_length / 2, -plate_width / 2 + arm_width / 2)
    .rect(arm_length, arm_width)
    .extrude(arm_thickness)
)

# Create the horizontal part of the arm
result = (
    result.faces(">Z")
    .workplane()
    .move(plate_length / 2 - arm_length / 2 + arm_length / 2, -plate_width / 2 + arm_width / 2)
    .rect(arm_length, arm_width)
    .extrude(arm_thickness)
)

# Add holes to the main plate
# Four corner holes
corner_hole_positions = [
    (-plate_length/2 + 10, plate_width/2 - 10),
    (plate_length/2 - 10, plate_width/2 - 10),
    (-plate_length/2 + 10, -plate_width/2 + 10),
    (plate_length/2 - 10, -plate_width/2 + 10)
]

for pos in corner_hole_positions:
    result = (
        result.faces(">Z")
        .workplane()
        .move(pos[0], pos[1])
        .hole(hole_diameter)
    )

# Two large center holes
result = (
    result.faces(">Z")
    .workplane()
    .move(0, 0)
    .hole(large_hole_diameter)
)

# Add holes to the arm
# Two holes near the base of the arm
result = (
    result.faces(">Z")
    .workplane()
    .move(plate_length/2 - arm_length/2, -plate_width/2 + arm_width/2)
    .hole(hole_diameter)
)

result = (
    result.faces(">Z")
    .workplane()
    .move(plate_length/2 - arm_length/2 + arm_length, -plate_width/2 + arm_width/2)
    .hole(hole_diameter)
)

# Add holes to the end plate of the arm
end_plate_x = plate_length/2 - arm_length/2 + arm_length/2
end_plate_y = -plate_width/2 + arm_width/2
result = (
    result.faces(">Z")
    .workplane()
    .move(end_plate_x, end_plate_y)
    .rect(arm_length, arm_width)
    .vertices()
    .hole(hole_diameter)
)

# Add the small protrusion/bump on the end of the arm
result = (
    result.faces(">Z")
    .workplane()
    .move(end_plate_x + arm_length/2, end_plate_y)
    .rect(5, 5)
    .extrude(2)
)

result = result.translate((0, 0, 0))  # Final translation to center the object