import cadquery as cq

# Define dimensions
cylinder_diameter = 40.0
cylinder_length = 60.0
block_width = 30.0
block_height = 40.0
block_length = 50.0
base_plate_width = 60.0
base_plate_length = 60.0
base_plate_thickness = 5.0
inner_rect_width = 20.0
inner_rect_height = 20.0
inner_rect_length = 30.0
shaft_diameter = 8.0
shaft_length = 15.0
cutout_width = 15.0
cutout_height = 10.0
cutout_depth = 10.0

# Create the cylindrical section
cylinder = cq.Workplane("XY").circle(cylinder_diameter/2).extrude(cylinder_length)

# Create the internal rectangular section
inner_rect = (
    cq.Workplane("XY", origin=(0, 0, cylinder_length/2))
    .rect(inner_rect_width, inner_rect_height)
    .extrude(inner_rect_length)
)

# Create the rectangular block
block = (
    cq.Workplane("XY", origin=(cylinder_length/2, 0, 0))
    .rect(block_width, block_height)
    .extrude(block_length)
)

# Create the cutout on the front face of the block
cutout = (
    cq.Workplane("XY", origin=(cylinder_length/2 + block_length/2, 0, block_height/2))
    .rect(cutout_width, cutout_height)
    .extrude(-cutout_depth)
)

# Create the shaft on top of the block
shaft = (
    cq.Workplane("XY", origin=(cylinder_length/2 + block_length/2, 0, block_height/2 + block_height/2))
    .circle(shaft_diameter/2)
    .extrude(shaft_length)
)

# Create the connecting plate between cylinder and block
connecting_plate = (
    cq.Workplane("XY", origin=(cylinder_length/2, 0, -base_plate_thickness))
    .rect(10, base_plate_width)
    .extrude(base_plate_thickness)
)

# Create the base plate
base_plate = (
    cq.Workplane("XY", origin=(0, 0, -base_plate_thickness))
    .rect(base_plate_width, base_plate_length)
    .extrude(base_plate_thickness)
)

# Combine all elements
result = cylinder.cut(inner_rect)
result = result.union(block)
result = result.cut(cutout)
result = result.union(shaft)
result = result.union(connecting_plate)
result = result.union(base_plate)

# Make the cylinder hollow by subtracting a smaller cylinder
inner_cylinder = cq.Workplane("XY").circle(cylinder_diameter/2 - 5).extrude(cylinder_length)
result = result.cut(inner_cylinder)