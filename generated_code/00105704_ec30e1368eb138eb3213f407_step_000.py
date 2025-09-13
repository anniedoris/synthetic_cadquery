import cadquery as cq

# Cabinet dimensions
cabinet_width = 100.0
cabinet_depth = 40.0
cabinet_height = 60.0
cabinet_thickness = 5.0

# Drawer dimensions
drawer_width = cabinet_width - 10.0
drawer_depth = cabinet_depth - 10.0
drawer_height = cabinet_height - 10.0

# Handle dimensions
handle_diameter = 4.0
handle_length = 8.0
handle_offset = 20.0

# Cylindrical object dimensions
cylinder_diameter = 30.0
cylinder_height = 20.0

# Create the cabinet base
cabinet = cq.Workplane("XY").box(cabinet_width, cabinet_depth, cabinet_height)

# Create the drawer panel (recessed)
drawer_panel = (
    cq.Workplane("XY")
    .box(drawer_width, drawer_depth, drawer_height)
    .translate((0, 0, cabinet_height - drawer_height))
)

# Subtract the drawer panel from the cabinet
cabinet = cabinet.cut(drawer_panel)

# Create the handle
handle = (
    cq.Workplane("YZ")
    .circle(handle_diameter / 2.0)
    .extrude(handle_length)
    .translate((0, 0, cabinet_height - drawer_height / 2.0))
)

# Position the handle on the drawer panel
handle = handle.translate((0, 0, -drawer_height / 2.0))

# Add the handle to the cabinet
cabinet = cabinet.union(handle)

# Create the cylindrical object on top
cylinder = (
    cq.Workplane("XY")
    .circle(cylinder_diameter / 2.0)
    .extrude(cylinder_height)
    .translate((0, 0, cabinet_height))
)

# Add the cylindrical object to the cabinet
result = cabinet.union(cylinder)