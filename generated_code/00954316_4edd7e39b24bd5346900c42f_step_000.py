import cadquery as cq

# Dimensions
length = 100.0
width = 60.0
height = 40.0
wall_thickness = 5.0
support_width = 10.0
support_height = 30.0
cutout_width = 6.0
cutout_height = 8.0
chamfer_radius = 3.0

# Create the main box with open top
result = cq.Workplane("XY").box(length, width, height)

# Create internal supports
# Left support
result = (
    result.faces("<X")
    .workplane(offset=wall_thickness)
    .rect(support_width, support_height, forConstruction=True)
    .vertices()
    .rect(support_width, support_height)
    .extrude(height - wall_thickness)
)

# Right support
result = (
    result.faces(">X")
    .workplane(offset=-wall_thickness)
    .rect(support_width, support_height, forConstruction=True)
    .vertices()
    .rect(support_width, support_height)
    .extrude(height - wall_thickness)
)

# Add cutouts to supports
# Left support cutouts
result = (
    result.faces("<X")
    .workplane(offset=wall_thickness + support_height - cutout_height)
    .rect(cutout_width, cutout_height, forConstruction=True)
    .vertices()
    .rect(cutout_width, cutout_height)
    .cutBlind(-cutout_height)
)

# Right support cutouts
result = (
    result.faces(">X")
    .workplane(offset=-wall_thickness - support_height + cutout_height)
    .rect(cutout_width, cutout_height, forConstruction=True)
    .vertices()
    .rect(cutout_width, cutout_height)
    .cutBlind(cutout_height)
)

# Add chamfers to top edges
result = (
    result.faces(">Z")
    .edges()
    .chamfer(chamfer_radius)
)

# Ensure we have the final result
result = result