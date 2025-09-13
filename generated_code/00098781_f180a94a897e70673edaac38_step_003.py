import cadquery as cq

# Dimensions for the dual outlet cover
length = 100.0   # Length of the plate
width = 50.0     # Width of the plate
thickness = 12.0 # Thickness of the plate

# Oval cutout dimensions
oval_width = 30.0   # Width of each oval cutout
oval_height = 18.0  # Height of each oval cutout

# Radius for rounded edges
edge_radius = 4.0

# Create the base rectangular plate with rounded edges
result = (
    cq.Workplane("XY")
    .box(length, width, thickness)
    .edges("|Z")
    .fillet(edge_radius)
)

# Create the first oval cutout (left side)
oval_offset_x = -20.0  # Offset from center to position the oval
result = (
    result.faces(">Z")
    .workplane()
    .center(oval_offset_x, 0)
    .ellipse(oval_width, oval_height)
    .cutThruAll()
)

# Create the second oval cutout (right side)
result = (
    result.faces(">Z")
    .workplane()
    .center(-oval_offset_x, 0)
    .ellipse(oval_width, oval_height)
    .cutThruAll()
)

# Optional: Add mounting holes (not visible in the description but typical for such plates)
# These would be placed near the corners
mounting_hole_diameter = 3.0
mounting_hole_offset = 15.0

result = (
    result.faces("<Z")
    .workplane()
    .center(mounting_hole_offset, mounting_hole_offset)
    .circle(mounting_hole_diameter/2)
    .cutThruAll()
    .center(-2*mounting_hole_offset, 0)
    .circle(mounting_hole_diameter/2)
    .cutThruAll()
    .center(0, -mounting_hole_offset)
    .circle(mounting_hole_diameter/2)
    .cutThruAll()
)