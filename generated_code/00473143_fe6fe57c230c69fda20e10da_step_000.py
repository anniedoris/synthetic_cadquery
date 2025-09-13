import cadquery as cq

# Define dimensions
outer_length = 100.0
outer_width = 60.0
outer_height = 40.0
wall_thickness = 5.0

# Create the outer box
outer_box = cq.Workplane("XY").box(outer_length, outer_width, outer_height)

# Create the inner box (hollow part)
# The inner dimensions are reduced by twice the wall thickness
inner_length = outer_length - 2 * wall_thickness
inner_width = outer_width - 2 * wall_thickness
inner_height = outer_height  # No bottom thickness needed since we want an open top

# Position the inner box to be centered
inner_box = cq.Workplane("XY").box(inner_length, inner_width, inner_height).translate((0, 0, wall_thickness))

# Subtract the inner box from the outer box to create the hollow structure
result = outer_box.cut(inner_box)