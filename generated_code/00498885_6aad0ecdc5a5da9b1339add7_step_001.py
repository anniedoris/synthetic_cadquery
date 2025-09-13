import cadquery as cq

# Define dimensions
length = 100.0
width = 60.0
height = 40.0
wall_thickness = 5.0

# Create the base
base = cq.Workplane("XY").box(length, width, wall_thickness)

# Create the four walls
# Front wall
front_wall = cq.Workplane("XY").box(length, wall_thickness, height).translate((0, width/2 - wall_thickness/2, wall_thickness/2 + height/2))

# Back wall
back_wall = cq.Workplane("XY").box(length, wall_thickness, height).translate((0, -width/2 + wall_thickness/2, wall_thickness/2 + height/2))

# Left wall
left_wall = cq.Workplane("XY").box(wall_thickness, width, height).translate((length/2 - wall_thickness/2, 0, wall_thickness/2 + height/2))

# Right wall
right_wall = cq.Workplane("XY").box(wall_thickness, width, height).translate((-length/2 + wall_thickness/2, 0, wall_thickness/2 + height/2))

# Combine all parts
result = base.union(front_wall).union(back_wall).union(left_wall).union(right_wall)