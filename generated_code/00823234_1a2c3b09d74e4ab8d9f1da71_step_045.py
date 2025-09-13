import cadquery as cq

# Define dimensions
base_length = 100.0
base_width = 60.0
thickness = 10.0

# Create the base plate with an extended corner
result = cq.Workplane("XY").box(base_length, base_width, thickness)

# Add holes - small holes near top
hole_radius = 2.0
result = (
    result.faces(">Z")
    .workplane()
    .moveTo(20, 20)
    .circle(hole_radius)
    .moveTo(-20, 20)
    .circle(hole_radius)
    .moveTo(20, -20)
    .circle(hole_radius)
    .moveTo(-20, -20)
    .circle(hole_radius)
    .cutThruAll()
)

# Add larger central hole
result = (
    result.faces(">Z")
    .workplane()
    .center(0, 0)
    .circle(10.0)
    .cutThruAll()
)

# Add cylindrical protrusions
# Left shaft (longer)
shaft_length = 20.0
shaft_radius = 5.0
result = (
    result.faces(">Z")
    .workplane()
    .moveTo(-40, 0)
    .circle(shaft_radius)
    .extrude(shaft_length)
)

# Right shaft (shorter)
right_shaft_length = 15.0
result = (
    result.faces(">Z")
    .workplane()
    .moveTo(40, -10)
    .circle(shaft_radius)
    .extrude(right_shaft_length)
)

# Bottom center hollow cylinder (bearing/guide)
bearing_radius = 8.0
bearing_hollow_radius = 4.0
bearing_length = 12.0
result = (
    result.faces(">Z")
    .workplane()
    .moveTo(0, -25)
    .circle(bearing_radius)
    .circle(bearing_hollow_radius)
    .extrude(bearing_length)
)

# Create curved section on the right side
# This creates a smooth curve on the right edge
result = (
    result.faces(">Y")
    .workplane(offset=5)
    .moveTo(45, 0)
    .threePointArc((50, 10), (45, 20))
    .lineTo(45, 25)
    .lineTo(30, 25)
    .lineTo(30, 0)
    .close()
    .extrude(5)
)

# Refine the edges to make them smooth
result = result.edges("|Z").fillet(2.0)

# Final result
result = result