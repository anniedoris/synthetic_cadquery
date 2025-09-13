import cadquery as cq

# Define dimensions
cube_side = 20.0
cylinder_diameter = 8.0
cylinder_radius = cylinder_diameter / 2.0
cylinder_height = 5.0

# Create the cube
result = cq.Workplane("XY").box(cube_side, cube_side, cube_side)

# Add the protruding cylinder on the front face, slightly offset from center
result = (
    result.faces(">Z")
    .workplane()
    .center(-cube_side/4, 0)
    .circle(cylinder_radius)
    .extrude(cylinder_height)
)

# Add the indented cylinder on the top face, centered
result = (
    result.faces(">Z")
    .workplane()
    .center(0, 0)
    .circle(cylinder_radius)
    .cutBlind(cylinder_height)
)