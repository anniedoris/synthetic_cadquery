import cadquery as cq

# Define dimensions
outer_diameter = 20.0
inner_diameter = 12.0
height = 10.0

# Create the outer cylinder
result = cq.Workplane("XY").circle(outer_diameter / 2.0).extrude(height)

# Create the inner cylinder and subtract it from the outer cylinder
inner_cylinder = cq.Workplane("XY").circle(inner_diameter / 2.0).extrude(height)

# Subtract the inner cylinder from the outer cylinder
result = result.cut(inner_cylinder)