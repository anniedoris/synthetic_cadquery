import cadquery as cq

# Define dimensions
outer_diameter = 20.0
inner_diameter = 8.0
thickness = 3.0

# Create the cylindrical ring with central hole
result = (
    cq.Workplane("XY")
    .circle(outer_diameter / 2.0)  # Outer circle
    .circle(inner_diameter / 2.0)  # Inner circle (hole)
    .extrude(thickness)
)