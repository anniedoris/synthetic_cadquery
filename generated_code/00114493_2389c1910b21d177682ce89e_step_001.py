import cadquery as cq

# Create the main base plate
result = cq.Workplane("XY").box(100, 80, 5)

# Add protrusions
# First protrusion
result = (
    result.faces(">Z")
    .workplane()
    .center(-30, 20)
    .rect(15, 10)
    .extrude(8)
)

# Second protrusion
result = (
    result.faces(">Z")
    .workplane()
    .center(20, -15)
    .rect(12, 8)
    .extrude(6)
)

# Third protrusion
result = (
    result.faces(">Z")
    .workplane()
    .center(40, 30)
    .rect(10, 15)
    .extrude(7)
)

# Add cutouts
# First cutout
result = (
    result.faces(">Z")
    .workplane()
    .center(-10, 0)
    .rect(20, 15)
    .cutThruAll()
)

# Second cutout
result = (
    result.faces(">Z")
    .workplane()
    .center(30, 10)
    .circle(8)
    .cutThruAll()
)

# Third cutout
result = (
    result.faces(">Z")
    .workplane()
    .center(-25, -25)
    .polygon(6, 12)
    .cutThruAll()
)

# Fourth cutout
result = (
    result.faces(">Z")
    .workplane()
    .center(50, -10)
    .rect(10, 10)
    .cutThruAll()
)

# Add chamfers to edges
result = result.edges("|Z").chamfer(1)

# Add a mounting hole
result = (
    result.faces(">Z")
    .workplane()
    .center(-40, 30)
    .circle(2)
    .cutThruAll()
)

# Add another mounting hole
result = (
    result.faces(">Z")
    .workplane()
    .center(45, -25)
    .circle(1.5)
    .cutThruAll()
)