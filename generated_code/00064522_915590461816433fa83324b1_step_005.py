import cadquery as cq

# Create the irregular, rounded shape using a combination of lines and arcs
result = (
    cq.Workplane("front")
    .lineTo(2.0, 0)
    .lineTo(3.0, 1.0)
    .threePointArc((2.5, 2.0), (1.5, 2.0))
    .threePointArc((0.5, 1.5), (0.0, 1.0))
    .lineTo(0, 0)
    .close()
    .extrude(0.5)
)

# Add the circular hole near the bottom edge
result = (
    result.faces(">Z")
    .workplane()
    .moveTo(1.0, 0.5)  # Position the hole near bottom edge
    .circle(0.2)       # Hole diameter of 0.4
    .cutThruAll()
)

# Add fillets to all edges for smooth finish
result = result.edges().fillet(0.1)