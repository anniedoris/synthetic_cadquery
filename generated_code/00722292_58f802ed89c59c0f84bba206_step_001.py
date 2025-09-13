import cadquery as cq

# Define dimensions
main_length = 100.0
main_width = 30.0
main_height = 10.0

left_length = 40.0
left_width = 20.0
left_height = 8.0

right_length = 50.0
right_width = 25.0
right_height = 12.0

# Create the main middle section with cutouts
result = cq.Workplane("XY").box(main_length, main_width, main_height)

# Add cutouts to the middle section
cutout_width = 15.0
cutout_height = 8.0
cutout_spacing = 20.0

# Create cutouts along the middle section
for i in range(3):
    result = (
        result.faces(">Z")
        .workplane(offset=0.1)
        .center(-main_length/2 + cutout_spacing * i + cutout_width/2, 0)
        .rect(cutout_width, cutout_height)
        .cutThruAll()
    )

# Add left section (offset and angled)
left_section = (
    cq.Workplane("XY")
    .box(left_length, left_width, left_height)
    .translate((-main_length/2 - left_length/2, 0, 0))
    .rotate((0, 0, 0), (0, 0, 1), 15)  # Rotate 15 degrees
)

# Add right section (offset and angled)
right_section = (
    cq.Workplane("XY")
    .box(right_length, right_width, right_height)
    .translate((main_length/2 + right_length/2, 0, 0))
    .rotate((0, 0, 0), (0, 0, 1), -10)  # Rotate -10 degrees
)

# Add smaller protrusions to the right section
# Add a rectangular protrusion
result = (
    right_section.faces(">Z")
    .workplane(offset=0.1)
    .center(-right_length/4, 0)
    .rect(8, 6)
    .extrude(3)
)

# Add irregular protrusions to the right section
result = (
    right_section.faces(">Z")
    .workplane(offset=0.1)
    .center(right_length/4, -right_width/4)
    .polygon(5, 5)
    .extrude(2)
)

result = (
    right_section.faces(">Z")
    .workplane(offset=0.1)
    .center(right_length/4, right_width/4)
    .circle(3)
    .extrude(2)
)

# Add cutouts to the right section
result = (
    right_section.faces(">Z")
    .workplane(offset=0.1)
    .center(0, 0)
    .rect(10, 8)
    .cutThruAll()
)

# Combine all parts
result = result.union(left_section).union(right_section)

# Add additional details to the middle section
# Add a small rectangular cutout in the center
result = (
    result.faces(">Z")
    .workplane(offset=0.1)
    .center(0, 0)
    .rect(10, 5)
    .cutThruAll()
)

# Add a fillet to the edges for a more realistic look
result = result.edges("|Z").fillet(1.0)

# Ensure the final object is properly oriented
result = result.rotate((0, 0, 0), (1, 0, 0), 0)

# Final result
result = result