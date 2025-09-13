import cadquery as cq

# Create the base cube
cube_size = 10.0
result = cq.Workplane("XY").box(cube_size, cube_size, cube_size)

# Create a pentagonal cavity centered in the cube
# The pentagon will be centered at the top face and extend down
pentagon_radius = 3.0  # Adjust this to control the size of the pentagon

# Create the pentagon cavity profile
cavity_profile = (
    cq.Workplane("XY")
    .polygon(5, pentagon_radius)  # 5 sides, radius 3.0
    .workplane(offset=8)  # Move up to create the cavity
    .polygon(5, pentagon_radius)
    .loft(combine=True)
)

# Cut the pentagonal cavity from the cube
# We'll cut a solid pentagonal prism that goes from top to near bottom
result = (
    result.faces(">Z")
    .workplane()
    .polygon(5, pentagon_radius)
    .extrude(-8)  # Extrude down to create the cavity
)

# Alternative approach - more precise
result = cq.Workplane("XY").box(cube_size, cube_size, cube_size)

# Create the internal pentagonal cavity by cutting a pentagonal prism
# from the top face down to near the bottom
result = (
    result.faces(">Z")
    .workplane()
    .polygon(5, pentagon_radius)
    .extrude(-8)  # This creates the cavity from top face down 8 units
)

# Or we can do it in a more explicit way:
# Create the main cube
result = cq.Workplane("XY").box(10, 10, 10)

# Create a pentagonal cavity that goes from the top down
# We'll use the polygon method to create a 5-sided polygon and extrude it
result = (
    result.faces(">Z")
    .workplane()
    .polygon(5, 3.0)  # 5 sides, radius of 3.0
    .extrude(-8)  # Extrude 8 units down (from top face to near bottom)
)