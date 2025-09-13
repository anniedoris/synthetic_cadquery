import cadquery as cq

# Define dimensions
bottom_length = 40.0
bottom_width = 30.0
bottom_height = 10.0

top_length = 35.0
top_width = 25.0
top_height = 10.0

# Define interlocking dimensions
groove_depth = 3.0
groove_width = 5.0
tab_height = 3.0

# Create bottom block
bottom = cq.Workplane("XY").box(bottom_length, bottom_width, bottom_height)

# Create groove on top edge of bottom block
groove_start_x = (bottom_length - groove_width) / 2
groove_start_y = (bottom_width - groove_depth) / 2

bottom = (
    bottom.faces(">Z")
    .workplane()
    .moveTo(groove_start_x, groove_start_y)
    .rect(groove_width, groove_depth, centered=True)
    .cutThruAll()
)

# Create top block
top = cq.Workplane("XY").box(top_length, top_width, top_height)

# Create tab on bottom edge of top block
tab_start_x = (top_length - groove_width) / 2
tab_start_y = (top_width - groove_depth) / 2

top = (
    top.faces("<Z")
    .workplane()
    .moveTo(tab_start_x, tab_start_y)
    .rect(groove_width, groove_depth, centered=True)
    .extrude(tab_height)
)

# Position the top block above the bottom block
top = top.translate((0, 0, bottom_height))

# Combine both blocks
result = bottom.union(top)