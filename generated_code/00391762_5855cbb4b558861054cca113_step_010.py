import cadquery as cq

# Define dimensions
hex_width = 10.0      # Width across flats of hexagon
hex_height = 7.0      # Height of hexagon
cylinder_diameter = 6.0  # Diameter of cylindrical shaft
cylinder_length = 20.0   # Length of cylindrical shaft
groove_diameter = 5.5    # Diameter of groove
groove_depth = 0.5       # Depth of groove

# Create the hexagonal head
result = cq.Workplane("XY").polygon(6, hex_width).extrude(hex_height)

# Create the cylindrical shaft
result = (
    result.faces(">Z")
    .workplane()
    .circle(cylinder_diameter / 2)
    .extrude(cylinder_length)
)

# Add the groove near the top of the cylinder
result = (
    result.faces(">Z")
    .workplane(offset=-0.5)
    .circle(groove_diameter / 2)
    .circle(cylinder_diameter / 2)
    .extrude(-groove_depth)
)

result = result.edges("|Z").fillet(0.5)