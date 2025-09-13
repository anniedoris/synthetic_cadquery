import cadquery as cq

# Dimensions
cabinet_width = 60.0
cabinet_depth = 40.0
cabinet_height = 80.0
countertop_thickness = 3.0
countertop_overhang = cabinet_width / 3.0
door_height = cabinet_height
door_width_side = cabinet_width / 3.0
door_width_middle = door_width_side / 2.0
door_recess = 1.0

# Create the cabinet structure
cabinet = cq.Workplane("XY").box(cabinet_width, cabinet_depth, cabinet_height)

# Create the countertop
countertop = (
    cq.Workplane("XY")
    .moveTo(-countertop_overhang, 0)
    .lineTo(cabinet_width, 0)
    .lineTo(cabinet_width, cabinet_depth)
    .lineTo(0, cabinet_depth)
    .lineTo(0, 0)
    .close()
    .extrude(countertop_thickness)
)

# Position countertop on cabinet
countertop = countertop.translate((0, 0, cabinet_height))

# Create side doors
# Left door
left_door = (
    cq.Workplane("XY")
    .box(door_width_side, cabinet_depth, door_height)
    .translate((-door_width_side/2, 0, cabinet_height/2))
)

# Right door
right_door = (
    cq.Workplane("XY")
    .box(door_width_side, cabinet_depth, door_height)
    .translate((door_width_side/2, 0, cabinet_height/2))
)

# Middle door
middle_door = (
    cq.Workplane("XY")
    .box(door_width_middle, cabinet_depth, door_height)
    .translate((0, 0, cabinet_height/2))
)

# Create recessed panel on doors
# Left door panel
left_panel = (
    cq.Workplane("XY")
    .box(door_width_side - 2*door_recess, cabinet_depth - 2*door_recess, door_height - 2*door_recess)
    .translate((-door_width_side/2 + door_recess, 0, cabinet_height/2 - door_recess))
)

# Right door panel
right_panel = (
    cq.Workplane("XY")
    .box(door_width_side - 2*door_recess, cabinet_depth - 2*door_recess, door_height - 2*door_recess)
    .translate((door_width_side/2 - door_recess, 0, cabinet_height/2 - door_recess))
)

# Middle door panel
middle_panel = (
    cq.Workplane("XY")
    .box(door_width_middle - 2*door_recess, cabinet_depth - 2*door_recess, door_height - 2*door_recess)
    .translate((0, 0, cabinet_height/2 - door_recess))
)

# Subtract panels from doors to create recessed effect
left_door = left_door.cut(left_panel)
right_door = right_door.cut(right_panel)
middle_door = middle_door.cut(middle_panel)

# Combine all parts
result = cabinet.union(countertop).union(left_door).union(right_door).union(middle_door)