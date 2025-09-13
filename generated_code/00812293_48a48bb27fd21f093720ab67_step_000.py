import cadquery as cq

# Define dimensions
outer_width = 20.0
outer_height = 10.0
thickness = 2.0
length = 50.0

# Create the outer rectangular prism
outer_box = cq.Workplane("XY").box(outer_width, outer_height, length)

# Create the inner rectangular prism (to be subtracted)
# The inner dimensions are reduced by twice the thickness
inner_width = outer_width - 2 * thickness
inner_height = outer_height - 2 * thickness
inner_box = cq.Workplane("XY").box(inner_width, inner_height, length)

# Position the inner box to be centered
inner_box = inner_box.translate((0, 0, 0))

# Subtract the inner box from the outer box to create the hollow channel
result = outer_box.cut(inner_box)