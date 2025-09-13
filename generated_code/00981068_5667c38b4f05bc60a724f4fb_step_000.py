import cadquery as cq

# Define dimensions
beam_width = 2.0
beam_height = 2.0
beam_length = 10.0
corner_length = 4.0
support_length = 3.0
support_width = 2.0

# Create the main framework
# Start with the bottom horizontal beam
result = cq.Workplane("XY").box(beam_length, beam_width, beam_height)

# Add the top horizontal beam
result = result.faces(">Z").workplane().box(beam_length, beam_width, beam_height)

# Add the vertical beams
# Left vertical beam
result = result.faces("<X").workplane().box(beam_width, beam_height, beam_length)
# Right vertical beam
result = result.faces(">X").workplane().box(beam_width, beam_height, beam_length)

# Add the L-shaped corner piece at the end
# Vertical leg of L-shape
result = result.faces(">Y").workplane(offset=beam_length).box(beam_width, beam_height, corner_length)
# Horizontal leg of L-shape
result = result.faces(">Z").workplane(offset=beam_height).box(corner_length, beam_width, beam_height)

# Add supporting beams at the end
# Horizontal supporting beam
result = result.faces(">Y").workplane(offset=beam_length).box(support_length, beam_width, beam_height)
# Vertical supporting beam
result = result.faces(">Z").workplane(offset=beam_height).box(beam_width, support_width, beam_height)

# Add another horizontal supporting beam
result = result.faces(">Z").workplane(offset=beam_height).box(support_length, beam_width, beam_height)

result = result