import cadquery as cq

# Define dimensions
body_length = 20.0
body_width = 8.0
body_height = 3.0
pin_length = 5.0
pin_width = 0.4
pin_height = 0.3
pin_spacing = 1.27  # Standard DIP pin spacing
num_pins_per_row = 8
pin_row_offset = 2.0  # Distance between pin rows

# Create the main body
body = cq.Workplane("XY").box(body_length, body_width, body_height)

# Create the curved top surface by filleting the edges
body = body.edges("|Z").fillet(0.5)

# Create pins for both rows
# First pin row (top row)
pin_row_1 = (
    cq.Workplane("XY")
    .moveTo(-body_length/2 + pin_spacing/2, body_width/2 - pin_row_offset)
    .rarray(pin_spacing, 0, num_pins_per_row, 1, center=True)
    .rect(pin_width, pin_height)
    .extrude(-pin_length)
)

# Second pin row (bottom row)
pin_row_2 = (
    cq.Workplane("XY")
    .moveTo(-body_length/2 + pin_spacing/2, -body_width/2 + pin_row_offset)
    .rarray(pin_spacing, 0, num_pins_per_row, 1, center=True)
    .rect(pin_width, pin_height)
    .extrude(-pin_length)
)

# Combine body and pins
result = body.union(pin_row_1).union(pin_row_2)