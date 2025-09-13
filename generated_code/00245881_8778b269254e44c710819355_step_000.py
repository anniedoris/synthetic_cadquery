import cadquery as cq

# Define dimensions
block1_width, block1_height, block1_depth = 40, 20, 10
block2_width, block2_height, block2_depth = 20, 30, 10
block3_width, block3_height, block3_depth = 60, 20, 10
block4_width, block4_height, block4_depth = 30, 20, 10
hole_diameter = 8

# Create Block 1 (top-left)
block1 = cq.Workplane("XY").box(block1_width, block1_height, block1_depth)

# Add circular cutout to Block 1
block1 = (
    block1.faces(">Z")
    .workplane()
    .circle(hole_diameter/2)
    .cutThruAll()
)

# Create Block 2 (connector between Block 1 and Block 3)
block2 = cq.Workplane("XY").box(block2_width, block2_height, block2_depth)

# Position Block 2 below and to the right of Block 1
block2 = block2.translate((block1_width/2 - block2_width/2, -block1_height/2, 0))

# Create Block 3 (center-bottom)
block3 = cq.Workplane("XY").box(block3_width, block3_height, block3_depth)

# Add circular cutout to Block 3
block3 = (
    block3.faces(">Z")
    .workplane()
    .circle(hole_diameter/2)
    .cutThruAll()
)

# Position Block 3 below Block 2
block3 = block3.translate((0, -block2_height/2 - block3_height/2, 0))

# Create Block 4 (right of Block 3)
block4 = cq.Workplane("XY").box(block4_width, block4_height, block4_depth)

# Add circular cutout to Block 4
block4 = (
    block4.faces(">Z")
    .workplane()
    .circle(hole_diameter/2)
    .cutThruAll()
)

# Position Block 4 to the right of Block 3
block4 = block4.translate((block3_width/2 + block4_width/2, 0, 0))

# Combine all blocks
result = block1.union(block2).union(block3).union(block4)