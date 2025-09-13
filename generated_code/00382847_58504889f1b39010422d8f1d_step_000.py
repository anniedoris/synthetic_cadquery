import cadquery as cq

# Dimensions
horizontal_arm_length = 80.0
horizontal_arm_width = 10.0
horizontal_arm_depth = 15.0
vertical_arm_length = 60.0
vertical_arm_width = 10.0
vertical_arm_depth = 15.0
corner_radius = 8.0
corner_diameter = 16.0

# Create the base L-shaped bracket
result = cq.Workplane("XY")

# Create the horizontal arm with hollow cross-section
result = (
    result
    .rect(horizontal_arm_length, horizontal_arm_width)
    .extrude(horizontal_arm_depth)
    .faces(">Z")
    .workplane()
    .rect(horizontal_arm_length - 2, horizontal_arm_width - 2)
    .cutBlind(-horizontal_arm_depth + 2)
)

# Create the vertical arm with hollow cross-section
result = (
    result
    .faces(">Y")
    .workplane()
    .rect(vertical_arm_length, vertical_arm_width)
    .extrude(vertical_arm_depth)
    .faces(">Z")
    .workplane()
    .rect(vertical_arm_length - 2, vertical_arm_width - 2)
    .cutBlind(-vertical_arm_depth + 2)
)

# Create the corner section (cylindrical)
result = (
    result
    .faces(">X and >Y")
    .workplane()
    .circle(corner_diameter / 2)
    .extrude(corner_diameter)
    .faces(">Z")
    .workplane()
    .circle(corner_diameter / 2 - 2)
    .cutBlind(-corner_diameter + 2)
)

# Add holes in the corner section
result = (
    result
    .faces(">Z")
    .workplane()
    .center(-corner_diameter/2 + 2, 0)
    .circle(2.0)
    .cutThruAll()
    .center(corner_diameter - 4, 0)
    .circle(2.0)
    .cutThruAll()
)

# Add rectangular cutout on the side of the corner
result = (
    result
    .faces(">X")
    .workplane()
    .center(0, 0)
    .rect(8, 8)
    .cutBlind(-2)
)

# Add holes in the vertical arm (top group)
result = (
    result
    .faces("<Y")
    .workplane(offset=-2)
    .center(0, 20)
    .circle(2.0)
    .cutThruAll()
    .center(0, 20)
    .circle(2.0)
    .cutThruAll()
    .center(0, 20)
    .circle(2.0)
    .cutThruAll()
)

# Add holes in the vertical arm (bottom group)
result = (
    result
    .faces("<Y")
    .workplane(offset=-vertical_arm_depth + 2)
    .center(0, 20)
    .circle(2.0)
    .cutThruAll()
    .center(0, 20)
    .circle(2.0)
    .cutThruAll()
    .center(0, 20)
    .circle(2.0)
    .cutThruAll()
    .center(0, 20)
    .circle(2.0)
    .cutThruAll()
)

# Add curved cutout at bottom of vertical arm
result = (
    result
    .faces("<Y")
    .workplane(offset=-vertical_arm_depth + 2)
    .center(0, -25)
    .circle(8.0)
    .cutBlind(-2)
)

# Add circular hole with concentric hole on far end of horizontal arm
result = (
    result
    .faces("<X")
    .workplane(offset=horizontal_arm_depth - 2)
    .center(horizontal_arm_length/2 - 5, 0)
    .circle(6.0)
    .cutBlind(-2)
    .center(0, 0)
    .circle(2.0)
    .cutThruAll()
)

# Add rounded end to horizontal arm
result = (
    result
    .faces("<X")
    .workplane(offset=horizontal_arm_depth - 2)
    .center(horizontal_arm_length/2 - 5, 0)
    .circle(5.0)
    .cutBlind(-2)
)

# Add final rounded edge
result = (
    result
    .faces("<X")
    .workplane(offset=horizontal_arm_depth - 2)
    .center(horizontal_arm_length/2 - 5, 0)
    .circle(4.0)
    .cutBlind(-2)
)

result = result