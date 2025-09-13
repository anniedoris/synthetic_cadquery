import cadquery as cq

# Define dimensions
vertical_bar_width = 10.0
vertical_bar_height = 100.0
vertical_bar_thickness = 5.0

top_crossbar_width = 8.0
top_crossbar_height = 30.0
top_crossbar_thickness = 5.0

middle_crossbar_width = 6.0
middle_crossbar_height = 20.0
middle_crossbar_thickness = 5.0

base_plate_width = 50.0
base_plate_height = 30.0
base_plate_thickness = 5.0

antenna_height = 15.0
antenna_width = 1.0

clamp_width = 8.0
clamp_height = 10.0
clamp_thickness = 3.0

# Create the vertical bar
result = cq.Workplane("XY").box(vertical_bar_width, vertical_bar_height, vertical_bar_thickness)

# Add the antenna-like feature at the top
antenna_offset = vertical_bar_height / 2 - antenna_height / 2
result = (
    result.faces(">Y")
    .workplane(offset=antenna_offset)
    .rect(antenna_width, antenna_height)
    .extrude(antenna_height)
)

# Add top crossbars
top_crossbar_offset = vertical_bar_height / 2 - top_crossbar_height / 2
result = (
    result.faces(">Y")
    .workplane(offset=top_crossbar_offset)
    .rect(top_crossbar_width, top_crossbar_height)
    .extrude(top_crossbar_thickness)
)

# Add middle crossbars
middle_crossbar_offset = vertical_bar_height / 2 - middle_crossbar_height / 2 - 20
result = (
    result.faces(">Y")
    .workplane(offset=middle_crossbar_offset)
    .rect(middle_crossbar_width, middle_crossbar_height)
    .extrude(middle_crossbar_thickness)
)

# Add base plate
base_plate_offset = -base_plate_height / 2
result = (
    result.faces("<Y")
    .workplane(offset=base_plate_offset)
    .rect(base_plate_width, base_plate_height)
    .extrude(base_plate_thickness)
)

# Add holes to the base plate
base_hole_positions = [
    (-base_plate_width/3, base_plate_height/3),
    (base_plate_width/3, base_plate_height/3),
    (-base_plate_width/3, -base_plate_height/3),
    (base_plate_width/3, -base_plate_height/3),
    (0, -base_plate_height/4)
]

result = result.faces("<Y").workplane(offset=base_plate_offset).pushPoints(base_hole_positions).hole(3.0)

# Add side flange
flange_width = 8.0
flange_height = 10.0
flange_offset = base_plate_width/2 - flange_width/2
result = (
    result.faces("<Y")
    .workplane(offset=base_plate_offset)
    .moveTo(flange_offset, -base_plate_height/2 + flange_height/2)
    .rect(flange_width, flange_height)
    .extrude(base_plate_thickness)
)

# Add circular feature to the flange
result = (
    result.faces("<Y")
    .workplane(offset=base_plate_offset)
    .moveTo(flange_offset + flange_width/2, -base_plate_height/2 + flange_height/2)
    .circle(2.0)
    .extrude(base_plate_thickness)
)

# Add clamp mechanism near middle
clamp_offset = vertical_bar_height / 2 - clamp_height / 2 - 20
result = (
    result.faces(">Y")
    .workplane(offset=clamp_offset)
    .rect(clamp_width, clamp_height)
    .extrude(clamp_thickness)
)

# Add hole to clamp
result = (
    result.faces(">Y")
    .workplane(offset=clamp_offset)
    .moveTo(0, 0)
    .circle(2.0)
    .extrude(clamp_thickness)
)

# Add connecting pin for clamp
pin_diameter = 2.0
pin_length = 5.0
result = (
    result.faces(">Y")
    .workplane(offset=clamp_offset)
    .moveTo(0, -clamp_height/2 + pin_length/2)
    .circle(pin_diameter/2)
    .extrude(pin_length)
)

result = result