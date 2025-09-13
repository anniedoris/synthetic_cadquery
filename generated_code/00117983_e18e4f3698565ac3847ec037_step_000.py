import cadquery as cq

# Define dimensions for the smaller block
small_width = 2.0
small_depth = 2.0
small_height = 4.0

# Define dimensions for the larger block
large_width = 2.0
large_depth = 2.0
large_height = 8.0

# Create the smaller block (vertical orientation)
small_block = cq.Workplane("XY").box(small_width, small_depth, small_height)

# Create the larger block (horizontal orientation, diagonal)
# We'll position it diagonally by rotating and translating
large_block = (
    cq.Workplane("XY")
    .box(large_width, large_depth, large_height)
    .rotate((0, 0, 0), (0, 0, 1), 30)  # Rotate 30 degrees for diagonal orientation
    .translate((2, 2, 0))  # Position it diagonally
)

# Combine both blocks
result = small_block.union(large_block)