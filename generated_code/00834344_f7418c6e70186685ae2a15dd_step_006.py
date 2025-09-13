import cadquery as cq

# Define dimensions
length = 100.0
width = 50.0
height = 30.0
thickness = 3.0

# Create the outer box
result = cq.Workplane("XY").box(length, width, height)

# Hollow out the interior by subtracting a smaller box
inner_length = length - 2 * thickness
inner_width = width - 2 * thickness
inner_height = height - thickness  # Leave room for the shelf
result = result.cut(cq.Workplane("XY").box(inner_length, inner_width, inner_height))

# Add the internal shelf (horizontal divider)
shelf_height = height / 2.0
shelf_thickness = thickness
result = result.cut(
    cq.Workplane("XY", origin=(0, 0, shelf_height))
    .box(inner_length, inner_width, shelf_thickness)
)

# Create the front overhang (lip or ledge)
front_overhang = 2.0
result = result.cut(
    cq.Workplane("XY", origin=(0, 0, height - thickness))
    .box(length, front_overhang, thickness)
)

# Add reinforcement at top front corner
reinforcement_thickness = 1.0
result = result.cut(
    cq.Workplane("XY", origin=(length/2 - thickness/2, width/2 - thickness/2, height - thickness))
    .box(reinforcement_thickness, reinforcement_thickness, thickness)
)

# Ensure we have a proper solid with correct orientation
result = result.val().fix()

# Final result
result = result