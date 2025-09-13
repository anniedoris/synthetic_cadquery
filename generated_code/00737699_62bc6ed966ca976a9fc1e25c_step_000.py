import cadquery as cq

# Create the base curved plate
result = cq.Workplane("XY").box(80, 60, 5)

# Create the thickened flange on upper right
# First create a workplane at the upper right area
result = (
    result.faces(">Y")
    .workplane(offset=2.5)
    .center(30, 20)
    .rect(20, 15, forConstruction=True)
    .vertices()
    .hole(3.0)  # hole in the flange
)

# Create the large central cutout
result = (
    result.faces(">Z")
    .workplane()
    .center(0, -10)
    .circle(15)
    .cutThruAll()
)

# Create smaller holes around the central cutout
# Hole 1 - near the edge of cutout
result = (
    result.faces(">Z")
    .workplane()
    .center(10, -25)
    .circle(2.0)
    .cutThruAll()
)

# Hole 2 - near the edge of cutout
result = (
    result.faces(">Z")
    .workplane()
    .center(-10, -25)
    .circle(2.0)
    .cutThruAll()
)

# Hole 3 - to the left of cutout
result = (
    result.faces(">Z")
    .workplane()
    .center(-25, -10)
    .circle(2.0)
    .cutThruAll()
)

# Hole 4 - to the right of cutout
result = (
    result.faces(">Z")
    .workplane()
    .center(25, -10)
    .circle(2.0)
    .cutThruAll()
)

# Create first protrusion with hole on top
result = (
    result.faces(">Z")
    .workplane()
    .center(-20, -25)
    .circle(5)
    .extrude(3)
    .faces(">Z")
    .workplane()
    .circle(2.0)
    .cutThruAll()
)

# Create second protrusion with hole on top
result = (
    result.faces(">Z")
    .workplane()
    .center(20, -25)
    .circle(5)
    .extrude(3)
    .faces(">Z")
    .workplane()
    .circle(2.0)
    .cutThruAll()
)

# Add some surface texturing/roughness by creating small circles
result = (
    result.faces(">Z")
    .workplane()
    .pushPoints([(-5, -5), (5, -5), (0, 0), (-10, 10), (10, 10)])
    .circle(0.5)
    .cutThruAll()
)