import cadquery as cq

# Dimensions
leg_width = 20.0
leg_depth = 10.0
leg_height = 50.0
top_curve_radius = 15.0
top_thickness = 10.0
reinforcement_width = 5.0

# Create the base U-shaped structure
# First, create the left leg
left_leg = cq.Workplane("XY").box(leg_width, leg_depth, leg_height)

# Create the right leg offset to the right
right_leg = cq.Workplane("XY").translate((leg_width + top_curve_radius * 2, 0, 0)).box(leg_width, leg_depth, leg_height)

# Combine the legs
result = left_leg.union(right_leg)

# Create the curved top section
# The curved section should connect the tops of both legs
# We'll create a U-shaped curve with the specified radius
top_section = (
    cq.Workplane("XY")
    .moveTo(leg_width/2, leg_height)
    .threePointArc((leg_width/2 + top_curve_radius, leg_height + top_curve_radius), (leg_width/2 + top_curve_radius * 2, leg_height))
    .lineTo(leg_width/2 + top_curve_radius * 2, leg_height - top_thickness)
    .threePointArc((leg_width/2 + top_curve_radius, leg_height - top_thickness - top_curve_radius), (leg_width/2, leg_height - top_thickness))
    .close()
    .extrude(top_thickness)
)

# Position the top section correctly
top_section = top_section.translate((0, -leg_depth/2, 0))

# Add the top section to the result
result = result.union(top_section)

# Add reinforcement at connection points
# Create reinforcement on the left leg
left_reinforcement = (
    cq.Workplane("XY")
    .moveTo(0, leg_height - top_thickness)
    .lineTo(0, leg_height)
    .lineTo(reinforcement_width, leg_height)
    .lineTo(reinforcement_width, leg_height - top_thickness)
    .close()
    .extrude(leg_depth)
)
left_reinforcement = left_reinforcement.translate((0, -leg_depth/2, 0))
result = result.union(left_reinforcement)

# Create reinforcement on the right leg
right_reinforcement = (
    cq.Workplane("XY")
    .moveTo(leg_width + top_curve_radius * 2, leg_height - top_thickness)
    .lineTo(leg_width + top_curve_radius * 2, leg_height)
    .lineTo(leg_width + top_curve_radius * 2 - reinforcement_width, leg_height)
    .lineTo(leg_width + top_curve_radius * 2 - reinforcement_width, leg_height - top_thickness)
    .close()
    .extrude(leg_depth)
)
right_reinforcement = right_reinforcement.translate((0, -leg_depth/2, 0))
result = result.union(right_reinforcement)

# Ensure the structure is solid by making it a single solid
result = result.clean()