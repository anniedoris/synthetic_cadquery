import cadquery as cq

# Define dimensions
panel_width = 40.0
panel_height = 30.0
panel_thickness = 5.0
cylinder_diameter = 12.0
cylinder_inner_diameter = 8.0
cylinder_length = 25.0
corner_radius = 3.0
hole_diameter = 3.0
protrusion_width = 8.0
protrusion_height = 6.0
protrusion_thickness = 5.0

# Create the flat panel with L-shape
result = (
    cq.Workplane("XY")
    .rect(panel_width, panel_height)
    .extrude(panel_thickness)
)

# Create the horizontal cylindrical section
result = (
    result.faces("<Y")
    .workplane(offset=-panel_thickness/2)
    .circle(cylinder_diameter/2)
    .circle(cylinder_inner_diameter/2)
    .extrude(cylinder_length)
)

# Create the vertical cylindrical section
result = (
    result.faces(">Z")
    .workplane(offset=panel_thickness/2)
    .circle(cylinder_diameter/2)
    .circle(cylinder_inner_diameter/2)
    .extrude(cylinder_length)
)

# Add rounded corners
result = result.edges("|Z").fillet(corner_radius)

# Add holes near the ends of cylindrical sections
# Horizontal cylinder holes
result = (
    result.faces("<Y")
    .workplane(offset=-panel_thickness/2)
    .center(cylinder_length/2, 0)
    .circle(hole_diameter/2)
    .cutThruAll()
)

# Vertical cylinder holes
result = (
    result.faces(">Z")
    .workplane(offset=panel_thickness/2)
    .center(0, cylinder_length/2)
    .circle(hole_diameter/2)
    .cutThruAll()
)

# Add protruding element on top of flat panel near vertical cylinder
result = (
    result.faces(">Z")
    .workplane(offset=panel_thickness/2)
    .center(0, cylinder_length/2)
    .rect(protrusion_width, protrusion_height)
    .extrude(protrusion_thickness)
)

result = result.faces(">Z").workplane(offset=panel_thickness/2).center(0, cylinder_length/2).rect(protrusion_width, protrusion_height).extrude(protrusion_thickness)

# Final result
result = result