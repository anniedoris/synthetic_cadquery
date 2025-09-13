import cadquery as cq

# Define dimensions
outer_diameter = 20.0
inner_diameter = 12.0
height = 10.0

# Create the cylindrical sleeve (hollow cylinder)
result = (
    cq.Workplane("XY")
    .circle(outer_diameter / 2.0)           # Outer circle
    .circle(inner_diameter / 2.0)           # Inner circle (concentric)
    .extrude(height)                       # Extrude to desired height
)

# The result is a hollow cylinder with smooth edges and flat top/bottom surfaces