import cadquery as cq

# Panel dimensions
panel_width = 200.0
panel_height = 300.0
panel_thickness = 10.0

# Linear element dimensions
linear_width = 12.0
linear_height = panel_height
linear_offset = 10.0

# L-shaped component dimensions
l_width = 30.0
l_height = 20.0
l_thickness = 8.0
l_flange_length = 15.0

# Protruding section dimensions
protrusion_width = 25.0
protrusion_height = 30.0
cutout_width = 15.0
cutout_height = 10.0

# Create the main panel
result = cq.Workplane("XY").box(panel_width, panel_height, panel_thickness)

# Add beveled edge at bottom corner
bevel_offset = 5.0
result = (
    result.faces("<Y")
    .edges("<X")
    .fillet(bevel_offset)
)

# Add the linear element (guide rail)
linear_x_pos = panel_width / 2 - linear_offset - linear_width / 2
result = (
    result.faces(">X")
    .workplane(offset=linear_x_pos)
    .rect(linear_width, linear_height)
    .extrude(panel_thickness)
)

# Add L-shaped components to the left
# Top L-shaped component
top_l_x = -panel_width / 2 + 15.0
top_l_y = panel_height / 2 - 50.0
result = (
    result.faces("<X")
    .workplane(offset=top_l_x, centerOption="CenterOfBoundBox")
    .center(0, top_l_y)
    .rect(l_width, l_height)
    .extrude(l_thickness)
    .faces(">Z")
    .workplane()
    .moveTo(0, l_height/2)
    .lineTo(l_flange_length, l_height/2)
    .lineTo(l_flange_length, l_height/2 - l_flange_length)
    .lineTo(0, l_height/2 - l_flange_length)
    .close()
    .extrude(l_thickness)
)

# Middle L-shaped component
middle_l_x = -panel_width / 2 + 15.0
middle_l_y = 0.0
result = (
    result.faces("<X")
    .workplane(offset=middle_l_x, centerOption="CenterOfBoundBox")
    .center(0, middle_l_y)
    .rect(l_width, l_height)
    .extrude(l_thickness)
    .faces(">Z")
    .workplane()
    .moveTo(0, l_height/2)
    .lineTo(l_flange_length, l_height/2)
    .lineTo(l_flange_length, l_height/2 - l_flange_length)
    .lineTo(0, l_height/2 - l_flange_length)
    .close()
    .extrude(l_thickness)
)

# Add protruding section on the right edge
protrusion_x = panel_width / 2 - protrusion_width / 2
result = (
    result.faces(">X")
    .workplane(offset=protrusion_x)
    .rect(protrusion_width, protrusion_height)
    .extrude(panel_thickness)
)

# Add rectangular cutout in protruding section
cutout_x = panel_width / 2 - protrusion_width / 2 + (protrusion_width - cutout_width) / 2
cutout_y = panel_height / 2 - protrusion_height / 2 + (protrusion_height - cutout_height) / 2
result = (
    result.faces(">X")
    .workplane(offset=cutout_x)
    .center(0, cutout_y)
    .rect(cutout_width, cutout_height)
    .cutBlind(-panel_thickness)
)

# Add the complex assembly at top right corner
# Create a small assembly with multiple parts
assembly_x = panel_width / 2 - 5.0
assembly_y = panel_height / 2 - 50.0

# Base of the assembly
result = (
    result.faces(">X")
    .workplane(offset=assembly_x)
    .center(0, assembly_y)
    .rect(10, 10)
    .extrude(5)
)

# Add a small rod or screw indicator
result = (
    result.faces(">Z")
    .workplane()
    .center(0, 5)
    .circle(1.5)
    .extrude(8)
)

# Add a small circular part for fastener
result = (
    result.faces(">Z")
    .workplane()
    .center(0, -5)
    .circle(3)
    .extrude(3)
)

# Add red line indicator (represented as a thin line)
result = (
    result.faces(">Z")
    .workplane()
    .center(0, 0)
    .moveTo(-5, 0)
    .lineTo(5, 0)
    .lineTo(5, 0.5)
    .lineTo(-5, 0.5)
    .close()
    .extrude(0.2)
)

# Final result
result = result