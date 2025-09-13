import cadquery as cq

# Base plate dimensions
base_length = 50.0
base_width = 30.0
base_thickness = 5.0

# Cylinder dimensions
cylinder_outer_diameter = 12.0
cylinder_inner_diameter = 8.0
cylinder_height = base_width  # Equal to the width of the base plate

# Create the base plate
result = cq.Workplane("XY").box(base_length, base_width, base_thickness)

# Create the cylindrical protrusion
# Move to the center of one of the longer sides (we'll use the front side)
# The front side is along the Y-axis, so we center on the X-axis and position at Y = width/2
result = (
    result.faces(">Z")
    .workplane(offset=base_thickness)
    .center(-base_length/2 + cylinder_outer_diameter/2, 0)
    .circle(cylinder_outer_diameter/2)
    .extrude(cylinder_height)
)

# Create the hollow center of the cylinder
result = (
    result.faces(">Z")
    .workplane(offset=cylinder_height)
    .circle(cylinder_inner_diameter/2)
    .cutBlind(cylinder_height)
)

# Ensure we have a clean annular shape by cutting the inner cylinder
result = (
    result.faces(">Z")
    .workplane(offset=cylinder_height)
    .circle(cylinder_inner_diameter/2)
    .extrude(-cylinder_height)
)