import cadquery as cq

# Base dimensions
base_length = 50.0
base_width = 30.0
base_thickness = 5.0

# Cylinder dimensions
cylinder_diameter = 15.0
cylinder_length = 20.0
cylinder_offset = 10.0  # Offset from center

# Hole dimensions
hole_diameter = 4.0
hole_offset = 8.0  # Distance from edge

# Groove dimensions
groove_depth = 1.0
groove_width = 2.0
groove_count = 6

# Create base
result = cq.Workplane("XY").box(base_length, base_width, base_thickness)

# Add mounting holes
result = (
    result.faces(">Z")
    .workplane()
    .pushPoints([
        (-base_length/2 + hole_offset, -base_width/2 + hole_offset),
        (base_length/2 - hole_offset, -base_width/2 + hole_offset)
    ])
    .hole(hole_diameter)
)

# Create cylindrical section
# Move to top of base and offset
result = (
    result.faces(">Z")
    .workplane(offset=base_thickness)
    .center(cylinder_offset, 0)
    .circle(cylinder_diameter/2)
    .extrude(cylinder_length)
)

# Add grooves to cylinder
groove_spacing = cylinder_length / (groove_count + 1)
for i in range(groove_count):
    groove_y = -cylinder_length/2 + (i+1) * groove_spacing
    result = (
        result.faces(">Z")
        .workplane(offset=groove_y)
        .center(cylinder_offset, 0)
        .rect(cylinder_diameter - groove_width, groove_depth, forConstruction=True)
        .vertices()
        .hole(groove_depth)
    )

# Add fillet at transition
result = result.edges("|Z").fillet(2.0)

# Ensure we have a solid result
result = result.val()

# The result is already a solid, so we can return it directly