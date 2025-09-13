import cadquery as cq

# Define dimensions
base_length = 50.0
base_width = 30.0
base_height = 10.0

vertical_length = 20.0
vertical_width = 30.0
vertical_height = 25.0

protrusion_length = 15.0
protrusion_width = 8.0
protrusion_height = 5.0

cutout_diameter_large = 8.0
cutout_diameter_small = 5.0

# Create the base section
result = cq.Workplane("XY").box(base_length, base_width, base_height)

# Add the two protrusions on the top surface
# Front protrusion
result = (
    result.faces(">Z")
    .workplane()
    .moveTo(-(base_length - protrusion_length) / 2, (base_width - protrusion_width) / 2)
    .rect(protrusion_length, protrusion_width)
    .extrude(protrusion_height)
)

# Back protrusion
result = (
    result.faces(">Z")
    .workplane()
    .moveTo((base_length - protrusion_length) / 2, (base_width - protrusion_width) / 2)
    .rect(protrusion_length, protrusion_width)
    .extrude(protrusion_height)
)

# Create the vertical section
# Move to the top of the base and create vertical section
result = (
    result.faces(">Z")
    .workplane()
    .moveTo(0, -base_width / 2 + vertical_width / 2)
    .rect(vertical_length, vertical_width)
    .extrude(vertical_height)
)

# Add the curved cutouts to the front face of the vertical section
# Get the front face of the vertical section
front_face = result.faces(">Y").workplane()

# Add the larger curved cutout
result = (
    front_face
    .moveTo(0, -vertical_height / 4)
    .circle(cutout_diameter_large / 2)
    .cutThruAll()
)

# Add the smaller curved cutout
result = (
    front_face
    .moveTo(0, vertical_height / 4)
    .circle(cutout_diameter_small / 2)
    .cutThruAll()
)