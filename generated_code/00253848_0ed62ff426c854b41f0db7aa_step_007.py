import cadquery as cq

# Define dimensions
base_length = 40.0
base_width = 40.0
base_height = 10.0

top_length = 30.0
top_width = 30.0
top_height = 15.0

central_cylinder_diameter = 8.0
central_cylinder_height = 12.0

side_protrusion_length = 8.0
side_protrusion_width = 6.0
side_protrusion_height = 8.0

side_cylinder_diameter = 4.0
side_cylinder_height = 4.0

# Create the base
result = cq.Workplane("XY").box(base_length, base_width, base_height)

# Create the stepped top
result = (
    result.faces(">Z")
    .workplane()
    .rect(top_length, top_width)
    .extrude(top_height - base_height)
)

# Create the central cylinder
result = (
    result.faces(">Z")
    .workplane()
    .center(0, 0)
    .circle(central_cylinder_diameter / 2)
    .extrude(central_cylinder_height)
)

# Create side protrusions
# Position them at the four edges of the top square
side_offset = (top_length - side_protrusion_length) / 2

# Front side
result = (
    result.faces(">Z")
    .workplane()
    .center(0, side_offset)
    .rect(side_protrusion_length, side_protrusion_width)
    .extrude(side_protrusion_height)
    .faces(">Z")
    .workplane()
    .center(0, 0)
    .circle(side_cylinder_diameter / 2)
    .extrude(side_cylinder_height)
)

# Back side
result = (
    result.faces(">Z")
    .workplane()
    .center(0, -side_offset)
    .rect(side_protrusion_length, side_protrusion_width)
    .extrude(side_protrusion_height)
    .faces(">Z")
    .workplane()
    .center(0, 0)
    .circle(side_cylinder_diameter / 2)
    .extrude(side_cylinder_height)
)

# Left side
result = (
    result.faces(">Z")
    .workplane()
    .center(-side_offset, 0)
    .rect(side_protrusion_width, side_protrusion_length)
    .extrude(side_protrusion_height)
    .faces(">Z")
    .workplane()
    .center(0, 0)
    .circle(side_cylinder_diameter / 2)
    .extrude(side_cylinder_height)
)

# Right side
result = (
    result.faces(">Z")
    .workplane()
    .center(side_offset, 0)
    .rect(side_protrusion_width, side_protrusion_length)
    .extrude(side_protrusion_height)
    .faces(">Z")
    .workplane()
    .center(0, 0)
    .circle(side_cylinder_diameter / 2)
    .extrude(side_cylinder_height)
)