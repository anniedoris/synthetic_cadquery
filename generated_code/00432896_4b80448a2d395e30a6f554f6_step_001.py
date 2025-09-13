import cadquery as cq

# Define dimensions
length = 100.0
width = 30.0
height = 20.0
cavity_diameter = 8.0
cavity_depth = 10.0

# Create the base rectangular block
result = cq.Workplane("XY").box(length, width, height)

# Add three cylindrical cavities on the top surface
# Position them evenly along the length
cavity_spacing = length / 4  # Space them at 1/4, 1/2, and 3/4 along length
cavity_positions = [
    (-length/2 + cavity_spacing, 0),  # First cavity
    (0, 0),                           # Second cavity (center)
    (length/2 - cavity_spacing, 0)    # Third cavity
]

# Create cavities on the top surface
for pos in cavity_positions:
    result = (
        result.faces(">Z")
        .workplane()
        .center(pos[0], pos[1])
        .circle(cavity_diameter/2)
        .cutBlind(-cavity_depth)
    )

# The result should be a rectangular block with three cylindrical cavities
# on its top surface, not through the entire block