import cadquery as cq

# Dimensions
main_length = 100.0
main_width = 20.0
main_height = 10.0
circle_diameter = 4.0
circle_radius = circle_diameter / 2.0
rect_cutout_width = 12.0
rect_cutout_height = 6.0
support_length = 15.0
support_width = 20.0
support_height = 8.0

# Create main body
result = cq.Workplane("XY").box(main_length, main_width, main_height)

# Add circular cutouts on top surface
circle_spacing = (main_length - 2 * circle_radius) / 4  # 5 circles means 4 spaces between
for i in range(5):
    x_pos = -main_length/2 + circle_radius + i * circle_spacing
    result = (
        result.faces(">Z")
        .workplane(offset=0.1)  # Slightly offset to avoid face issues
        .center(x_pos, 0)
        .circle(circle_diameter/2)
        .cutThruAll()
    )

# Add rectangular cutouts on front and back faces
result = (
    result.faces(">Y")
    .workplane()
    .center(0, 0)
    .rect(rect_cutout_width, rect_cutout_height)
    .cutThruAll()
)

result = (
    result.faces("<Y")
    .workplane()
    .center(0, 0)
    .rect(rect_cutout_width, rect_cutout_height)
    .cutThruAll()
)

# Create end supports
# Left support
result = (
    result.faces("<X")
    .workplane(offset=-support_height/2)
    .center(-main_length/2 - support_length/2, 0)
    .box(support_length, support_width, support_height)
    .faces(">Z")
    .workplane()
    .center(0, 0)
    .circle(circle_diameter/2)
    .cutThruAll()
)

# Right support
result = (
    result.faces(">X")
    .workplane(offset=-support_height/2)
    .center(main_length/2 + support_length/2, 0)
    .box(support_length, support_width, support_height)
    .faces(">Z")
    .workplane()
    .center(0, 0)
    .circle(circle_diameter/2)
    .cutThruAll()
)

# Ensure the result is properly assembled
result = result