import cadquery as cq

# Define dimensions
body_length = 40.0
body_width = 30.0
body_height = 20.0
shaft_diameter = 6.0
shaft_length = 15.0
bearing_diameter = 10.0
mounting_hole_diameter = 3.0
mounting_hole_spacing = 25.0

# Create the main body with tapering bottom
result = (
    cq.Workplane("XY")
    .box(body_length, body_width, body_height)
    .faces("<Z")
    .workplane()
    .rect(body_length * 0.9, body_width * 0.9)
    .extrude(-body_height * 0.1)
)

# Create the shaft protruding from the top center
result = (
    result.faces(">Z")
    .workplane()
    .center(0, 0)
    .circle(shaft_diameter / 2)
    .extrude(shaft_length)
)

# Add the bearing plate
result = (
    result.faces(">Z")
    .workplane()
    .center(0, 0)
    .circle(bearing_diameter / 2)
    .extrude(1.0)
)

# Add mounting holes
result = (
    result.faces(">Z")
    .workplane()
    .rect(mounting_hole_spacing, mounting_hole_spacing, forConstruction=True)
    .vertices()
    .hole(mounting_hole_diameter)
)

# Add fillets for a more polished look
result = result.edges("|Z").fillet(1.0)

# Assign to result variable
result = result