import cadquery as cq

# Define dimensions
outer_diameter = 50.0
inner_diameter = 20.0
hub_height = 5.0
total_height = 8.0
peripheral_hole_diameter = 4.0
central_hole_diameter = 6.0
peripheral_hole_depth = 4.0

# Create the main cylindrical body
result = cq.Workplane("XY").circle(outer_diameter/2).extrude(total_height)

# Create the central hub
result = (
    result.faces(">Z")
    .workplane()
    .circle(inner_diameter/2)
    .extrude(hub_height)
)

# Create the peripheral holes
result = (
    result.faces(">Z")
    .workplane()
    .rarray(outer_diameter/2 - peripheral_hole_diameter, outer_diameter/2 - peripheral_hole_diameter, 4, 1, True)
    .circle(peripheral_hole_diameter/2)
    .cutBlind(-peripheral_hole_depth)
)

# Create the central hole
result = (
    result.faces(">Z")
    .workplane()
    .circle(central_hole_diameter/2)
    .cutBlind(-total_height)
)

# Add fillets to edges for better aesthetics and stress distribution
result = result.edges("|Z").fillet(1.0)