import cadquery as cq

# Define dimensions
top_length = 100.0
top_width = 60.0
top_thickness = 5.0
leg_height = 40.0
leg_width = 8.0
leg_depth = 8.0

# Create the top surface
top = cq.Workplane("XY").box(top_length, top_width, top_thickness)

# Create the legs
# Position legs at each corner of the top
leg_offset_x = (top_length - leg_width) / 2
leg_offset_y = (top_width - leg_depth) / 2

# Create one leg and then duplicate it for all four corners
leg = cq.Workplane("XY").box(leg_width, leg_depth, leg_height)

# Position the legs at each corner
result = top
result = result.pushPoints([
    (-leg_offset_x, -leg_offset_y),  # Bottom-left
    (leg_offset_x, -leg_offset_y),   # Bottom-right
    (-leg_offset_x, leg_offset_y),   # Top-left
    (leg_offset_x, leg_offset_y)     # Top-right
]).union(leg)

# Since we want the legs to be separate from the top, we'll create them separately
# and then union them together
legs = cq.Workplane("XY")
legs = legs.pushPoints([
    (-leg_offset_x, -leg_offset_y),  # Bottom-left
    (leg_offset_x, -leg_offset_y),   # Bottom-right
    (-leg_offset_x, leg_offset_y),   # Top-left
    (leg_offset_x, leg_offset_y)     # Top-right
]).box(leg_width, leg_depth, leg_height)

# Combine top and legs
result = top.union(legs)