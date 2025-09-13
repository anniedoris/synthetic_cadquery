import cadquery as cq

# Define dimensions
outer_diameter = 20.0
inner_diameter = 12.0
height = 5.0

# Create the hollow cylindrical ring
result = (
    cq.Workplane("XY")
    .circle(outer_diameter / 2.0)  # Outer circle
    .circle(inner_diameter / 2.0)   # Inner circle (creates the ring)
    .extrude(height)               # Extrude to create the cylinder
)

# The result is a hollow cylindrical ring with:
# - Outer diameter: 20.0
# - Inner diameter: 12.0
# - Height: 5.0
# The wall thickness is uniform at 4.0 (outer radius 10.0 - inner radius 6.0)