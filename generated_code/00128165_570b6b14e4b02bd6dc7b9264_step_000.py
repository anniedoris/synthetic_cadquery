import cadquery as cq

# Define dimensions
body_length = 80.0
body_width = 40.0
body_height = 10.0
panel_depth = 30.0
panel_height = 20.0
hinge_diameter = 6.0
hinge_offset = 10.0
hole_diameter = 3.0
groove_depth = 2.0
groove_width = 5.0

# Create the main body
result = cq.Workplane("XY").box(body_length, body_width, body_height)

# Create the side panel
panel = (
    cq.Workplane("XY")
    .box(panel_depth, body_width, panel_height)
    .translate((body_length/2, 0, body_height))
)

# Add hinge cutout to main body
hinge_cutout = (
    cq.Workplane("XY")
    .circle(hinge_diameter/2)
    .extrude(body_height + 2)
    .translate((body_length/2 - hinge_offset, 0, -1))
)
result = result.cut(hinge_cutout)

# Add hinge cutout to side panel
panel_hinge_cutout = (
    cq.Workplane("XY")
    .circle(hinge_diameter/2)
    .extrude(panel_height + 2)
    .translate((panel_depth/2, 0, -1))
)
panel = panel.cut(panel_hinge_cutout)

# Create hinge pin
hinge_pin = (
    cq.Workplane("XY")
    .circle(hinge_diameter/2)
    .extrude(body_height + 2)
    .translate((body_length/2 - hinge_offset, 0, -1))
)

# Add grooves to main body
groove1 = (
    cq.Workplane("XY")
    .rect(groove_width, body_width, forConstruction=True)
    .vertices()
    .rect(groove_width, groove_depth)
    .extrude(-groove_depth)
    .translate((body_length/2 - groove_width/2, 0, -body_height))
)
result = result.union(groove1)

# Add fastening holes to main body
fasten_holes = (
    cq.Workplane("XY")
    .rect(body_length - 10, body_width - 10, forConstruction=True)
    .vertices()
    .circle(hole_diameter/2)
    .extrude(-body_height)
)
result = result.union(fasten_holes)

# Add fastening holes to side panel
panel_fasten_holes = (
    cq.Workplane("XY")
    .rect(panel_depth - 10, body_width - 10, forConstruction=True)
    .vertices()
    .circle(hole_diameter/2)
    .extrude(-panel_height)
    .translate((0, 0, body_height))
)
panel = panel.union(panel_fasten_holes)

# Combine the main body and panel
result = result.union(panel)

# Add the hinge pin (this would be the actual pin that connects the two parts)
result = result.union(hinge_pin)

# Add some additional structural features
# Add reinforcement ribs to the side panel
rib1 = (
    cq.Workplane("XY")
    .rect(2, body_width, forConstruction=True)
    .vertices()
    .rect(2, 2)
    .extrude(-panel_height)
    .translate((panel_depth/2 - 2, 0, body_height))
)
panel = panel.union(rib1)

# Position the panel properly
panel = panel.translate((0, 0, body_height))

# Add the panel to the main result
result = result.union(panel)