import cadquery as cq

# Define dimensions
panel_width = 100.0
panel_height = 150.0
panel_thickness = 10.0
column_width = 15.0
hinge_width = 8.0
hinge_height = 12.0
ridge_width = 2.0
ridge_height = 8.0
ridge_spacing = 10.0
angle = 15.0  # degrees

# Create the vertical column
column = cq.Workplane("XY").box(column_width, panel_height, panel_thickness)

# Create the hinge component
hinge = cq.Workplane("XY", origin=(0, 0, 0)).box(hinge_width, hinge_height, panel_thickness)

# Position the hinge on the column
hinge = hinge.translate((column_width/2 - hinge_width/2, panel_height/2 - hinge_height/2, 0))

# Create the main panel
panel = cq.Workplane("XY", origin=(0, 0, 0)).box(panel_width, panel_height, panel_thickness)

# Rotate the panel to create the hinged effect
panel = panel.rotate((0, 0, 0), (0, 0, 1), angle)

# Position the panel to connect with the column
panel = panel.translate((column_width/2, panel_height/2, 0))

# Create vertical ridges on the panel
# First, we need to find the edge where the ridges will be placed
# We'll draw lines from the left edge to the right edge
ridge_count = int((panel_width - 2*ridge_width) / ridge_spacing) + 1

for i in range(ridge_count):
    x_pos = i * ridge_spacing + ridge_width/2
    ridge = cq.Workplane("XY", origin=(x_pos, 0, 0)).box(ridge_width, panel_height, panel_thickness)
    ridge = ridge.translate((0, panel_height/2, 0))
    panel = panel.union(ridge)

# Combine all parts
result = column.union(hinge).union(panel)