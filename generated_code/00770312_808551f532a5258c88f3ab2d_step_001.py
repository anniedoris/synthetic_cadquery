import cadquery as cq

# Define dimensions
platform_length = 200.0
platform_width = 100.0
platform_thickness = 10.0

# Upright structure dimensions
upright_width = 15.0
upright_depth = 15.0

# Heights for the 5 upright structures (front to back, increasing height)
upright_heights = [30.0, 30.0, 50.0, 60.0, 70.0]

# Create the platform base
result = cq.Workplane("XY").box(platform_length, platform_width, platform_thickness)

# Define positions for the upright structures
# Positions are (x, y) relative to the center of the platform
positions = [
    (-60.0, -25.0),  # Front left
    (0.0, -25.0),    # Front center
    (60.0, -25.0),   # Front right
    (-30.0, 25.0),   # Back left
    (30.0, 25.0),    # Back right
]

# Add the upright structures
for i, (x, y) in enumerate(positions):
    height = upright_heights[i]
    result = (
        result.workplane(offset=platform_thickness)
        .center(x, y)
        .box(upright_width, upright_depth, height)
    )

# Ensure the result is properly defined
result = result.val()