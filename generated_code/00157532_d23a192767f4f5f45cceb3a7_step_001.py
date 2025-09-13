import cadquery as cq

# Define dimensions
main_body_width = 40.0
main_body_height = 30.0
main_body_depth = 20.0
cylinder_diameters = [12.0, 10.0, 8.0, 6.0]  # Varying diameters
cylinder_height = 4.0
cylinder_spacing = 5.0
cutout_width = 4.0
cutout_height = 3.0
cutout_depth = 2.0

# Create the main body with rounded edges
main_body = (
    cq.Workplane("XY")
    .box(main_body_width, main_body_height, main_body_depth)
    .edges("|Z").fillet(2.0)
    .faces(">Z").workplane().rect(20, 15, forConstruction=True).vertices().hole(3.0)
)

# Create the protruding section with stacked cylinders
protruding_section = cq.Workplane("XY").center(0, 15).center(0, 0)

# Add cylinders
for i, diameter in enumerate(cylinder_diameters):
    y_offset = i * (cylinder_height + cylinder_spacing)
    cylinder = (
        cq.Workplane("XY")
        .center(0, y_offset)
        .circle(diameter/2)
        .extrude(cylinder_height)
    )
    protruding_section = protruding_section.union(cylinder)

# Create cutouts in each cylinder
cutout = cq.Workplane("XY").rect(cutout_width, cutout_height).extrude(cutout_depth)
cutout_pos = -cutout_depth/2

for i, diameter in enumerate(cylinder_diameters):
    y_offset = i * (cylinder_height + cylinder_spacing)
    cutout_placed = cutout.translate((0, y_offset, cutout_pos))
    protruding_section = protruding_section.cut(cutout_placed)

# Position the protruding section on top of the main body
result = main_body.union(protruding_section.translate((0, 0, main_body_depth)))

# Ensure smooth connection between main body and protruding section
result = result.edges("|Z").fillet(1.0)