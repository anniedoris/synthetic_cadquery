import cadquery as cq

# Define dimensions
cylinder_diameter = 20.0
cylinder_height = 10.0
wall_thickness = 2.0
flange_width = 8.0
flange_height = 4.0
flange_length = 12.0
hole_diameter = 3.0
groove_depth = 1.0
groove_width = 2.0

# Create the main cylindrical body
cylinder_radius = cylinder_diameter / 2.0
inner_radius = cylinder_radius - wall_thickness

# Create the outer cylinder
outer_cylinder = cq.Workplane("XY").circle(cylinder_radius).extrude(cylinder_height)

# Create the inner cylinder (to make it hollow)
inner_cylinder = cq.Workplane("XY").circle(inner_radius).extrude(cylinder_height)

# Subtract to create the hollow cylinder
result = outer_cylinder.cut(inner_cylinder)

# Add the internal groove
groove_offset = cylinder_radius - wall_thickness - groove_width/2
groove = cq.Workplane("XY").center(0, 0).circle(groove_offset + groove_width/2).extrude(groove_depth)
groove_cut = cq.Workplane("XY").center(0, 0).circle(groove_offset - groove_width/2).extrude(groove_depth)
result = result.cut(groove_cut)

# Create the left flange
left_flange = cq.Workplane("YZ").center(-flange_length/2, 0).rect(flange_length, flange_height).extrude(flange_width)
result = result.union(left_flange)

# Create the right flange
right_flange = cq.Workplane("YZ").center(flange_length/2, 0).rect(flange_length, flange_height).extrude(flange_width)
result = result.union(right_flange)

# Add holes to the left flange
left_hole_pos = flange_length/2 - 2.0
left_hole = cq.Workplane("YZ").center(-left_hole_pos, 0).circle(hole_diameter/2).extrude(flange_width)
result = result.cut(left_hole)

left_hole2 = cq.Workplane("YZ").center(-left_hole_pos, 2.0).circle(hole_diameter/2).extrude(flange_width)
result = result.cut(left_hole2)

# Add holes to the right flange
right_hole_pos = flange_length/2 - 2.0
right_hole = cq.Workplane("YZ").center(right_hole_pos, 0).circle(hole_diameter/2).extrude(flange_width)
result = result.cut(right_hole)

right_hole2 = cq.Workplane("YZ").center(right_hole_pos, 2.0).circle(hole_diameter/2).extrude(flange_width)
result = result.cut(right_hole2)

# Add some surface lines to represent manufacturing details
# Horizontal lines on the outer surface
line1 = cq.Workplane("XY").center(0, 0).circle(cylinder_radius - 0.5).extrude(0.1)
line2 = cq.Workplane("XY").center(0, 0).circle(cylinder_radius - 1.5).extrude(0.1)
result = result.union(line1).union(line2)