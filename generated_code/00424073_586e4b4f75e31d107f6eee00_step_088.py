import cadquery as cq

# Dimensions
plate_length = 50.0
plate_width = 30.0
plate_thickness = 5.0
pin_diameter = 3.0
pin_length = 8.0
tab_length = 15.0
tab_width = plate_thickness
tab_height = 8.0
hole_diameter = 2.0

# Create the base plate
result = cq.Workplane("XY").box(plate_length, plate_width, plate_thickness)

# Add pins on the top side
pin_spacing = (plate_length - 2 * pin_diameter) / 5  # 6 pins, so 5 spaces
for i in range(6):
    x_pos = -plate_length/2 + pin_diameter + i * pin_spacing
    result = (
        result.faces(">Z")
        .workplane(offset=plate_thickness/2)
        .center(x_pos, 0)
        .circle(pin_diameter/2)
        .extrude(pin_length)
    )

# Add pins on the bottom side
for i in range(6):
    x_pos = -plate_length/2 + pin_diameter + i * pin_spacing
    result = (
        result.faces("<Z")
        .workplane(offset=-plate_thickness/2)
        .center(x_pos, 0)
        .circle(pin_diameter/2)
        .extrude(pin_length)
    )

# Add the protruding tab on one end
result = (
    result.faces(">X")
    .workplane(offset=plate_thickness/2)
    .center(plate_length/2 - tab_length/2, 0)
    .rect(tab_length, tab_width)
    .extrude(tab_height)
)

# Add the hole near the tab
result = (
    result.faces(">X")
    .workplane(offset=plate_thickness/2)
    .center(plate_length/2 - tab_length/2, 0)
    .hole(hole_diameter)
)

# Round the edges for a smooth finish
result = result.edges("|Z").fillet(1.0)

# Ensure the result is properly defined
result = result.val()