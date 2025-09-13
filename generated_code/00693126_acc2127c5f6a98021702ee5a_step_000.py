import cadquery as cq

# Define dimensions
outer_diameter = 20.0
inner_diameter = 12.0
thickness = 4.0

# Create the ring profile (outer circle with inner hole)
ring_profile = (
    cq.Workplane("XY")
    .circle(outer_diameter / 2.0)
    .circle(inner_diameter / 2.0)
    .extrude(thickness)
)

# Rotate the ring to create the tilted appearance
# Rotate around the X-axis by 30 degrees to give the tilted effect
result = ring_profile.rotate((0, 0, 0), (1, 0, 0), 30)

# Alternative approach using a more complex rotation for better tilt effect:
# result = (
#     cq.Workplane("XY")
#     .circle(outer_diameter / 2.0)
#     .circle(inner_diameter / 2.0)
#     .extrude(thickness)
#     .rotate((0, 0, 0), (1, 1, 0), 45)
# )