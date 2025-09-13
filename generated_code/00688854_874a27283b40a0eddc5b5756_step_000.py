import cadquery as cq

# Define dimensions
base_length = 40.0
base_width = 30.0
base_height = 5.0

cylinder_diameter = 20.0
cylinder_height = 20.0
cylinder_thickness = 2.0

# Create the rectangular base
result = cq.Workplane("XY").box(base_length, base_width, base_height)

# Create the hollow cylindrical top
# First, create the outer cylinder
outer_cylinder = cq.Workplane("XY").center(0, 0).circle(cylinder_diameter / 2.0).extrude(cylinder_height)

# Then, create the inner cylinder to make it hollow
inner_cylinder = cq.Workplane("XY").center(0, 0).circle((cylinder_diameter - 2 * cylinder_thickness) / 2.0).extrude(cylinder_height)

# Subtract the inner cylinder from the outer cylinder to create the hollow part
cylinder = outer_cylinder.cut(inner_cylinder)

# Position the cylinder on top of the base
result = result.union(cylinder)

# Ensure the cylinder is centered on the base
result = result.translate((0, 0, base_height))