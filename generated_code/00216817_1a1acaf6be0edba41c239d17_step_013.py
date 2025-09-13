import cadquery as cq

# Parameters
diameter = 10.0
length = 50.0
radius = diameter / 2.0

# Create the diagonal rod with rounded ends
# We'll create a cylinder with hemispherical ends
# First, create the main cylinder
result = cq.Workplane("XY").cylinder(length, radius, centered=False)

# Add hemispherical ends by creating spheres at each end
# For the bottom hemisphere
bottom_sphere = cq.Workplane("XY").translate((0, 0, -radius)).sphere(radius)

# For the top hemisphere  
top_sphere = cq.Workplane("XY").translate((0, 0, length)).sphere(radius)

# Combine the cylinder and spheres
result = result.union(bottom_sphere).union(top_sphere)

# Orient the diagonal by rotating it
# Rotate to make it diagonal (example rotation)
result = result.rotate((0, 0, 0), (1, 0, 0), 30)
result = result.rotate((0, 0, 0), (0, 1, 0), 15)

# Actually, let's create a cleaner diagonal rod using a more direct approach
# Create a rod with diagonal orientation using a more precise method

# Create the base rod with hemispherical ends
base_rod = cq.Workplane("XY").cylinder(length, radius, centered=False)

# Create the rounded ends with spheres
bottom_end = cq.Workplane("XY").translate((0, 0, 0)).sphere(radius)
top_end = cq.Workplane("XY").translate((0, 0, length)).sphere(radius)

# Combine them
result = base_rod.union(bottom_end).union(top_end)

# Orient it diagonally by transforming it
# Move it to a diagonal position
result = result.translate((0, 0, 0))

# Let's create a cleaner version with proper diagonal orientation
# Create a cylinder and then add hemispherical caps at both ends

# Create main cylindrical body
main_cylinder = cq.Workplane("XY").cylinder(length, radius, centered=False)

# Create hemispherical ends
hemisphere_bottom = cq.Workplane("XY").translate((0, 0, 0)).sphere(radius)
hemisphere_top = cq.Workplane("XY").translate((0, 0, length)).sphere(radius)

# Combine everything
result = main_cylinder.union(hemisphere_bottom).union(hemisphere_top)

# For a more precise diagonal orientation, let's create it using a different approach:
# Create the entire object at the right orientation from the start

# Create a cylinder with hemispherical ends, then orient it diagonally
# We'll use a box approach with a diagonal alignment

# Create a simple version that represents the described object
result = (
    cq.Workplane("XY")
    .cylinder(50, 5, centered=False)
    .faces("<Z")
    .workplane()
    .sphere(5)
    .faces(">Z")
    .workplane()
    .sphere(5)
)

# Apply diagonal rotation to make it appear diagonal
result = result.rotate((0, 0, 0), (1, 0, 0), 30)
result = result.rotate((0, 0, 0), (0, 1, 0), 15)

# Or use a cleaner approach with a custom orientation
# The most direct way to achieve the diagonal rod with rounded ends:

result = (
    cq.Workplane("XY")
    .cylinder(50, 5, centered=False)
    .faces("<Z")
    .workplane()
    .sphere(5)
    .faces(">Z")
    .workplane()
    .sphere(5)
    .rotate((0, 0, 0), (1, 1, 0), 30)
)