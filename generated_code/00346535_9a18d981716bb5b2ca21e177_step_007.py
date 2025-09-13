import cadquery as cq

# Table dimensions
table_length = 100.0
table_width = 60.0
table_height = 30.0
leg_radius = 5.0

# Create the table top
top = cq.Workplane("XY").box(table_length, table_width, 5.0)

# Create the legs
# Position legs at each corner
leg_offset_x = (table_length - 2 * leg_radius) / 2
leg_offset_y = (table_width - 2 * leg_radius) / 2

# Create legs using cylinders
legs = (
    top.faces(">Z")
    .workplane()
    .center(-leg_offset_x, -leg_offset_y)
    .circle(leg_radius)
    .extrude(table_height)
    .faces(">Z")
    .workplane()
    .center(2 * leg_offset_x, 0)
    .circle(leg_radius)
    .extrude(table_height)
    .faces(">Z")
    .workplane()
    .center(0, 2 * leg_offset_y)
    .circle(leg_radius)
    .extrude(table_height)
    .faces(">Z")
    .workplane()
    .center(-2 * leg_offset_x, 0)
    .circle(leg_radius)
    .extrude(table_height)
)

# Combine top and legs
result = top.union(legs)