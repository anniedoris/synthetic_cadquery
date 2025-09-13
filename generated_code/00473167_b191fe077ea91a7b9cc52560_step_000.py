import cadquery as cq

# Dimensions
cabinet_width = 200.0
cabinet_depth = 100.0
cabinet_height = 300.0
drawer_width = 180.0
drawer_depth = 90.0
drawer_height = 250.0
handle_width = 10.0
handle_height = 5.0
handle_position = 120.0  # From left edge of drawer
chamfer_distance = 5.0

# Create the main cabinet body
result = cq.Workplane("XY").box(cabinet_width, cabinet_depth, cabinet_height)

# Create the drawer
drawer = (
    cq.Workplane("XY")
    .box(drawer_width, drawer_depth, drawer_height)
    .translate((0, 0, cabinet_height - drawer_height))
)

# Subtract the drawer from the cabinet to create the drawer opening
result = result.cut(drawer)

# Create the drawer handle
handle = (
    cq.Workplane("XY")
    .rect(handle_width, handle_height)
    .extrude(2.0)
    .translate((0, drawer_depth/2 - 1.0, cabinet_height - drawer_height/2))
)

# Add the handle to the drawer
result = result.union(handle)

# Add chamfers to the top edges
result = (
    result.edges("|Z")
    .edges(">X or <X or >Y or <Y")
    .chamfer(chamfer_distance)
)

# Ensure the drawer is properly positioned
drawer = drawer.translate((0, 0, cabinet_height - drawer_height))
result = result.union(drawer)