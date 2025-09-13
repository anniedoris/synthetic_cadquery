import cadquery as cq

# Dimensions
platform_length = 100.0
platform_width = 60.0
platform_height = 10.0
leg_height = 20.0
ramp_length = 80.0
ramp_width = platform_width
ramp_height = 10.0
step_height = 5.0
step_depth = 8.0
num_steps = 4
stair_width = platform_width
stair_length = num_steps * step_depth

# Create the platform
platform = cq.Workplane("XY").box(platform_length, platform_width, platform_height)

# Add slats to the platform top
slat_width = 2.0
slat_height = 0.5
num_slats = int(platform_length / slat_width) + 1
for i in range(num_slats):
    slat = cq.Workplane("XY", origin=(i * slat_width - platform_length/2, 0, platform_height)).box(slat_width, platform_width, slat_height)
    platform = platform.union(slat)

# Create legs
leg_offset = 10.0
leg_positions = [
    (-platform_length/2 + leg_offset, -platform_width/2 + leg_offset),
    (platform_length/2 - leg_offset, -platform_width/2 + leg_offset),
    (-platform_length/2 + leg_offset, platform_width/2 - leg_offset),
    (platform_length/2 - leg_offset, platform_width/2 - leg_offset)
]

for x, y in leg_positions:
    leg = cq.Workplane("XY", origin=(x, y, 0)).box(5, 5, leg_height)
    platform = platform.union(leg)

# Create the ramp
ramp_base = cq.Workplane("XY", origin=(platform_length/2, 0, platform_height)).box(ramp_length, ramp_width, ramp_height)
ramp = cq.Workplane("XY", origin=(platform_length/2, 0, platform_height)).box(ramp_length, ramp_width, ramp_height)

# Create the stairs
stairs = cq.Workplane("XY", origin=(platform_length/2 + ramp_length, 0, platform_height)).box(stair_length, stair_width, step_height * num_steps)

# Add steps to the stairs
for i in range(num_steps):
    step = cq.Workplane("XY", origin=(platform_length/2 + ramp_length + i*step_depth, 0, platform_height + i*step_height)).box(step_depth, stair_width, step_height)
    
    # Add tread pattern to each step
    pattern_width = 2.0
    pattern_height = 0.3
    num_patterns = int(step_depth / pattern_width) + 1
    for j in range(num_patterns):
        pattern = cq.Workplane("XY", origin=(platform_length/2 + ramp_length + i*step_depth + j*pattern_width - step_depth/2, 0, platform_height + i*step_height)).box(pattern_width, stair_width, pattern_height)
        step = step.union(pattern)
    
    stairs = stairs.union(step)

# Connect the ramp and stairs
combined = platform.union(ramp).union(stairs)

# Add a safety lip to the ramp edge
lip_height = 1.0
lip = cq.Workplane("XY", origin=(platform_length/2 + ramp_length/2, 0, platform_height)).box(5, ramp_width, lip_height)
combined = combined.union(lip)

result = combined