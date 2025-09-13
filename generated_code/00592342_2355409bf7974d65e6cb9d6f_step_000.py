import cadquery as cq

# Define dimensions
base_width = 100.0
base_depth = 50.0
platform_height = 10.0
platform_thickness = 5.0
vertical_section_height = 30.0
vertical_section_width = 30.0

# Create the base platform
result = cq.Workplane("XY").box(base_width, base_depth, platform_thickness)

# Add second platform (narrower)
second_platform_width = base_width - 20.0
second_platform_depth = base_depth - 10.0
result = (
    result
    .translate((0, 0, platform_height))
    .box(second_platform_width, second_platform_depth, platform_thickness)
)

# Add third platform (narrowest)
third_platform_width = base_width - 40.0
third_platform_depth = base_depth - 20.0
result = (
    result
    .translate((0, 0, platform_height))
    .box(third_platform_width, third_platform_depth, platform_thickness)
)

# Add vertical section to create L-shape
result = (
    result
    .translate((0, base_depth, 0))
    .box(vertical_section_width, vertical_section_height, platform_thickness)
)

# Ensure sharp edges by filleting (if needed, but description suggests sharp edges)
# Since the problem asks for sharp edges, I'll leave them as is