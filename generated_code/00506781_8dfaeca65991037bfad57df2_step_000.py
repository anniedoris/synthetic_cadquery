import cadquery as cq

# Define dimensions
outer_diameter = 50.0
inner_diameter = 20.0
thickness = 5.0

# Create the disk with central hole
result = (
    cq.Workplane("XY")
    .circle(outer_diameter / 2.0)           # Outer circle
    .circle(inner_diameter / 2.0)           # Inner circle (hole)
    .extrude(thickness)                     # Extrude to create thickness
)

# Optional: Add a slight chamfer to the edges for a more realistic appearance
# result = result.edges("|Z").chamfer(0.5)