import cadquery as cq

# Dimensions
top_length = 20.0
top_width = 15.0
top_height = 8.0

base_length = 25.0
base_width = 20.0
base_height = 12.0

recess_depth = 5.0
recess_width = 8.0
recess_height = 4.0

hole_diameter = 2.0
mounting_hole_diameter = 3.0
support_leg_height = 2.0
cable_cutout_width = 6.0
cable_cutout_height = 3.0

# Create the base section
result = cq.Workplane("XY").box(base_length, base_width, base_height)

# Create the top section and position it
top = cq.Workplane("XY").box(top_length, top_width, top_height)
top = top.translate((0, 0, base_height))
result = result.union(top)

# Add the recessed area on one side of the base
recess_origin_x = (base_length - recess_width) / 2
recess_origin_y = (base_width - recess_depth) / 2
recess = cq.Workplane("XY").rect(recess_width, recess_depth).extrude(recess_height)
recess = recess.translate((recess_origin_x, recess_origin_y, base_height - recess_height))
result = result.cut(recess)

# Add the circular feature inside the recess
circle_origin_x = recess_origin_x + recess_width / 2
circle_origin_y = recess_origin_y + recess_depth / 2
circle = cq.Workplane("XY").circle(hole_diameter/2).extrude(recess_height)
circle = circle.translate((circle_origin_x, circle_origin_y, base_height - recess_height))
result = result.cut(circle)

# Add the two mounting holes on the side
mounting_hole_offset_x = (base_length - mounting_hole_diameter) / 2
mounting_hole_offset_y = (base_width - mounting_hole_diameter) / 2

# First mounting hole
hole1 = cq.Workplane("XY").circle(mounting_hole_diameter/2).extrude(base_height)
hole1 = hole1.translate((mounting_hole_offset_x, mounting_hole_offset_y, 0))
result = result.cut(hole1)

# Second mounting hole
hole2 = cq.Workplane("XY").circle(mounting_hole_diameter/2).extrude(base_height)
hole2 = hole2.translate((base_length - mounting_hole_offset_x, base_width - mounting_hole_offset_y, 0))
result = result.cut(hole2)

# Add the small protruding feature near the bottom
support_leg_width = 4.0
support_leg_length = 4.0
support_leg = cq.Workplane("XY").rect(support_leg_width, support_leg_length).extrude(support_leg_height)
support_leg = support_leg.translate((base_length/2 - support_leg_width/2, base_width - support_leg_length, 0))
result = result.union(support_leg)

# Add the rectangular cutout near the bottom
cutout_origin_x = (base_length - cable_cutout_width) / 2
cutout_origin_y = (base_width - cable_cutout_height) / 2
cutout = cq.Workplane("XY").rect(cable_cutout_width, cable_cutout_height).extrude(1.0)
cutout = cutout.translate((cutout_origin_x, cutout_origin_y, 0))
result = result.cut(cutout)

# Add the small circular hole near the top
top_hole = cq.Workplane("XY").circle(hole_diameter/2).extrude(top_height)
top_hole = top_hole.translate((top_length/2, top_width/2, base_height))
result = result.cut(top_hole)