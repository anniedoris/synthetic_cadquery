import cadquery as cq
from math import pi

# Define dimensions
outer_diameter = 20.0
inner_diameter = 10.0
length = 30.0
groove_diameter = 12.0
groove_depth = 1.5
groove_count = 6
groove_spacing = length / (groove_count + 1)

# Create the outer cylinder
result = cq.Workplane("XY").circle(outer_diameter/2).extrude(length)

# Create the inner cylinder (shaft)
inner_cylinder = cq.Workplane("XY").circle(inner_diameter/2).extrude(length)

# Subtract the inner cylinder from the outer to create the annular gap
result = result.cut(inner_cylinder)

# Create grooves on the inner surface of the outer cylinder
for i in range(groove_count):
    z_position = groove_spacing * (i + 1)
    # Create a groove at the specified position
    groove = (
        cq.Workplane("XY")
        .center(0, 0)
        .workplane(offset=z_position)
        .circle(groove_diameter/2)
        .circle(inner_diameter/2)
        .extrude(groove_depth)
    )
    result = result.cut(groove)

# Ensure the inner cylinder extends slightly beyond the end faces
# by creating a slightly longer inner cylinder and then cutting
inner_cylinder_extended = cq.Workplane("XY").circle(inner_diameter/2).extrude(length + 2*groove_depth)
result = result.cut(inner_cylinder_extended)

# Create the final inner cylinder with proper extension
inner_cylinder_final = cq.Workplane("XY").circle(inner_diameter/2).extrude(length)
result = result.cut(inner_cylinder_final)

# Alternative approach: Create the final component more directly
result = cq.Workplane("XY").circle(outer_diameter/2).extrude(length)
result = result.faces(">Z").workplane().circle(inner_diameter/2).extrude(length)
result = result.faces("<Z").workplane().circle(inner_diameter/2).extrude(length)

# Create the grooves on the inner surface
for i in range(groove_count):
    z_position = groove_spacing * (i + 1)
    groove = (
        cq.Workplane("XY")
        .center(0, 0)
        .workplane(offset=z_position)
        .circle(groove_diameter/2)
        .circle(inner_diameter/2)
        .extrude(groove_depth)
    )
    result = result.cut(groove)

# Clean up the geometry by creating proper inner cylinder
# Remove the inner cylinder and create a proper annular section
result = cq.Workplane("XY").circle(outer_diameter/2).extrude(length)
result = result.faces(">Z").workplane().circle(inner_diameter/2).extrude(length)

# Create the grooves as recesses on the inner cylindrical surface
groove_radius = (outer_diameter - inner_diameter) / 2 - groove_depth/2
for i in range(groove_count):
    z_position = groove_spacing * (i + 1)
    # Create a recess in the inner cylindrical surface
    recess = (
        cq.Workplane("XY")
        .center(0, 0)
        .workplane(offset=z_position)
        .circle(inner_diameter/2 + groove_radius)
        .circle(inner_diameter/2)
        .extrude(groove_depth)
    )
    result = result.cut(recess)

# Final approach - simpler and cleaner
result = cq.Workplane("XY").circle(outer_diameter/2).extrude(length)
inner_cylinder = cq.Workplane("XY").circle(inner_diameter/2).extrude(length)
result = result.cut(inner_cylinder)

# Create the grooves on the inner cylindrical surface
groove_radius = (outer_diameter - inner_diameter) / 2 - groove_depth/2
for i in range(groove_count):
    z_position = groove_spacing * (i + 1)
    groove = (
        cq.Workplane("XY")
        .center(0, 0)
        .workplane(offset=z_position)
        .circle(inner_diameter/2 + groove_radius)
        .circle(inner_diameter/2)
        .extrude(groove_depth)
    )
    result = result.cut(groove)

# Create a cleaner final version
result = cq.Workplane("XY").circle(outer_diameter/2).extrude(length)

# Create inner cylinder and cut it out
inner_cylinder = cq.Workplane("XY").circle(inner_diameter/2).extrude(length)
result = result.cut(inner_cylinder)

# Create grooves on the inner cylindrical surface
for i in range(groove_count):
    z_position = groove_spacing * (i + 1)
    # Create cylindrical recesses that go around the inner cylinder
    groove_recess = (
        cq.Workplane("XY")
        .center(0, 0)
        .workplane(offset=z_position)
        .circle(inner_diameter/2 + groove_radius)
        .circle(inner_diameter/2)
        .extrude(groove_depth)
    )
    result = result.cut(groove_recess)
    
# More accurate approach - creating proper grooves
result = cq.Workplane("XY").circle(outer_diameter/2).extrude(length)

# Create the inner shaft
inner_shaft = cq.Workplane("XY").circle(inner_diameter/2).extrude(length)
result = result.cut(inner_shaft)

# Create the grooves by subtracting cylindrical recesses from the inner surface
groove_radius = 1.0  # groove radius
for i in range(groove_count):
    z_position = groove_spacing * (i + 1)
    # Create a cylindrical recess to represent the groove
    groove = (
        cq.Workplane("XY")
        .center(0, 0)
        .workplane(offset=z_position)
        .circle(inner_diameter/2 + groove_radius)
        .circle(inner_diameter/2)
        .extrude(groove_depth)
    )
    result = result.cut(groove)