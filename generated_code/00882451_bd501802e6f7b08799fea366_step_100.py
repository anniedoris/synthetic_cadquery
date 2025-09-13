import cadquery as cq

# Parameters for the hollow cylinder
outer_diameter = 20.0
inner_diameter = 12.0
length = 50.0

# Create the hollow cylinder
result = (
    cq.Workplane("XY")
    .circle(outer_diameter / 2.0)           # Outer circle
    .circle(inner_diameter / 2.0)           # Inner circle (creates the hollow)
    .extrude(length)                        # Extrude to create the cylinder
)

# Alternative approach using shell method (more explicit for hollow objects)
# result = cq.Workplane("XY").circle(outer_diameter / 2.0).extrude(length).faces(">Z").workplane().circle(inner_diameter / 2.0).cutBlind(-length)