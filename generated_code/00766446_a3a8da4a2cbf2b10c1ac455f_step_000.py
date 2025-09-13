import cadquery as cq

# Dimensions
body_length = 60.0
body_width = 30.0
body_height = 10.0
key_length = 20.0
key_width = 8.0
key_height = 12.0
key_offset = 5.0
hole_diameter = 2.0
text_height = 3.0
text_width = 40.0
rounding_radius = 2.0

# Create main body with inclined top surface
result = cq.Workplane("XY").box(body_length, body_width, body_height)

# Create the inclined top surface by cutting a wedge
result = (
    result.faces(">Z")
    .workplane()
    .rect(body_length, body_width, forConstruction=True)
    .vertices()
    .moveTo(0, body_width/2 - 10)
    .lineTo(body_length/2, body_width/2)
    .lineTo(body_length/2, body_width/2 - 10)
    .close()
    .extrude(-2)
)

# Round all edges
result = result.edges("|Z").fillet(rounding_radius)

# Create key protrusion
key = (
    cq.Workplane("XY")
    .rect(key_length, key_width)
    .extrude(key_height)
    .faces("<Z")
    .workplane(offset=-key_height)
    .moveTo(key_length/2, 0)
    .circle(hole_diameter/2)
    .cutThruAll()
)

# Position key protrusion
result = result.union(
    key.translate((body_length/2 + key_length/2 + key_offset, 0, body_height/2 - key_height/2))
)

# Add engraved text
result = (
    result.faces(">Z")
    .workplane()
    .moveTo(-text_width/2, 0)
    .text("Stephen Posner", 3.0, 0.5, cut=True)
)

result = result.translate((-body_length/2, -body_width/2, -body_height/2))

# Make the final object
result = result