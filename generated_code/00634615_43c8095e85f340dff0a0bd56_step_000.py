import cadquery as cq

# Base plate dimensions
plate_width = 50.0
plate_height = 50.0
plate_thickness = 5.0
edge_radius = 3.0

# Cylindrical protrusion dimensions
cylinder_diameter = 10.0
cylinder_height = 15.0

# Rectangular feature dimensions
rect_width = 8.0
rect_height = 12.0
rect_thickness = 5.0

# Additional component dimensions
comp_width = 20.0
comp_height = 15.0
comp_thickness = 3.0
hole_diameter = 4.0

# Create the base plate with rounded edges
result = (
    cq.Workplane("XY")
    .box(plate_width, plate_height, plate_thickness)
    .edges("|Z")
    .fillet(edge_radius)
)

# Add holes to the base plate
hole_spacing = 10.0
for i in range(4):
    for j in range(4):
        result = (
            result.faces(">Z")
            .workplane()
            .center(-plate_width/2 + i*hole_spacing, -plate_height/2 + j*hole_spacing)
            .hole(2.0)
        )

# Add cylindrical protrusion at bottom-left corner
result = (
    result.faces("<X and <Y")
    .workplane(offset=-plate_thickness/2)
    .center(plate_width/2 - cylinder_diameter/2, plate_height/2 - cylinder_diameter/2)
    .circle(cylinder_diameter/2)
    .extrude(cylinder_height)
)

# Add rectangular feature on the side of the cylinder
result = (
    result.faces(">Y and <Z")
    .workplane(offset=cylinder_height/2)
    .center(0, cylinder_diameter/2 + rect_width/2)
    .rect(rect_width, rect_height)
    .extrude(rect_thickness)
)

# Create additional component in bottom right
additional_comp = (
    cq.Workplane("XY")
    .box(comp_width, comp_height, comp_thickness)
    .faces(">Z")
    .workplane()
    .center(0, 0)
    .circle(hole_diameter/2)
    .extrude(comp_thickness)
    .faces(">Z")
    .workplane()
    .center(-comp_width/2 + hole_diameter, comp_height/2 - hole_diameter)
    .rect(8, 6)
    .extrude(comp_thickness/2)
)

# Position the additional component
result = result.union(
    additional_comp.translate((
        plate_width/2 - comp_width/2 - 10,
        -plate_height/2 + comp_height/2 + 10,
        0
    ))
)

# Apply perspective by rotating
result = result.rotate((0, 0, 0), (1, 0, 0), 15)
result = result.rotate((0, 0, 0), (0, 1, 0), 15)