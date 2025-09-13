import cadquery as cq

# Create the main body with curved surfaces
result = (
    cq.Workplane("XY")
    # Create a base profile with curved edges
    .moveTo(0, 0)
    .lineTo(50, 0)
    .threePointArc((60, 10), (50, 20))
    .lineTo(30, 30)
    .threePointArc((20, 40), (10, 30))
    .lineTo(0, 20)
    .close()
    # Extrude to create the main body
    .extrude(5)
)

# Add the protruding rectangular feature
result = (
    result.faces(">Y")
    .workplane()
    .moveTo(25, 15)
    .rect(8, 4)
    .extrude(3)
)

# Add the hole in the protruding feature
result = (
    result.faces(">Z")
    .workplane()
    .moveTo(29, 17)
    .circle(1.5)
    .cutThruAll()
)

# Add some additional curved details to make it more complex
result = (
    result.faces(">X")
    .workplane()
    .moveTo(45, 5)
    .threePointArc((50, 10), (45, 15))
    .lineTo(40, 15)
    .close()
    .extrude(1)
)

# Add fillets to some edges for a more realistic appearance
result = result.edges("|Z").fillet(0.5)

# Add a small chamfer to some edges
result = result.edges("#Z").chamfer(0.3)

# Add a small circular indentation on the main body
result = (
    result.faces("<Y")
    .workplane()
    .moveTo(10, 10)
    .circle(2)
    .cutBlind(-2)
)

# Add a small rectangular cutout on the side
result = (
    result.faces(">X")
    .workplane()
    .moveTo(40, 8)
    .rect(3, 2)
    .cutBlind(-1)
)