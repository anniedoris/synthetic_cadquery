import cadquery as cq

# Define dimensions
horizontal_leg_length = 60.0
vertical_leg_length = 20.0
thickness = 3.0

# Define hole parameters
vertical_hole_diameter = 3.0
horizontal_hole_diameter = 5.0
large_horizontal_hole_diameter = 7.0

# Create the base L-shaped bracket
result = (
    cq.Workplane("XY")
    .box(horizontal_leg_length, vertical_leg_length, thickness)
)

# Add holes to the vertical leg (4 holes)
vertical_hole_spacing = vertical_leg_length / 5  # 4 holes evenly spaced
for i in range(4):
    y_pos = vertical_hole_spacing * (i + 1)
    result = (
        result.faces(">Z")
        .workplane(offset=-thickness/2)
        .center(0, y_pos)
        .hole(vertical_hole_diameter)
    )

# Add holes to the horizontal leg (5 holes)
horizontal_hole_spacing = horizontal_leg_length / 6  # 5 holes evenly spaced
for i in range(5):
    x_pos = horizontal_hole_spacing * (i + 1)
    # Make the central hole larger
    if i == 2:  # Central hole
        hole_diameter = large_horizontal_hole_diameter
    else:
        hole_diameter = horizontal_hole_diameter
    
    result = (
        result.faces(">Z")
        .workplane(offset=-thickness/2)
        .center(x_pos, 0)
        .hole(hole_diameter)
    )

# Ensure the bracket is properly oriented with the vertical leg on the left
result = result.rotate((0, 0, 0), (0, 0, 1), 90)