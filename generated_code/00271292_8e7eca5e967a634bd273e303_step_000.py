import cadquery as cq

# Dimensions
base_length = 100.0
base_width = 60.0
base_thickness = 10.0
cavity_length = 40.0
cavity_width = 20.0
cylinder_diameter = 12.0
cylinder_height = 10.0
hole_diameter = 4.0

# Create the base plate with rounded corners
result = cq.Workplane("XY").box(base_length, base_width, base_thickness)

# Create the central rectangular cavity (open on one side)
cavity_offset = (base_length - cavity_length) / 2
result = (
    result.faces(">Z")
    .workplane()
    .rect(cavity_length, cavity_width, forConstruction=True)
    .vertices()
    .hole(cavity_width)  # This creates a through hole for the cavity
)

# Remove material to create the cavity
result = (
    result.faces(">Z")
    .workplane()
    .move(-cavity_offset, 0)
    .rect(cavity_length, cavity_width)
    .cutBlind(-base_thickness)
)

# Add the two cylindrical features
cylinder_radius = cylinder_diameter / 2
cylinder_offset = (base_length - cavity_length) / 2 - cylinder_radius

# Left cylinder
result = (
    result.faces(">Z")
    .workplane()
    .move(-cylinder_offset, 0)
    .circle(cylinder_radius)
    .extrude(cylinder_height)
)

# Right cylinder
result = (
    result.faces(">Z")
    .workplane()
    .move(cylinder_offset, 0)
    .circle(cylinder_radius)
    .extrude(cylinder_height)
)

# Add the small circular hole on one side
hole_offset = (base_length - cavity_length) / 2 - 10.0
result = (
    result.faces(">Z")
    .workplane()
    .move(-hole_offset, 0)
    .circle(hole_diameter / 2)
    .cutBlind(-base_thickness)
)

# Round the corners of the base plate
result = result.edges("|Z").fillet(5.0)

# Ensure the central cavity is properly formed
result = (
    result.faces(">Z")
    .workplane()
    .move(-cavity_offset, 0)
    .rect(cavity_length, cavity_width)
    .cutBlind(-base_thickness)
)