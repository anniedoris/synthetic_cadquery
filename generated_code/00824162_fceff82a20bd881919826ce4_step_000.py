import cadquery as cq

# Dimensions
length = 50.0
width = 50.0
height = 10.0
recess_diameter = 30.0
groove_diameter = 25.0
groove_width = 2.0
cutout_diameter = 4.0
side_hole_diameter = 3.0

# Create the base rectangular prism
result = cq.Workplane("XY").box(length, width, height)

# Create the central recessed circular area
result = (
    result.faces(">Z")
    .workplane()
    .circle(recess_diameter / 2.0)
    .cutBlind(-2.0)
)

# Add concentric grooves
groove_radii = [
    (groove_diameter / 2.0) - (groove_width * 0.5),
    (groove_diameter / 2.0) - (groove_width * 1.5),
    (groove_diameter / 2.0) - (groove_width * 2.5)
]

for radius in groove_radii:
    result = (
        result.faces(">Z")
        .workplane()
        .circle(radius)
        .cutBlind(-0.5)
    )

# Add central cutouts
result = (
    result.faces(">Z")
    .workplane()
    .center(-2.0, 0)
    .circle(cutout_diameter / 2.0)
    .cutBlind(-2.0)
    .center(4.0, 0)
    .circle(cutout_diameter / 2.0)
    .cutBlind(-2.0)
)

# Add side features (mounting holes)
# Front face
result = (
    result.faces(">Y")
    .workplane()
    .center(-length/2 + 5.0, -width/2 + 5.0)
    .circle(side_hole_diameter / 2.0)
    .cutBlind(-height)
)

# Rear face
result = (
    result.faces("<Y")
    .workplane()
    .center(-length/2 + 5.0, width/2 - 5.0)
    .circle(side_hole_diameter / 2.0)
    .cutBlind(-height)
)

# Left face
result = (
    result.faces("<X")
    .workplane()
    .center(length/2 - 5.0, -width/2 + 5.0)
    .circle(side_hole_diameter / 2.0)
    .cutBlind(-height)
)

# Right face
result = (
    result.faces(">X")
    .workplane()
    .center(-length/2 + 5.0, width/2 - 5.0)
    .circle(side_hole_diameter / 2.0)
    .cutBlind(-height)
)

# Final result
result = result