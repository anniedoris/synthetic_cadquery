import cadquery as cq

# Define dimensions
body_length = 40.0
body_width = 30.0
body_height = 15.0

cylinder_diameter = 12.0
cylinder_length = 20.0
cylinder_hole_diameter = 8.0

protrusion_length = 10.0
protrusion_width = 8.0
protrusion_height = 5.0

# Create the main body
result = cq.Workplane("XY").box(body_length, body_width, body_height)

# Add the cylindrical protrusion on the front face
result = (
    result.faces(">Z")
    .workplane()
    .center(-body_length/2 + cylinder_length/2, 0)
    .circle(cylinder_diameter/2)
    .extrude(cylinder_length)
)

# Add the hole through the back face, aligned with the cylinder
result = (
    result.faces("<Z")
    .workplane()
    .center(-body_length/2 + cylinder_length/2, 0)
    .circle(cylinder_hole_diameter/2)
    .cutThruAll()
)

# Add the smaller rectangular protrusion on top
result = (
    result.faces(">Z")
    .workplane()
    .center(0, body_width/2 - protrusion_width/2)
    .rect(protrusion_length, protrusion_width)
    .extrude(protrusion_height)
)

# Add the L-shaped feature at the end of the protrusion
# The L-shape will be 3mm thick and 4mm high
result = (
    result.faces(">Z")
    .workplane()
    .center(protrusion_length/2 - 1.5, 0)
    .rect(3.0, 4.0)
    .extrude(3.0)
)

# Add a small fillet to make it more realistic
result = result.edges("|Z").fillet(1.0)

# Ensure the object is properly oriented and centered
result = result.translate((-body_length/2, -body_width/2, 0))