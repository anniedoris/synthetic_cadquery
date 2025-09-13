import cadquery as cq

# Define dimensions
outer_diameter = 20.0
inner_diameter = 8.0
height = 20.0

# Create the cylindrical part with central bore
result = (
    cq.Workplane("XY")
    .circle(outer_diameter / 2.0)
    .circle(inner_diameter / 2.0)
    .extrude(height)
)