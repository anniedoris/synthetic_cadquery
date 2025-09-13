import cadquery as cq

# Define dimensions
base_diameter = 20.0
base_height = 10.0
hex_width = 12.0
hex_height = 8.0
cone_diameter_top = 16.0
cone_diameter_bottom = 24.0
cone_height = 12.0
cavity_diameter = 10.0

# Create the base cylindrical section
result = cq.Workplane("XY").circle(base_diameter/2).extrude(base_height)

# Create the hexagonal section
result = (
    result.faces(">Z")
    .workplane()
    .polygon(6, hex_width)
    .extrude(hex_height)
)

# Create the conical section
result = (
    result.faces(">Z")
    .workplane()
    .circle(cone_diameter_bottom/2)
    .workplane(offset=cone_height)
    .circle(cone_diameter_top/2)
    .loft(combine=True)
)

# Create the internal cavity
result = (
    result.faces(">Z")
    .workplane()
    .circle(cavity_diameter/2)
    .extrude(cone_height)
)

# Add fillets to smooth transitions
result = result.edges("|Z").fillet(1.0)

# The final object is assigned to result