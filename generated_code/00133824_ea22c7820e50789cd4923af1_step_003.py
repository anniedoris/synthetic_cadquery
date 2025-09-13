import cadquery as cq

# Define dimensions
block1_length = 40.0
block1_height = 10.0
block1_width = 15.0

block2_length = 35.0
block2_height = 10.0
block2_width = 15.0

# Protrusion dimensions
protrusion_width = 8.0
protrusion_height = 3.0
protrusion_depth = 5.0

# Create Block 1 (Left Block)
block1 = cq.Workplane("XY").box(block1_length, block1_height, block1_width)

# Create the protruding section on Block 1
protrusion = cq.Workplane("XY").box(protrusion_width, protrusion_height, protrusion_depth)
protrusion = protrusion.translate((block1_length/2 - protrusion_width/2, 
                                  block1_height/2 - protrusion_height/2, 
                                  -protrusion_depth/2))

# Combine block1 with protrusion
result = block1.union(protrusion)

# Create Block 2 (Right Block)
block2 = cq.Workplane("XY").box(block2_length, block2_height, block2_width)

# Create the recessed cavity on Block 2
cavity = cq.Workplane("XY").box(protrusion_width, protrusion_height, protrusion_depth)
cavity = cavity.translate((-block2_length/2 + protrusion_width/2, 
                          block2_height/2 - protrusion_height/2, 
                          -protrusion_depth/2))

# Cut the cavity from block2
block2 = block2.cut(cavity)

# Position block2 to align with block1
block2 = block2.translate((block1_length/2 - block2_length/2, 0, 0))

# Combine both blocks
result = result.union(block2)

# Ensure the top surfaces are coplanar by adjusting the positions
# Move block2 so that its top surface aligns with block1's top surface
result = result.translate((0, 0, -block1_width/2 + block2_width/2))