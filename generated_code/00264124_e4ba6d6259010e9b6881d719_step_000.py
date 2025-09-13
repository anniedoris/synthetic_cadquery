import cadquery as cq

# Parameters for the pipe bundle
pipe_diameter = 4.0
pipe_radius = pipe_diameter / 2.0
pipe_length = 100.0
pipe_count = 12
row_count = 4
spacing_x = pipe_diameter * 1.5  # Horizontal spacing between pipes
spacing_y = pipe_diameter * 1.2  # Vertical spacing between rows
offset = spacing_x / 2.0  # Offset for staggered arrangement

# Create the pipe bundle
result = cq.Workplane("XY")

# Create pipes in a staggered arrangement
for row in range(row_count):
    y_offset = row * spacing_y
    x_offset = (row % 2) * offset  # Offset every other row
    
    for i in range(pipe_count):
        x_pos = i * spacing_x + x_offset
        # Create a cylinder for each pipe
        pipe = cq.Workplane("XY").translate((x_pos, y_offset, 0)).circle(pipe_radius).extrude(pipe_length)
        result = result.union(pipe)

# Ensure the result is properly formed
result = result.val().fix()