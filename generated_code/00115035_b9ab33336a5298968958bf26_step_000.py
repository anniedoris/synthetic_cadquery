import cadquery as cq

# Create the abstract organic shape based on the description
result = (
    cq.Workplane("front")
    # Start with the top left sharp point and diagonal line
    .moveTo(-2.0, 2.0)
    .lineTo(-1.0, 0.5)
    # First smooth curve creating an indentation
    .threePointArc((-0.5, 0.2), (0.0, 0.5))
    # Second indentation
    .threePointArc((0.5, 0.8), (1.0, 0.5))
    # Curve to the right side
    .threePointArc((1.5, 0.2), (2.0, -0.5))
    # Continue to bottom right with rounded corner
    .threePointArc((2.2, -1.0), (1.8, -1.5))
    # Connect back to the left side
    .lineTo(-1.0, -1.0)
    .lineTo(-2.0, -0.5)
    .close()
    .extrude(0.5)
)