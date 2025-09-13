import cadquery as cq

# Define dimensions
plate_length = 80.0
plate_width = 40.0
plate_thickness = 5.0
cylinder_diameter = 10.0
cylinder_length = 20.0
bottom_hole_diameter = 8.0
top_hole_diameter = 4.0
bottom_hole_spacing = 30.0
top_hole_spacing = 15.0
top_hole_row_offset = 10.0

# Create the base plate
result = cq.Workplane("XY").box(plate_length, plate_width, plate_thickness)

# Add bottom holes
result = (
    result.faces(">Z")
    .workplane()
    .center(-bottom_hole_spacing/2, -plate_width/2 + 10)
    .circle(bottom_hole_diameter/2)
    .center(bottom_hole_spacing, 0)
    .circle(bottom_hole_diameter/2)
    .cutThruAll()
)

# Add top holes
result = (
    result.faces(">Z")
    .workplane()
    .center(-top_hole_spacing, plate_width/2 - 10)
    .circle(top_hole_diameter/2)
    .center(top_hole_spacing, 0)
    .circle(top_hole_diameter/2)
    .center(0, -top_hole_row_offset)
    .circle(top_hole_diameter/2)
    .center(top_hole_spacing, 0)
    .circle(top_hole_diameter/2)
    .cutThruAll()
)

# Create the L-shape bend and cylinder
# First, we need to create a workplane at the end of the plate
result = (
    result.faces(">Y")
    .workplane(offset=plate_thickness)
    .center(plate_length/2 - cylinder_length/2, 0)
    .circle(cylinder_diameter/2)
    .extrude(cylinder_length)
)

# Create a fillet where the cylinder meets the plate
result = result.edges("|Z").fillet(2.0)

# Make sure the cylinder extends out from the plate properly
result = (
    result.faces(">Y")
    .workplane(offset=plate_thickness)
    .center(plate_length/2 - cylinder_length/2, 0)
    .circle(cylinder_diameter/2)
    .extrude(cylinder_length)
)

# Add fillet to the connection between plate and cylinder
result = result.edges("#Z").fillet(1.0)

result = result.translate((0, 0, 0))