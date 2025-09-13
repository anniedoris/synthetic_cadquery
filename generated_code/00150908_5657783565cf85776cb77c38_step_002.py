import cadquery as cq

# Define dimensions
horizontal_length = 100.0
horizontal_width = 20.0
horizontal_thickness = 5.0

vertical_length = 60.0
vertical_width = 20.0
vertical_thickness = 5.0

gusset_thickness = 5.0
gusset_length = 25.0

bolt_hole_diameter = 6.0
mounting_plate_width = 15.0
mounting_plate_thickness = 3.0

# Create the horizontal bar
result = cq.Workplane("XY").box(horizontal_length, horizontal_width, horizontal_thickness)

# Add the vertical bar
result = (
    result.faces(">Y")
    .workplane(offset=horizontal_thickness)
    .box(vertical_length, vertical_width, vertical_thickness)
)

# Add the gusset plate at the connection
# Create a triangular gusset connecting the bars
gusset_points = [
    (0, 0, 0),  # bottom left of gusset
    (gusset_length, 0, 0),  # bottom right of gusset
    (0, gusset_length, gusset_thickness),  # top of gusset
]

# Create the gusset as a solid
gusset = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(gusset_length, 0)
    .lineTo(0, gusset_length)
    .close()
    .extrude(gusset_thickness)
)

# Position the gusset at the corner
result = result.union(
    gusset.translate((
        horizontal_length - gusset_length,
        -vertical_width/2 + gusset_length/2,
        horizontal_thickness
    ))
)

# Add bolt hole at the left end of horizontal bar
result = (
    result.faces("<X")
    .workplane()
    .hole(bolt_hole_diameter)
)

# Add mounting plate at the left end of horizontal bar
result = (
    result.faces("<X")
    .workplane(offset=-mounting_plate_thickness)
    .rect(mounting_plate_width, horizontal_width, forConstruction=True)
    .vertices()
    .hole(bolt_hole_diameter)
)

# Add bolt hole at the right end of vertical bar
result = (
    result.faces(">Z")
    .workplane(offset=vertical_length)
    .hole(bolt_hole_diameter)
)

# Add mounting plate at the right end of vertical bar
result = (
    result.faces(">Z")
    .workplane(offset=vertical_length + mounting_plate_thickness)
    .rect(vertical_width, mounting_plate_width, forConstruction=True)
    .vertices()
    .hole(bolt_hole_diameter)
)

# Add mounting plate at the left end of horizontal bar
result = (
    result.faces("<X")
    .workplane(offset=horizontal_thickness + mounting_plate_thickness)
    .rect(mounting_plate_width, horizontal_width, forConstruction=True)
    .vertices()
    .hole(bolt_hole_diameter)
)

# Add mounting plate at the bottom end of vertical bar
result = (
    result.faces("<Y")
    .workplane(offset=vertical_length + mounting_plate_thickness)
    .rect(vertical_width, mounting_plate_width, forConstruction=True)
    .vertices()
    .hole(bolt_hole_diameter)
)