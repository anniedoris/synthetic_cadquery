import cadquery as cq

# Define washer parameters
outer_diameter = 20.0
inner_diameter = 10.0
thickness = 2.0

# Create the washer by extruding the annular profile
result = (
    cq.Workplane("XY")
    .circle(outer_diameter / 2.0)           # Outer circle
    .circle(inner_diameter / 2.0)           # Inner circle (creates the annular shape)
    .extrude(thickness)                     # Give it uniform thickness
)

# The resulting object is a washer/spacer with:
# - Outer diameter: 20.0
# - Inner diameter: 10.0  
# - Thickness: 2.0