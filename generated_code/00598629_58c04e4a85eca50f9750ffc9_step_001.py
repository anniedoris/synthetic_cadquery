import cadquery as cq

# Define dimensions
top_cylinder_diameter = 10.0
top_cylinder_height = 5.0
hexagon_diameter = 12.0
hexagon_height = 3.0
taper_angle = 15.0  # degrees
taper_length = 8.0
bottom_cylinder_diameter = 8.0
bottom_cylinder_height = 4.0
small_hole_diameter = 1.5
small_hole_spacing = 4.0

# Create the base object
result = cq.Workplane("XY")

# Add top cylindrical feature with flat top
result = result.circle(top_cylinder_diameter / 2).extrude(top_cylinder_height)

# Add hexagonal section below the top cylinder
result = (
    result.faces(">Z")
    .workplane()
    .polygon(6, hexagon_diameter)
    .extrude(hexagon_height)
)

# Add tapered section
result = (
    result.faces(">Z")
    .workplane()
    .polygon(6, hexagon_diameter)
    .workplane(offset=hexagon_height)
    .pushPoints([(0, 0)])
    .polygon(6, hexagon_diameter * (1 - taper_length * 0.01 * (1 - 1 / (1 + 0.01 * taper_angle)) * 2))
    .loft(combine=True)
)

# Add bottom cylindrical feature
result = (
    result.faces(">Z")
    .workplane()
    .circle(bottom_cylinder_diameter / 2)
    .extrude(bottom_cylinder_height)
)

# Add two small holes on the bottom cylinder
result = (
    result.faces(">Z")
    .workplane()
    .center(-small_hole_spacing/2, 0)
    .circle(small_hole_diameter / 2)
    .cutThruAll()
    .center(small_hole_spacing, 0)
    .circle(small_hole_diameter / 2)
    .cutThruAll()
)

# Ensure smooth transitions by filleting
result = result.edges("|Z").fillet(0.5)

# Final object
result = result