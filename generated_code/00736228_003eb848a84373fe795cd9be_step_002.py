import cadquery as cq

# Define dimensions
base_length = 50.0
base_width = 30.0
base_thickness = 5.0
left_upright_height = 20.0
right_upright_height = 15.0
upright_width = 8.0
upright_thickness = 5.0
sphere_radius = 4.0

# Create the base plate
result = cq.Workplane("XY").box(base_length, base_width, base_thickness)

# Create the left upright section
result = (
    result.faces(">Z")
    .workplane(offset=base_thickness)
    .rect(upright_width, left_upright_height, forConstruction=True)
    .vertices()
    .rect(upright_width, upright_thickness)
    .extrude(left_upright_height - upright_thickness)
)

# Create the right upright section
result = (
    result.faces(">Z")
    .workplane(offset=base_thickness)
    .rect(upright_width, right_upright_height, forConstruction=True)
    .vertices("<X")
    .rect(upright_width, upright_thickness)
    .extrude(right_upright_height - upright_thickness)
)

# Create the spherical protrusion on the left side
result = (
    result.faces("<X")
    .workplane(offset=-base_thickness)
    .center(-base_length/2 + upright_width/2, 0)
    .sphere(sphere_radius)
)

# Ensure the sphere is properly attached to the base
result = result.faces("<X").workplane(offset=-base_thickness).circle(sphere_radius).extrude(-sphere_radius*2)