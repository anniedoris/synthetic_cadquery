import cadquery as cq

# Dimensions
top_length = 100.0
top_width = 60.0
top_thickness = 5.0
leg_height = 80.0
leg_width = 5.0
shelf_height = 30.0
shelf_thickness = 5.0
shelf_gap = 20.0

# Create the top surface
top = cq.Workplane("XY").box(top_length, top_width, top_thickness)

# Create the legs
leg_offset = (top_length - 2 * leg_width) / 2
leg_positions = [
    (-leg_offset, -leg_offset, 0),
    (leg_offset, -leg_offset, 0),
    (-leg_offset, leg_offset, 0),
    (leg_offset, leg_offset, 0)
]

for x, y, z in leg_positions:
    leg = cq.Workplane("XY", origin=(x, y, z)).box(leg_width, leg_width, leg_height)
    top = top.union(leg)

# Create the top horizontal supports
support_height = leg_height - top_thickness
support_length = top_length - 2 * leg_width
support_width = 5.0

# Front and back supports
front_support = cq.Workplane("XY", origin=(0, -leg_offset, leg_height - support_height)).box(support_length, support_width, support_height)
back_support = cq.Workplane("XY", origin=(0, leg_offset, leg_height - support_height)).box(support_length, support_width, support_height)
top = top.union(front_support).union(back_support)

# Side supports
left_support = cq.Workplane("XY", origin=(-leg_offset, 0, leg_height - support_height)).box(support_width, support_length, support_height)
right_support = cq.Workplane("XY", origin=(leg_offset, 0, leg_height - support_height)).box(support_width, support_length, support_height)
top = top.union(left_support).union(right_support)

# Create the shelves
shelf1_z = leg_height - shelf_gap - shelf_thickness
shelf2_z = leg_height - shelf_gap - shelf_thickness - shelf_height - shelf_thickness

# Shelf 1
shelf1 = cq.Workplane("XY", origin=(0, 0, shelf1_z)).box(top_length, top_width, shelf_thickness)
top = top.union(shelf1)

# Shelf 2
shelf2 = cq.Workplane("XY", origin=(0, 0, shelf2_z)).box(top_length, top_width, shelf_thickness)
top = top.union(shelf2)

# Add shelf supports
shelf_support_length = top_length - 2 * leg_width
shelf_support_width = 5.0

# Shelf 1 supports
shelf1_front_support = cq.Workplane("XY", origin=(0, -leg_offset, shelf1_z)).box(shelf_support_length, shelf_support_width, shelf_thickness)
shelf1_back_support = cq.Workplane("XY", origin=(0, leg_offset, shelf1_z)).box(shelf_support_length, shelf_support_width, shelf_thickness)
top = top.union(shelf1_front_support).union(shelf1_back_support)

# Shelf 2 supports
shelf2_front_support = cq.Workplane("XY", origin=(0, -leg_offset, shelf2_z)).box(shelf_support_length, shelf_support_width, shelf_thickness)
shelf2_back_support = cq.Workplane("XY", origin=(0, leg_offset, shelf2_z)).box(shelf_support_length, shelf_support_width, shelf_thickness)
top = top.union(shelf2_front_support).union(shelf2_back_support)

# Create the final result
result = top