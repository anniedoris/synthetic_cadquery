import cadquery as cq

# Define dimensions for each tier
R1 = 20.0  # Bottom cone large radius
r1 = 15.0  # Bottom cone small radius
H1 = 10.0  # Bottom cone height

r2 = 10.0  # Middle cone small radius
H2 = 8.0   # Middle cone height

r3 = 5.0   # Top cone small radius
H3 = 6.0   # Top cone height

r4 = 1.0   # Top opening radius

# Create the bottom tier (truncated cone)
bottom_cone = cq.Workplane("XY").circle(R1).circle(r1).extrude(H1)

# Create the middle tier (truncated cone) on top of bottom
middle_cone = (
    cq.Workplane("XY", origin=(0, 0, H1))
    .circle(r1)
    .circle(r2)
    .extrude(H2)
)

# Create the top tier (truncated cone) on top of middle
top_cone = (
    cq.Workplane("XY", origin=(0, 0, H1 + H2))
    .circle(r2)
    .circle(r3)
    .extrude(H3)
)

# Create the opening in the top cone
opening = (
    cq.Workplane("XY", origin=(0, 0, H1 + H2 + H3))
    .circle(r4)
    .extrude(0.1)  # Small extrusion to create the opening
)

# Combine all parts
result = bottom_cone.union(middle_cone).union(top_cone).union(opening)