import cadquery as cq

# Define dimensions
sphere_radius = 10.0
block_length = 15.0
block_width = 8.0
block_height = 6.0
hex_radius = 5.0
hex_height = 3.0
transition_radius = 2.0

# Create the spherical element
sphere = cq.Workplane("XY").sphere(sphere_radius)

# Create the rectangular block
block = cq.Workplane("XY").box(block_length, block_width, block_height)

# Position the block to connect with the sphere
# The block should be positioned so that one face connects to the sphere
# We'll place the block along the positive Y axis from the sphere center
block = block.translate((0, sphere_radius + block_height/2, 0))

# Create a smooth transition between sphere and block
# This is a simple approach - we'll use a fillet on the connection
# First, we need to make sure the sphere and block intersect properly
# We'll create the transition using a combination of operations

# Create the main assembly by combining sphere and block
# Start with the sphere
result = sphere

# Add the block
result = result.union(block)

# Create the hexagonal component (nut)
hexagon = cq.Workplane("XY").polygon(6, hex_radius * 2).extrude(hex_height)

# Position the hexagon on the top face of the block
hexagon = hexagon.translate((0, 0, block_height/2 + hex_height/2))

# Add the hexagon to the assembly
result = result.union(hexagon)

# Apply a fillet to the transition between sphere and block for smoothness
# We need to identify the edges where sphere and block meet
# This is a simplified approach - we'll fillet the edges where they connect
result = result.edges("|Z").fillet(transition_radius)

# Let's refine the model with a more precise approach:
# Create a clean base model
result = cq.Workplane("XY").sphere(sphere_radius)

# Create the connecting block
block = cq.Workplane("XY").box(block_length, block_width, block_height)

# Position block so it connects to the sphere (with proper overlap)
# The block is positioned with its center aligned with the sphere's center
# and extended in the positive Y direction
block = block.translate((0, sphere_radius + block_height/2, 0))

# Union the sphere and block
result = result.union(block)

# Create hexagonal nut
hex_nut = cq.Workplane("XY").polygon(6, hex_radius * 2).extrude(hex_height)

# Position hex nut on the top of the block
hex_nut = hex_nut.translate((0, 0, block_height/2 + hex_height/2))

# Union the hex nut
result = result.union(hex_nut)

# Apply fillet to the transition area
# We need to identify the edges properly - the connection edge between sphere and block
# For a better transition, let's create a more accurate connection
result = result.edges("|Y").fillet(transition_radius)