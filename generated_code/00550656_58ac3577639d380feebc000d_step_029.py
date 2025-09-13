import cadquery as cq

# Define dimensions
hex_side_to_side = 16.0  # 16mm across opposite sides of hexagon
hex_height = 5.0
cylinder_diameter = 12.0
cylinder_height = 8.0
bore_diameter = 6.0

# Create the hexagonal base
result = cq.Workplane("XY").polygon(6, hex_side_to_side).extrude(hex_height)

# Create the cylindrical top section
result = (
    result.faces(">Z")
    .workplane()
    .circle(cylinder_diameter / 2.0)
    .extrude(cylinder_height)
)

# Create the central bore
result = (
    result.faces(">Z")
    .workplane()
    .circle(bore_diameter / 2.0)
    .cutThruAll()
)

# Optional: Add a fillet to the step between hexagon and cylinder for smoother transition
result = result.edges("|Z").fillet(0.5)