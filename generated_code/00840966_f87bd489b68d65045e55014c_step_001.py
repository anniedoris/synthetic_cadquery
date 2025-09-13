import cadquery as cq

# Create a cylinder and rotate it to get the diagonal orientation
# Using a cylinder with radius 5 and height 10
cylinder = cq.Workplane("XY").cylinder(10, 5, centered=False)

# Rotate the cylinder to give it a diagonal orientation
# Rotate 30 degrees around the X-axis to tilt it
cylinder = cylinder.rotate((0, 0, 0), (1, 0, 0), 30)

# Create a cutting plane that intersects the cylinder at an angle
# This plane will cut through the cylinder creating a flat edge
# We'll use a workplane at an angle to cut the cylinder
cutting_plane = cq.Workplane("XY").workplane(offset=2).transformed(
    rotate=cq.Vector(0, 30, 0)
)

# Cut the cylinder with the angled plane
# We'll cut with a rectangular section to create the flat edge
result = cylinder.cut(cutting_plane.rect(15, 15).extrude(15))

# Alternative approach - create a more precise cut
# Create the base cylinder
base_cylinder = cq.Workplane("XY").cylinder(10, 5, centered=False)

# Rotate it for diagonal orientation
rotated_cylinder = base_cylinder.rotate((0, 0, 0), (1, 0, 0), 30)

# Create a cutting plane that intersects at an angle
# We'll create a plane that cuts through the cylinder
cutting_workplane = cq.Workplane("XY").transformed(
    offset=cq.Vector(0, 0, 2),
    rotate=cq.Vector(30, 0, 0)
)

# Create the cutting shape (a rectangular section) and extrude it
cutting_shape = cutting_workplane.rect(12, 12).extrude(15)

# Cut the cylinder with the plane
result = rotated_cylinder.cut(cutting_shape)

# Even better approach - create a more realistic cylinder segment
# Create a cylinder with proper orientation
cylinder = cq.Workplane("XY").cylinder(10, 5, centered=False)

# Rotate to get diagonal orientation
cylinder = cylinder.rotate((0, 0, 0), (1, 0, 0), 30)

# Create the cut plane that intersects at an angle
# We'll create a plane that cuts through the cylinder
cut_plane = cq.Workplane("XY").transformed(
    offset=cq.Vector(0, 0, 2),
    rotate=cq.Vector(45, 0, 0)
)

# Create a rectangular cutting section and extrude it
cut_section = cut_plane.rect(10, 10).extrude(12)

# Perform the cut
result = cylinder.cut(cut_section)

# Even simpler approach - let's just make a proper cylinder segment
# Create a cylinder
result = cq.Workplane("XY").cylinder(10, 5, centered=False)

# Rotate it to get the diagonal orientation
result = result.rotate((0, 0, 0), (1, 0, 0), 30)

# Create a plane that intersects the cylinder at an angle
# Cut with a rectangular solid to create the flat edge
cutting_plane = cq.Workplane("XY").transformed(
    offset=cq.Vector(0, 0, 3),
    rotate=cq.Vector(45, 0, 0)
)

# Create a rectangular cutting section that extends beyond the cylinder
cutting_section = cutting_plane.rect(15, 15).extrude(15)

# Cut the cylinder
result = result.cut(cutting_section)