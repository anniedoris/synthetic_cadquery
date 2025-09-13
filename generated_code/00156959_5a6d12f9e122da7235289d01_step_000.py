import cadquery as cq

# Define dimensions
length = 100.0
width = 20.0
height = 10.0
cutout_radius = 4.0
cutout_spacing = 15.0
flange_length = 10.0
end_rect_width = 8.0
end_rect_height = 6.0

# Create the base rectangular plate
result = cq.Workplane("XY").box(length, width, height)

# Add flanges at both ends
# Left flange
result = result.faces("<X").workplane(offset=-flange_length).box(flange_length, width, height)

# Right flange
result = result.faces(">X").workplane(offset=flange_length).box(flange_length, width, height)

# Add semi-circular cutouts along the length
# Calculate number of cutouts
num_cutouts = int((length - 2 * flange_length) / cutout_spacing) + 1

# Position cutouts along the length
for i in range(num_cutouts):
    cutout_x = -length/2 + flange_length + i * cutout_spacing
    result = (
        result.faces(">Z")
        .workplane(offset=height/2, centerOption="CenterOfBoundBox")
        .center(cutout_x, 0)
        .circle(cutout_radius)
        .cutBlind(-height)
    )

# Add rectangular sections at the ends
# Left end rectangle
result = (
    result.faces("<X")
    .workplane(offset=-flange_length/2)
    .center(-length/2 + flange_length/2, 0)
    .rect(end_rect_width, end_rect_height)
    .extrude(-flange_length)
)

# Right end rectangle
result = (
    result.faces(">X")
    .workplane(offset=flange_length/2)
    .center(length/2 - flange_length/2, 0)
    .rect(end_rect_width, end_rect_height)
    .extrude(flange_length)
)

# Ensure smooth edges by filleting
result = result.edges("|Z").fillet(1.0)

# Ensure top surface is flat
result = result.faces(">Z").workplane().box(length, width, 0.001)

# Final result
result = result