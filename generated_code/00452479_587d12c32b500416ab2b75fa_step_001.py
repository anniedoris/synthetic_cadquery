import cadquery as cq

# Dimensions
block_length = 80.0
block_width = 40.0
block_height = 10.0

base_length = 60.0
base_width = 40.0
base_height = 8.0

pivot_diameter = 6.0
pivot_offset = 10.0

arm_width = 8.0
arm_height = 12.0
arm_length = 20.0

# Create the base plate
base = cq.Workplane("XY").box(base_length, base_width, base_height)

# Add holes to the base plate
hole_positions = [
    (-20, 0),
    (-10, 0),
    (0, 0),
    (10, 0),
    (20, 0)
]

for pos in hole_positions:
    base = base.workplane(offset=base_height).center(pos[0], pos[1]).circle(2.0).cutThruAll()

# Create the central pivot
pivot = cq.Workplane("XY").center(0, 0).circle(pivot_diameter/2).extrude(base_height + 2)

# Create the connecting arms
arm1 = cq.Workplane("XY").center(-base_length/2 + arm_length/2, 0).rect(arm_length, arm_width).extrude(arm_height)
arm2 = cq.Workplane("XY").center(base_length/2 - arm_length/2, 0).rect(arm_length, arm_width).extrude(arm_height)

# Create the rectangular block
block = cq.Workplane("XY").box(block_length, block_width, block_height)

# Create the pivot hole in the block
block_pivot_hole = cq.Workplane("XY").center(0, 0).circle(pivot_diameter/2).extrude(block_height + 2)

# Position components
result = base.union(pivot).union(arm1).union(arm2).union(block).union(block_pivot_hole)

# Position the block to align with the hinge
result = result.translate((0, 0, base_height))

# Position the arms to connect to the base plate
result = result.translate((0, 0, 0))

# Position the pivot correctly
result = result.translate((0, 0, base_height/2))

# Move block to align with pivot
result = result.translate((0, 0, 0))