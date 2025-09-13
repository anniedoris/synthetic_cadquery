import cadquery as cq

# Define dimensions
base_length = 50.0
base_width = 30.0
height = 20.0
top_length = 30.0
top_width = 20.0
circle_diameter = 8.0
groove_depth = 8.0
groove_width = 6.0

# Create the base rectangle
result = cq.Workplane("XY").rect(base_length, base_width).extrude(height)

# Create the sloped top surface by cutting a trapezoidal prism
# First, create a workplane at the top
top_plane = result.faces(">Z").workplane()

# Create a trapezoidal profile for the top surface
# The top surface is a rectangle that's smaller than the base
top_profile = (
    cq.Workplane("XY")
    .rect(top_length, top_width)
    .extrude(height)
    .faces(">Z")
    .workplane()
    .rect(top_length, top_width)
    .extrude(height)
)

# Create a trapezoidal cut to form the sloped top
trapezoid = (
    cq.Workplane("XY")
    .rect(base_length, base_width)
    .workplane(offset=height)
    .rect(top_length, top_width)
    .loft(combine=True)
)

# Cut the trapezoidal shape from the base
result = result.cut(trapezoid)

# Add the circular cutout on the top surface
result = (
    result.faces(">Z")
    .workplane()
    .circle(circle_diameter / 2.0)
    .cutThruAll()
)

# Create V-shaped groove on one side
# First, create a workplane on the side where the groove will be
side_face = result.faces("<X").workplane()

# Create the V-shaped profile
groove_profile = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(-groove_width/2, groove_depth)
    .lineTo(groove_width/2, groove_depth)
    .close()
)

# Extrude the groove
groove = groove_profile.extrude(-base_width/2)

# Cut the groove
result = result.cut(groove)

# Ensure the object is solid and properly formed
result = result.clean()

# Make sure the final shape is correct by checking the edges
result = result.edges("|Z").edges("<X").fillet(0.1)