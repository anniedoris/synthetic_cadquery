import cadquery as cq
from math import sqrt

# Define dimensions
cylinder_diameter = 10.0
cylinder_height = 5.0
hexagon_diameter = 12.0  # Across flats
hexagon_height = 4.0
cone_base_diameter = 14.0
cone_top_diameter = 8.0
cone_height = 6.0
internal_bore_diameter = 6.0
internal_bore_depth = 8.0

# Create the cylindrical shaft
result = cq.Workplane("XY").circle(cylinder_diameter/2).extrude(cylinder_height)

# Add the hexagonal section
result = (
    result.faces(">Z")
    .workplane()
    .polygon(6, hexagon_diameter)
    .extrude(hexagon_height)
)

# Add the conical section
result = (
    result.faces(">Z")
    .workplane()
    .circle(cone_base_diameter/2)
    .workplane(offset=cone_height)
    .circle(cone_top_diameter/2)
    .loft(combine=True)
)

# Create the internal cavity
result = (
    result.faces(">Z")
    .workplane()
    .circle(internal_bore_diameter/2)
    .extrude(internal_bore_depth)
)

# Ensure the internal cavity goes through the entire conical section
# Calculate the depth of the conical section that's within the internal bore
cone_bottom_z = cylinder_height + hexagon_height
cone_top_z = cone_bottom_z + cone_height

# If the internal bore extends beyond the conical section, we'll need to cut it
# to just the appropriate depth. However, the way we've built it, it should
# already be correct since we extruded the full depth.

# But to be more precise, let's cut the bore properly through the conical section
# First, get the conical face and cut from there
result = (
    result.faces(">Z")
    .workplane()
    .circle(internal_bore_diameter/2)
    .cutBlind(-internal_bore_depth)
)