import cadquery as cq

# Dimensions
base_width = 50.0
base_height = 50.0
base_thickness = 10.0
shaft_diameter = 12.0
shaft_height = 15.0
top_plate_diameter = 30.0
mounting_hole_diameter = 4.0
mounting_hole_depth = 3.0
chamfer_radius = 2.0

# Create the base with chamfered edges
result = cq.Workplane("XY").box(base_width, base_height, base_thickness)

# Chamfer the edges of the base
result = result.edges("|Z").chamfer(chamfer_radius)

# Create the central shaft
result = (
    result.faces(">Z")
    .workplane()
    .center(0, 0)
    .circle(shaft_diameter / 2.0)
    .extrude(shaft_height)
)

# Create the flat top of the shaft
result = (
    result.faces(">Z")
    .workplane()
    .center(0, 0)
    .circle(shaft_diameter / 2.0)
    .extrude(1.0)
)

# Create the circular top plate
result = (
    result.faces(">Z")
    .workplane()
    .center(0, 0)
    .circle(top_plate_diameter / 2.0)
    .cutBlind(-1.0)
)

# Create mounting holes at each corner
result = (
    result.faces("<Z")
    .workplane()
    .rect(base_width - 10, base_height - 10, forConstruction=True)
    .vertices()
    .cboreHole(mounting_hole_diameter, mounting_hole_diameter * 1.5, mounting_hole_depth)
)

# Ensure the top plate is flush with the shaft top
result = (
    result.faces(">Z")
    .workplane()
    .center(0, 0)
    .circle(top_plate_diameter / 2.0)
    .cutBlind(-1.0)
)

# Final result
result = result