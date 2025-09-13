import cadquery as cq

# Define dimensions
beam_width = 20.0
beam_thickness = 5.0
beam_height = 50.0
sphere_diameter = 30.0
horizontal_beam_length = 100.0

# Create the two vertical beams
# Left vertical beam
left_beam = cq.Workplane("XY").box(beam_width, beam_thickness, beam_height)

# Right vertical beam positioned to the right
right_beam = cq.Workplane("XY").translate((horizontal_beam_length - beam_width, 0, 0)).box(beam_width, beam_thickness, beam_height)

# Create the horizontal beam connecting the tops of vertical beams
# The horizontal beam should be centered between the vertical beams
horizontal_beam = (
    cq.Workplane("XY")
    .translate(((horizontal_beam_length - beam_width) / 2, 0, beam_height))
    .box(beam_width, beam_thickness, beam_height)
)

# Create the sphere
sphere = (
    cq.Workplane("XY")
    .translate(((horizontal_beam_length - beam_width) / 2 + beam_width / 2, 0, beam_height + sphere_diameter / 2))
    .sphere(sphere_diameter / 2)
)

# Combine all parts
result = left_beam.union(right_beam).union(horizontal_beam).union(sphere)