import cadquery as cq

# Define dimensions
outer_diameter = 20.0
inner_hole_diameter = 8.0
inner_ring_diameter = 12.0
height = 10.0

# Create the main cylindrical part with central hole
result = (
    cq.Workplane("XY")
    .circle(outer_diameter / 2.0)  # Outer cylinder
    .circle(inner_hole_diameter / 2.0)  # Inner hole
    .extrude(height)
)

# Create the inner ring
result = (
    result.faces(">Z")
    .workplane()
    .circle(inner_ring_diameter / 2.0)
    .circle(inner_hole_diameter / 2.0)
    .extrude(height/2.0)
)