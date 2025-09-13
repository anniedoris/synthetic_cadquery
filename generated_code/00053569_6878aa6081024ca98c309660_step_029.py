import cadquery as cq

# Define dimensions
top_panel_length = 80.0
top_panel_width = 10.0
top_panel_height = 5.0

vertical_panel_height = 20.0
vertical_panel_width = 8.0

lower_panel_length = 60.0
lower_panel_width = 10.0
lower_panel_angle = 15.0  # degrees

connector_radius = 3.0

# Create the top panel
result = cq.Workplane("XY").box(top_panel_length, top_panel_width, top_panel_height)

# Add the small protrusion at the left end
protrusion_length = 5.0
protrusion_width = 3.0
protrusion_height = 2.0
result = (
    result.faces(">X")
    .workplane(offset=-protrusion_length)
    .rect(protrusion_width, protrusion_height)
    .extrude(protrusion_length)
)

# Add the vertical support panel
result = (
    result.faces(">Y")
    .workplane(offset=vertical_panel_height/2)
    .rect(vertical_panel_width, vertical_panel_height)
    .extrude(vertical_panel_height)
)

# Add the lower horizontal panel
result = (
    result.faces(">Z")
    .workplane(offset=-lower_panel_length/2)
    .rect(lower_panel_length, lower_panel_width)
    .extrude(lower_panel_length)
)

# Create the central connector
result = (
    result.faces(">Z")
    .workplane(offset=-lower_panel_length/2)
    .circle(connector_radius)
    .extrude(2 * connector_radius)
)

# Add side panels
side_panel_length = 15.0
side_panel_width = 5.0
side_panel_height = 10.0

# Left side panel
result = (
    result.faces("<Z")
    .workplane(offset=-side_panel_length/2)
    .rect(side_panel_width, side_panel_length)
    .extrude(side_panel_length)
)

# Right side panel
result = (
    result.faces(">Z")
    .workplane(offset=-side_panel_length/2)
    .rect(side_panel_width, side_panel_length)
    .extrude(side_panel_length)
)

# Apply fillets to improve aesthetics and remove sharp edges
result = result.edges("|Z").fillet(1.0)

# Make sure the object is properly oriented
result = result.rotate((0, 0, 0), (1, 0, 0), 90)

# The result object now contains the complete mechanical component
# with all specified panels, protrusions, and connectors