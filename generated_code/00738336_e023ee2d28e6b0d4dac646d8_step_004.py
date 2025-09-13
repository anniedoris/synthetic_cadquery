import cadquery as cq

# Define dimensions
outer_width = 10.0
outer_height = 8.0
outer_depth = 6.0
thickness = 1.0

# Create the outer box
outer_box = cq.Workplane("XY").box(outer_width, outer_height, outer_depth)

# Create the inner box (smaller by 2*thickness on each dimension)
inner_width = outer_width - 2 * thickness
inner_height = outer_height - 2 * thickness
inner_depth = outer_depth - 2 * thickness

# Create the inner box
inner_box = cq.Workplane("XY").box(inner_width, inner_height, inner_depth)

# Subtract the inner box from the outer box to create the frame
result = outer_box.cut(inner_box)

# Add some perspective by rotating slightly to show trapezoidal faces
result = result.rotate((0, 0, 0), (1, 0, 0), 15)
result = result.rotate((0, 0, 0), (0, 1, 0), 10)