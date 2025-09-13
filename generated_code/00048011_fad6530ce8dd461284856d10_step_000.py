import cadquery as cq

# Define dimensions
base_length = 50.0
base_width = 30.0
base_thickness = 5.0

l_shape_width = 20.0
l_shape_height = 15.0

protrusion1_length = 10.0
protrusion1_width = 8.0
protrusion1_height = 5.0

protrusion2_length = 10.0
protrusion2_width = 8.0
protrusion2_height = 5.0

protrusion3_length = 8.0
protrusion3_width = 10.0
protrusion3_height = 5.0

# Create the base platform
result = cq.Workplane("XY").box(base_length, base_width, base_thickness)

# Add the L-shaped feature
# First section of L-shape
l_shape_section1 = (
    cq.Workplane("XY")
    .moveTo(base_length/2, -base_width/2)
    .lineTo(base_length/2 + l_shape_width, -base_width/2)
    .lineTo(base_length/2 + l_shape_width, -base_width/2 + l_shape_height)
    .lineTo(base_length/2, -base_width/2 + l_shape_height)
    .close()
    .extrude(base_thickness)
)

# Second section of L-shape (vertical)
l_shape_section2 = (
    cq.Workplane("XY")
    .moveTo(base_length/2, -base_width/2 + l_shape_height)
    .lineTo(base_length/2 + l_shape_width, -base_width/2 + l_shape_height)
    .lineTo(base_length/2 + l_shape_width, -base_width/2 + l_shape_height + l_shape_height)
    .lineTo(base_length/2, -base_width/2 + l_shape_height + l_shape_height)
    .close()
    .extrude(base_thickness)
)

# Add the first rectangular protrusion (near corner)
protrusion1 = (
    cq.Workplane("XY")
    .moveTo(-base_length/2 + protrusion1_length/2, -base_width/2 + protrusion1_width/2)
    .rect(protrusion1_length, protrusion1_width)
    .extrude(protrusion1_height)
)

# Add the second rectangular protrusion (on opposite side)
protrusion2 = (
    cq.Workplane("XY")
    .moveTo(base_length/2 - protrusion2_length/2, base_width/2 - protrusion2_width/2)
    .rect(protrusion2_length, protrusion2_width)
    .extrude(protrusion2_height)
)

# Add the third rectangular protrusion (near end of L-shape)
protrusion3 = (
    cq.Workplane("XY")
    .moveTo(base_length/2 + l_shape_width - protrusion3_length/2, -base_width/2 + l_shape_height + protrusion3_width/2)
    .rect(protrusion3_length, protrusion3_width)
    .extrude(protrusion3_height)
)

# Combine all parts
result = result.union(l_shape_section1)
result = result.union(l_shape_section2)
result = result.union(protrusion1)
result = result.union(protrusion2)
result = result.union(protrusion3)