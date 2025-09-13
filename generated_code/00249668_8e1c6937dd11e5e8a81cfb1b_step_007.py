import cadquery as cq

# Create the main curved profile
# Define the main shape with varying curvature
points = [
    (0, 0),
    (10, 5),
    (20, 10),
    (30, 15),
    (40, 20),
    (50, 25),
    (60, 30),
    (70, 35),
    (80, 40),
    (90, 45),
    (100, 50),
    (110, 45),
    (120, 40),
    (130, 35),
    (140, 30),
    (150, 25),
    (160, 20),
    (170, 15),
    (180, 10),
    (190, 5),
    (200, 0),
]

# Create the main profile
profile = cq.Workplane("XY").polyline(points)

# Create a smooth curve from the polyline
result = profile.close().extrude(10)

# Add the rectangular protrusion
result = (
    result.faces(">Z")
    .workplane()
    .center(100, 20)
    .rect(20, 30)
    .extrude(15)
)

# Add the cutout in the protrusion
result = (
    result.faces(">Z")
    .workplane()
    .center(100, 20)
    .rect(10, 20, forConstruction=True)
    .vertices()
    .hole(3)
)

# Add the hook mechanism
result = (
    result.faces(">Z")
    .workplane()
    .center(0, 0)
    .moveTo(-10, 0)
    .lineTo(-20, 0)
    .threePointArc((-25, 5), (-20, 10))
    .lineTo(-10, 10)
    .close()
    .extrude(10)
)

# Round the edges for a smooth finish
result = result.edges().fillet(2)

# Ensure the object is solid and properly constructed
result = result.clean()

# Since we're making a 3D solid with extrusion and various features,
# the result variable now contains the complete object