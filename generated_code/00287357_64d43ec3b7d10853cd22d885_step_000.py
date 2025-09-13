import cadquery as cq

# Define dimensions
bar_length = 50.0
bar_width = 10.0
bar_thickness = 5.0
plate_height = 20.0
plate_thickness = 5.0
hole_diameter = 3.0
hole_spacing = 15.0

# Create the rectangular bar
result = cq.Workplane("XY").box(bar_length, bar_width, bar_thickness)

# Add holes to the bar
hole_positions = [-hole_spacing, 0.0, hole_spacing]
for pos in hole_positions:
    result = (
        result.faces(">Z")
        .workplane(offset=0.1)
        .center(pos, 0)
        .hole(hole_diameter)
    )

# Create the plate by extending from the end of the bar
# First, create a workplane on the face of the bar
result = (
    result.faces(">Y")
    .workplane(offset=bar_thickness/2)
    .rect(plate_thickness, plate_height)
    .extrude(bar_thickness/2)
)

# Create the L-shaped bend by rotating the plate
# Move to the end of the bar and create the plate
result = (
    result.faces("<Y")
    .workplane(offset=bar_thickness/2)
    .rect(plate_thickness, plate_height)
    .extrude(bar_thickness/2)
)

# Actually, let's restructure this more clearly:
# Start with the bar
result = cq.Workplane("XY").box(bar_length, bar_width, bar_thickness)

# Add holes
for i in range(3):
    hole_x = -hole_spacing + i * hole_spacing
    result = (
        result.faces(">Z")
        .workplane(offset=0.1)
        .center(hole_x, 0)
        .hole(hole_diameter)
    )

# Add the plate at the end of the bar, perpendicular to it
# Create a workplane on the face at the end of the bar
result = (
    result.faces(">X")
    .workplane(offset=bar_thickness/2)
    .rect(plate_height, bar_thickness)
    .extrude(bar_thickness/2)
)

# The plate extends in the Y direction, but we want it to extend in the Z direction
# Let's correct this approach
result = cq.Workplane("XY").box(bar_length, bar_width, bar_thickness)

# Add holes
for i in range(3):
    hole_x = -hole_spacing + i * hole_spacing
    result = (
        result.faces(">Z")
        .workplane(offset=0.1)
        .center(hole_x, 0)
        .hole(hole_diameter)
    )

# Add the plate section at the end of the bar
result = (
    result.faces(">X")
    .workplane(offset=bar_thickness/2)
    .rect(bar_thickness, plate_height)
    .extrude(bar_thickness/2)
)

# Actually, let's properly model the L-shaped structure:
# Start with the bar
result = cq.Workplane("XY").box(bar_length, bar_width, bar_thickness)

# Add holes to the bar
for i in range(3):
    hole_x = -hole_spacing + i * hole_spacing
    result = (
        result.faces(">Z")
        .workplane(offset=0.1)
        .center(hole_x, 0)
        .hole(hole_diameter)
    )

# Create the plate that extends perpendicularly from the bar
# The plate extends in the Y direction from the end of the bar
result = (
    result.faces(">X")
    .workplane(offset=bar_thickness/2)
    .rect(bar_width, plate_height)
    .extrude(bar_thickness/2)
)

# Better approach - create plate perpendicular to the bar
# Create the main bar
result = cq.Workplane("XY").box(bar_length, bar_width, bar_thickness)

# Add holes to the bar
for i in range(3):
    hole_x = -hole_spacing + i * hole_spacing
    result = (
        result.faces(">Z")
        .workplane(offset=0.1)
        .center(hole_x, 0)
        .hole(hole_diameter)
    )

# Create the plate that extends vertically (in Z direction) from the end of the bar
result = (
    result.faces(">X")
    .workplane(offset=bar_thickness/2)
    .rect(bar_width, plate_height)
    .extrude(bar_thickness/2)
)

# That's not right either. Let's carefully create the L-shape:
# Create the bar section
result = cq.Workplane("XY").box(bar_length, bar_width, bar_thickness)

# Add holes to the bar
for i in range(3):
    hole_x = -hole_spacing + i * hole_spacing
    result = (
        result.faces(">Z")
        .workplane(offset=0.1)
        .center(hole_x, 0)
        .hole(hole_diameter)
    )

# Create a plate that extends downward (in -Z direction) from the end of the bar
result = (
    result.faces(">X")
    .workplane(offset=bar_thickness/2)
    .rect(bar_width, plate_height)
    .extrude(-bar_thickness/2)
)

# Let's define the final version:
# Start with the bar
result = cq.Workplane("XY").box(bar_length, bar_width, bar_thickness)

# Add holes to the bar
for i in range(3):
    hole_x = -hole_spacing + i * hole_spacing
    result = (
        result.faces(">Z")
        .workplane(offset=0.1)
        .center(hole_x, 0)
        .hole(hole_diameter)
    )

# Create the plate that extends vertically downward from the bar end
# We need to work on the face of the bar at the end
result = (
    result.faces(">X")
    .workplane(offset=bar_thickness/2)
    .rect(bar_width, plate_height)
    .extrude(-bar_thickness/2)
)

# Actually, the simplest and most correct approach:
# Create the bar
result = cq.Workplane("XY").box(bar_length, bar_width, bar_thickness)

# Add holes to the bar
for i in range(3):
    hole_x = -hole_spacing + i * hole_spacing
    result = (
        result.faces(">Z")
        .workplane(offset=0.1)
        .center(hole_x, 0)
        .hole(hole_diameter)
    )

# Create the vertical plate by extending from the end of the bar
# The plate extends from the end of the bar (X=bar_length/2) in the -Z direction
result = (
    result.faces(">X")
    .workplane(offset=bar_thickness/2)
    .rect(bar_width, plate_height)
    .extrude(-bar_thickness/2)
)