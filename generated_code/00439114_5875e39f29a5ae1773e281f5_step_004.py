import cadquery as cq

# Base block dimensions
base_length = 50.0
base_width = 30.0
base_height = 10.0

# Inclined section dimensions
inclined_length = 40.0
inclined_width = 30.0
inclined_height = 20.0

# Rod dimensions
rod_diameter = 6.0
rod_length = 30.0

# Arm dimensions
arm_length = 35.0
arm_width = 8.0
arm_height = 5.0

# Linkage mechanism dimensions
link_length = 15.0
link_width = 6.0
link_height = 4.0

# Create base block
result = cq.Workplane("XY").box(base_length, base_width, base_height)

# Create inclined section
result = (
    result.faces(">Z")
    .workplane(offset=base_height)
    .rect(inclined_length, inclined_width)
    .extrude(inclined_height)
)

# Add circular features to base block
# Center hole
result = (
    result.faces(">Z")
    .workplane()
    .hole(8.0)
)

# Add holes for rods
result = (
    result.faces(">Z")
    .workplane()
    .center(-15, 0)
    .hole(6.0)
    .center(30, 0)
    .hole(6.0)
)

# Add connecting rods
result = (
    result.faces(">Z")
    .workplane()
    .center(-15, 0)
    .circle(rod_diameter/2)
    .extrude(rod_length)
    .faces(">Z")
    .workplane()
    .center(30, 0)
    .circle(rod_diameter/2)
    .extrude(rod_length)
)

# Create articulated arms
# Left arm
result = (
    result.faces(">Z")
    .workplane()
    .center(-15, 0)
    .moveTo(0, -10)
    .lineTo(0, -arm_length)
    .lineTo(arm_width, -arm_length)
    .lineTo(arm_width, -10)
    .close()
    .extrude(arm_height)
    .faces(">Z")
    .workplane()
    .center(arm_width/2, -arm_length + 2)
    .hole(4.0)
)

# Right arm
result = (
    result.faces(">Z")
    .workplane()
    .center(30, 0)
    .moveTo(0, -10)
    .lineTo(0, -arm_length)
    .lineTo(-arm_width, -arm_length)
    .lineTo(-arm_width, -10)
    .close()
    .extrude(arm_height)
    .faces(">Z")
    .workplane()
    .center(-arm_width/2, -arm_length + 2)
    .hole(4.0)
)

# Create linkage mechanism
# First link
result = (
    result.faces("<Z")
    .workplane()
    .center(-15, 10)
    .rect(link_length, link_width)
    .extrude(link_height)
)

# Second link
result = (
    result.faces("<Z")
    .workplane()
    .center(30, 10)
    .rect(link_length, link_width)
    .extrude(link_height)
)

# Add circular joints for linkage
result = (
    result.faces("<Z")
    .workplane()
    .center(-15, 10)
    .hole(5.0)
    .center(30, 10)
    .hole(5.0)
)

# Add circular features to inclined section
result = (
    result.faces(">Z")
    .workplane()
    .center(0, 15)
    .hole(8.0)
    .center(0, -15)
    .hole(8.0)
)

# Add hole for connecting rod to inclined section
result = (
    result.faces("<Z")
    .workplane()
    .center(0, 15)
    .hole(6.0)
)

# Add final details
result = (
    result.faces(">Z")
    .workplane()
    .center(-15, 0)
    .circle(4.0)
    .extrude(2.0)
    .faces(">Z")
    .workplane()
    .center(30, 0)
    .circle(4.0)
    .extrude(2.0)
)

# Add fillets for smoother edges
result = result.edges("|Z").fillet(2.0)