import cadquery as cq

# Define dimensions
base_width = 50.0
base_depth = 30.0
base_thickness = 5.0
vertical_height = 50.0
vertical_width = 30.0
curved_radius = 15.0
hole_diameter = 4.0
counterbore_diameter = 8.0
counterbore_depth = 3.0
side_hole_diameter = 2.0

# Create the base plate with rounded edges
result = cq.Workplane("XY").rect(base_width, base_depth).extrude(base_thickness)

# Add countersunk holes to each corner
# Top face
result = (
    result.faces(">Z")
    .workplane()
    .rect(base_width - 10, base_depth - 10, forConstruction=True)
    .vertices()
    .cboreHole(hole_diameter, counterbore_diameter, counterbore_depth)
)

# Create vertical section
# Select the front face and create a vertical section
result = (
    result.faces(">Y")
    .workplane(offset=base_thickness)
    .rect(vertical_width, vertical_height)
    .extrude(vertical_height)
)

# Create the curved protruding feature at the top of vertical section
# Select the top face of vertical section
result = (
    result.faces(">Z")
    .workplane(offset=vertical_height)
    .circle(curved_radius)
    .extrude(curved_radius)
)

# Create the small hole on the side of the vertical section
# Select the side face near the top
result = (
    result.faces("<Y")
    .workplane(offset=vertical_height - 10)
    .circle(side_hole_diameter / 2)
    .cutThruAll()
)

# Add fillets to the edges for a more polished look
result = result.edges("|Z").fillet(2.0)