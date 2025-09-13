import cadquery as cq

# Define dimensions
base_length = 100.0
base_width = 60.0
height = 80.0
vertical_diameter = 8.0
beam_width = 6.0
beam_height = 4.0
brace_width = 4.0
brace_height = 3.0
cross_beam_width = 3.0
cross_beam_height = 2.0

# Create base plate
result = cq.Workplane("XY").box(base_length, base_width, beam_height)

# Add vertical supports at each corner
vertical_positions = [
    (-base_length/2 + vertical_diameter, -base_width/2 + vertical_diameter),
    (base_length/2 - vertical_diameter, -base_width/2 + vertical_diameter),
    (-base_length/2 + vertical_diameter, base_width/2 - vertical_diameter),
    (base_length/2 - vertical_diameter, base_width/2 - vertical_diameter)
]

for x, y in vertical_positions:
    result = result.workplane(offset=beam_height).center(x, y).circle(vertical_diameter/2).extrude(height - beam_height)

# Add top horizontal beam (wider than bottom)
top_beam_offset = height - beam_height
result = (
    result.faces(">Z")
    .workplane(offset=top_beam_offset)
    .rect(base_length - 2*vertical_diameter, base_width - 2*vertical_diameter, forConstruction=True)
    .vertices()
    .circle(beam_width/2)
    .extrude(beam_height)
)

# Add diagonal braces on all sides
# Top diagonal braces
result = (
    result.faces(">Z")
    .workplane(offset=top_beam_offset)
    .rect(base_length - 2*vertical_diameter, base_width - 2*vertical_diameter, forConstruction=True)
    .vertices()
    .circle(brace_width/2)
    .extrude(brace_height)
)

# Add cross beams
# Vertical cross beams
cross_beam_positions = [
    (-base_length/4, 0),
    (base_length/4, 0),
    (0, -base_width/4),
    (0, base_width/4)
]

for x, y in cross_beam_positions:
    result = (
        result.faces(">Z")
        .workplane(offset=beam_height + (height - 2*beam_height)/2)
        .center(x, y)
        .rect(cross_beam_width, cross_beam_height)
        .extrude(beam_height)
    )

# Add additional diagonal braces connecting vertical supports to cross beams
# Bottom to cross beams
for x, y in cross_beam_positions:
    result = (
        result.faces("<Z")
        .workplane(offset=0)
        .center(x, y)
        .rect(brace_width, brace_height)
        .extrude(beam_height)
    )

# Add cross beams connecting vertical supports
# Horizontal cross beams
result = (
    result.faces(">Z")
    .workplane(offset=beam_height + (height - 2*beam_height)/2)
    .rect(base_length - 2*vertical_diameter, base_width - 2*vertical_diameter, forConstruction=True)
    .vertices()
    .circle(cross_beam_width/2)
    .extrude(cross_beam_height)
)

# Add top platform support structure
result = (
    result.faces(">Z")
    .workplane(offset=top_beam_offset)
    .rect(base_length - 2*vertical_diameter, base_width - 2*vertical_diameter, forConstruction=True)
    .vertices()
    .circle(brace_width/2)
    .extrude(brace_height)
)

# Add middle cross beam structure
result = (
    result.faces(">Z")
    .workplane(offset=beam_height + (height - 2*beam_height)/2)
    .rect(base_length - 2*vertical_diameter, base_width - 2*vertical_diameter, forConstruction=True)
    .vertices()
    .circle(cross_beam_width/2)
    .extrude(cross_beam_height)
)

# Final structure
result = result