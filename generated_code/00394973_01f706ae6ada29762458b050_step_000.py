import cadquery as cq

# Define dimensions
triangle_base = 100.0
triangle_height = 80.0
platform_thickness = 5.0

# Create triangular base platform
base = cq.Workplane("XY").polygon(3, triangle_base).extrude(platform_thickness)

# Define building parameters
building_width = 8.0
building_length = 12.0
building_heights = [4.0, 6.0, 8.0, 10.0]
building_positions = [
    (0, 0, platform_thickness),
    (20, 0, platform_thickness),
    (-20, 0, platform_thickness),
    (0, 20, platform_thickness),
    (0, -20, platform_thickness),
    (15, 15, platform_thickness),
    (-15, 15, platform_thickness),
    (15, -15, platform_thickness),
    (-15, -15, platform_thickness),
    (0, 40, platform_thickness),
    (30, 0, platform_thickness),
    (-30, 0, platform_thickness),
    (0, -40, platform_thickness),
    (25, 25, platform_thickness),
    (-25, 25, platform_thickness),
    (25, -25, platform_thickness),
    (-25, -25, platform_thickness),
]

# Create buildings
buildings = cq.Workplane("XY")
for i, (x, y, z) in enumerate(building_positions):
    height = building_heights[i % len(building_heights)]
    building = cq.Workplane("XY", origin=(x, y, z)).rect(building_width, building_length).extrude(height)
    buildings = buildings.union(building)

# Create a more detailed building with windows and extensions
detail_building = (
    cq.Workplane("XY", origin=(0, 40, platform_thickness))
    .rect(12.0, 16.0)
    .extrude(12.0)
    .faces(">Z")
    .workplane()
    .rect(10.0, 14.0, forConstruction=True)
    .vertices()
    .hole(1.0)
    .faces(">Z")
    .workplane()
    .center(0, 6.0)
    .rect(4.0, 2.0)
    .extrude(2.0)
)

# Add some roads/paths
# Create a path from base to apex
path = (
    cq.Workplane("XY", origin=(-40, 0, platform_thickness))
    .rect(80.0, 4.0)
    .extrude(1.0)
    .faces(">Z")
    .workplane()
    .rect(4.0, 80.0)
    .extrude(1.0)
)

# Combine all elements
result = base.union(buildings).union(detail_building).union(path)

# Add some small features like trees or decorative elements
trees = cq.Workplane("XY", origin=(0, 0, platform_thickness + 12.0))
for i in range(5):
    tree = (
        cq.Workplane("XY", origin=(0, 0, platform_thickness + 12.0))
        .circle(1.0)
        .extrude(3.0)
        .faces(">Z")
        .workplane()
        .circle(2.0)
        .extrude(2.0)
    )
    trees = trees.union(tree)

result = result.union(trees)