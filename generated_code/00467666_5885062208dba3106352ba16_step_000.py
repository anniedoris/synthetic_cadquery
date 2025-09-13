import cadquery as cq

# Define dimensions
length = 100.0
width = 20.0
height = 10.0
hole_diameter = 4.0
hole_spacing = 15.0
hole_offset = (length - 5 * hole_spacing) / 2  # Center the holes

# Create the base block
result = cq.Workplane("XY").box(length, width, height)

# Add the holes
for i in range(6):
    x_pos = hole_offset + i * hole_spacing
    result = (
        result.faces(">Z")
        .workplane(offset=0, centerOption="CenterOfBoundBox")
        .center(x_pos - length/2, 0)
        .hole(hole_diameter)
    )

# Round the corners slightly for a more realistic appearance
result = result.edges("|Z").fillet(1.0)