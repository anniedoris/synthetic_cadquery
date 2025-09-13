import cadquery as cq

# Define dimensions
width = 100.0   # Width of the ladder frame
height = 200.0  # Height of the ladder frame
depth = 20.0    # Depth/thickness of the vertical sides
rung_thickness = 10.0  # Thickness of the rungs
rung_width = 80.0      # Width of the rungs
rung_height = 10.0     # Height of the rungs (thickness)
screw_diameter = 4.0   # Diameter of the screw holes
screw_offset = 5.0     # Offset from the top edge for screw holes

# Create the vertical sides
# Left vertical side
left_side = cq.Workplane("XY").box(depth, width, height)

# Right vertical side
right_side = cq.Workplane("XY").box(depth, width, height).translate((height, 0, 0))

# Combine the vertical sides
ladder_frame = left_side.union(right_side)

# Create the horizontal rungs
# First rung (bottom)
rung1 = cq.Workplane("XY").box(rung_width, rung_thickness, rung_height).translate((0, (width - rung_thickness) / 2, 0))

# Second rung (middle)
rung2 = cq.Workplane("XY").box(rung_width, rung_thickness, rung_height).translate((0, (width - rung_thickness) / 2, height/2))

# Third rung (top)
rung3 = cq.Workplane("XY").box(rung_width, rung_thickness, rung_height).translate((0, (width - rung_thickness) / 2, height))

# Add the rungs to the ladder frame
ladder_frame = ladder_frame.union(rung1).union(rung2).union(rung3)

# Create screw holes at the top corners
# Top left screw hole
screw1 = cq.Workplane("XY").circle(screw_diameter/2).extrude(depth).translate((0, 0, height - screw_offset))

# Top right screw hole
screw2 = cq.Workplane("XY").circle(screw_diameter/2).extrude(depth).translate((height, 0, height - screw_offset))

# Add screw holes to the ladder frame
ladder_frame = ladder_frame.cut(screw1).cut(screw2)

# Create a more realistic structure by subtracting the inner part of the vertical sides
# This creates a hollow frame effect
inner_depth = depth - 2
inner_width = width - 2
inner_height = height - 2

# Inner vertical sides
inner_left = cq.Workplane("XY").box(inner_depth, inner_width, inner_height).translate((1, 1, 1))
inner_right = cq.Workplane("XY").box(inner_depth, inner_width, inner_height).translate((height + 1, 1, 1))

# Create the final ladder structure
result = ladder_frame.cut(inner_left).cut(inner_right)

# Alternative approach: Create a more precise frame with proper spacing and features
# Base workplane
base = cq.Workplane("XY")

# Create vertical sides with proper dimensions
# Left side
left_side = base.rect(depth, width).extrude(height).translate((0, 0, 0))

# Right side
right_side = base.rect(depth, width).extrude(height).translate((height, 0, 0))

# Combine sides
ladder_with_sides = left_side.union(right_side)

# Create rungs
# Rungs at different heights
rung_y_pos = (width - rung_thickness) / 2
rung1_pos = 0
rung2_pos = height/2
rung3_pos = height

# Rung 1 (bottom)
rung1 = base.rect(rung_width, rung_thickness).extrude(rung_height).translate((0, rung_y_pos, rung1_pos))

# Rung 2 (middle)
rung2 = base.rect(rung_width, rung_thickness).extrude(rung_height).translate((0, rung_y_pos, rung2_pos))

# Rung 3 (top)
rung3 = base.rect(rung_width, rung_thickness).extrude(rung_height).translate((0, rung_y_pos, rung3_pos))

# Combine all parts
ladder = ladder_with_sides.union(rung1).union(rung2).union(rung3)

# Create screw holes at top corners
# Top left screw hole
screw1 = base.circle(screw_diameter/2).extrude(depth).translate((0, 0, height - screw_offset))

# Top right screw hole
screw2 = base.circle(screw_diameter/2).extrude(depth).translate((height, 0, height - screw_offset))

# Add screw holes
result = ladder.cut(screw1).cut(screw2)