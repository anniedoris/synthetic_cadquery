import cadquery as cq

# Define dimensions
outer_diameter = 20.0
inner_diameter = 8.0
thickness = 2.0

# Create the washer
result = (
    cq.Workplane("XY")
    .circle(outer_diameter / 2.0)  # Outer circle
    .circle(inner_diameter / 2.0)   # Inner circle (hole)
    .extrude(thickness)             # Extrude to create the 3D washer
)