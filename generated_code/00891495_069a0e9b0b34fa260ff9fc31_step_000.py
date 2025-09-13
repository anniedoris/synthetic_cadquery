import cadquery as cq

# Define dimensions
shaft_diameter = 10.0
shaft_length = 100.0
left_protrusion_diameter = 6.0
left_protrusion_length = 15.0
rect_block_width = 8.0
rect_block_height = 6.0
rect_block_length = 12.0
small_rect_length = 4.0
small_rect_height = 2.0
small_rect_width = 2.0
right_cylinder_diameter = 15.0
right_cylinder_length = 20.0
right_inner_diameter = 8.0
groove_depth = 1.0
groove_width = 2.0
groove_count = 4
central_bearing_diameter = 5.0
central_bearing_length = 8.0

# Create the main shaft
result = cq.Workplane("XY").box(shaft_length, shaft_diameter, shaft_diameter)

# Add left end features
# Left protrusion
left_protrusion = (
    cq.Workplane("XY")
    .moveTo(-shaft_length/2 + left_protrusion_length/2, 0)
    .box(left_protrusion_length, left_protrusion_diameter, left_protrusion_diameter)
)

# Rectangular block
rect_block = (
    cq.Workplane("XY")
    .moveTo(-shaft_length/2 + left_protrusion_length + rect_block_length/2, 0)
    .box(rect_block_length, rect_block_width, rect_block_height)
)

# Small rectangular protrusion
small_rect = (
    cq.Workplane("XY")
    .moveTo(-shaft_length/2 + left_protrusion_length + rect_block_length + small_rect_length/2, 0)
    .box(small_rect_length, small_rect_width, small_rect_height)
)

# Small cylinder on side of rectangular block
small_cylinder = (
    cq.Workplane("XY")
    .moveTo(-shaft_length/2 + left_protrusion_length + rect_block_length + 1, 0)
    .circle(1.5)
    .extrude(2)
)

# Add right end features
# Right cylinder with stepped design
right_cylinder = (
    cq.Workplane("XY")
    .moveTo(shaft_length/2 - right_cylinder_length/2, 0)
    .box(right_cylinder_length, right_cylinder_diameter, right_cylinder_diameter)
)

# Inner cylinder for the stepped design
inner_cylinder = (
    cq.Workplane("XY")
    .moveTo(shaft_length/2 - right_cylinder_length/2, 0)
    .circle(right_inner_diameter/2)
    .extrude(right_cylinder_diameter)
)

# Add grooves to right cylinder
for i in range(groove_count):
    groove_angle = i * (360 / groove_count)
    groove = (
        cq.Workplane("XY")
        .moveTo(shaft_length/2 - right_cylinder_length/2, 0)
        .circle(right_cylinder_diameter/2 - groove_depth)
        .extrude(groove_width)
        .rotateAboutCenter((0, 0, 1), groove_angle)
    )
    result = result.union(groove)

# Add central bearing
central_bearing = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .circle(central_bearing_diameter/2)
    .extrude(central_bearing_length)
)

# Combine all features
result = result.union(left_protrusion)
result = result.union(rect_block)
result = result.union(small_rect)
result = result.union(small_cylinder)
result = result.union(right_cylinder)
result = result.union(inner_cylinder)
result = result.union(central_bearing)

# Cut the shaft to the correct length
result = result.cut(
    cq.Workplane("XY")
    .moveTo(shaft_length/2 + 1, 0)
    .box(2, shaft_diameter, shaft_diameter)
)

result = result.cut(
    cq.Workplane("XY")
    .moveTo(-shaft_length/2 - 1, 0)
    .box(2, shaft_diameter, shaft_diameter)
)

# Position everything correctly
result = result.translate((0, 0, 0))