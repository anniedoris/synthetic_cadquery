import cadquery as cq

# Define dimensions
top_length = 200.0
top_width = 100.0
top_thickness = 10.0

leg_width = 20.0
leg_depth = 20.0
leg_height = 150.0

support_length = 190.0  # Slightly shorter than top
support_width = 20.0
support_thickness = 10.0

# Create the top surface
result = cq.Workplane("XY").box(top_length, top_width, top_thickness)

# Create the vertical legs
# Two legs at the ends and one in the center
leg_positions = [
    (-top_length/2 + leg_width, 0, -top_thickness/2),  # Left leg
    (top_length/2 - leg_width, 0, -top_thickness/2),   # Right leg
    (0, 0, -top_thickness/2)                           # Center leg
]

for pos in leg_positions:
    leg = cq.Workplane("XY", origin=pos).box(leg_width, leg_depth, leg_height)
    result = result.union(leg)

# Create bottom supports
# Front and back supports
support_positions = [
    (-support_length/2, -top_width/2 + support_width/2, -top_thickness/2 - leg_height + support_thickness/2),  # Front
    (-support_length/2, top_width/2 - support_width/2, -top_thickness/2 - leg_height + support_thickness/2)   # Back
]

for pos in support_positions:
    support = cq.Workplane("XY", origin=pos).box(support_length, support_width, support_thickness)
    result = result.union(support)

# Ensure proper alignment by centering the entire object
result = result.translate((0, 0, leg_height/2 + top_thickness/2 + support_thickness/2))