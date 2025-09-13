import cadquery as cq

# Define dimensions
outer_diameter = 20.0
inner_diameter = 12.0
height = 30.0

# Create the hollow cylinder
result = (
    cq.Workplane("XY")
    .circle(outer_diameter / 2.0)           # Outer circle
    .circle(inner_diameter / 2.0)           # Inner circle (hole)
    .extrude(height)                        # Extrude to create the cylinder
)