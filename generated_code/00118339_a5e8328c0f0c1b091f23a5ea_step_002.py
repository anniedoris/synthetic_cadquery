import cadquery as cq

# Define dimensions
base_length = 100.0
base_width = 60.0
base_thickness = 5.0

# Vertical block dimensions
vblock_width = 8.0
vblock_depth = 8.0
vblock_heights = [20.0, 18.0, 16.0, 14.0, 12.0, 10.0, 8.0, 6.0]  # Decreasing heights
vblock_spacing = 12.0

# L-shaped block dimensions
lblock_width = 10.0
lblock_depth = 10.0
lblock_height = 15.0

# Connecting element dimensions
conn_width = 6.0
conn_depth = 6.0
conn_height = 5.0

# Create base platform
result = cq.Workplane("XY").box(base_length, base_width, base_thickness)

# Add vertical blocks with decreasing heights
for i, height in enumerate(vblock_heights):
    x_pos = -base_length/2 + vblock_width/2 + i * vblock_spacing
    result = (
        result.workplane(offset=base_thickness)
        .center(x_pos, 0)
        .box(vblock_width, vblock_depth, height)
    )

# Add L-shaped blocks around the perimeter
# Top L-shaped blocks
result = (
    result.workplane(offset=base_thickness)
    .center(-base_length/2 + lblock_width/2, base_width/2 - lblock_depth/2)
    .box(lblock_width, lblock_depth, lblock_height)
)
result = (
    result.workplane(offset=base_thickness)
    .center(base_length/2 - lblock_width/2, base_width/2 - lblock_depth/2)
    .box(lblock_width, lblock_depth, lblock_height)
)

# Bottom L-shaped blocks
result = (
    result.workplane(offset=base_thickness)
    .center(-base_length/2 + lblock_width/2, -base_width/2 + lblock_depth/2)
    .box(lblock_width, lblock_depth, lblock_height)
)
result = (
    result.workplane(offset=base_thickness)
    .center(base_length/2 - lblock_width/2, -base_width/2 + lblock_depth/2)
    .box(lblock_width, lblock_depth, lblock_height)
)

# Side L-shaped blocks
result = (
    result.workplane(offset=base_thickness)
    .center(-base_length/2 + lblock_width/2, 0)
    .box(lblock_width, lblock_depth, lblock_height)
)
result = (
    result.workplane(offset=base_thickness)
    .center(base_length/2 - lblock_width/2, 0)
    .box(lblock_width, lblock_depth, lblock_height)
)

# Add connecting elements between vertical blocks and L-shaped blocks
# Connect leftmost vertical block to left L-shaped block
result = (
    result.workplane(offset=base_thickness)
    .center(-base_length/2 + vblock_width/2, base_width/2 - lblock_depth/2)
    .box(conn_width, conn_depth, conn_height)
)

# Connect rightmost vertical block to right L-shaped block
result = (
    result.workplane(offset=base_thickness)
    .center(base_length/2 - vblock_width/2, base_width/2 - lblock_depth/2)
    .box(conn_width, conn_depth, conn_height)
)

# Connect leftmost vertical block to left L-shaped block (bottom)
result = (
    result.workplane(offset=base_thickness)
    .center(-base_length/2 + vblock_width/2, -base_width/2 + lblock_depth/2)
    .box(conn_width, conn_depth, conn_height)
)

# Connect rightmost vertical block to right L-shaped block (bottom)
result = (
    result.workplane(offset=base_thickness)
    .center(base_length/2 - vblock_width/2, -base_width/2 + lblock_depth/2)
    .box(conn_width, conn_depth, conn_height)
)

# Add corner reinforcement L-shaped blocks
# Top-left corner
result = (
    result.workplane(offset=base_thickness)
    .center(-base_length/2 + lblock_width/2, base_width/2 - lblock_depth/2)
    .box(lblock_width, lblock_depth, lblock_height)
)

# Top-right corner
result = (
    result.workplane(offset=base_thickness)
    .center(base_length/2 - lblock_width/2, base_width/2 - lblock_depth/2)
    .box(lblock_width, lblock_depth, lblock_height)
)

# Bottom-left corner
result = (
    result.workplane(offset=base_thickness)
    .center(-base_length/2 + lblock_width/2, -base_width/2 + lblock_depth/2)
    .box(lblock_width, lblock_depth, lblock_height)
)

# Bottom-right corner
result = (
    result.workplane(offset=base_thickness)
    .center(base_length/2 - lblock_width/2, -base_width/2 + lblock_depth/2)
    .box(lblock_width, lblock_depth, lblock_height)
)