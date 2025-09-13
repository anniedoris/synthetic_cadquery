import cadquery as cq

# Define dimensions
main_length = 40.0
main_width = 20.0
main_height = 10.0

protrusion_length = 15.0
protrusion_width = 10.0
protrusion_height = 5.0
protrusion_offset = 5.0

# Create the main body
result = cq.Workplane("XY").box(main_length, main_width, main_height)

# Create the protruding section
protrusion = (
    cq.Workplane("XY")
    .box(protrusion_length, protrusion_width, protrusion_height)
    .translate((main_length/2 - protrusion_length/2 - protrusion_offset, 0, main_height))
)

# Combine the main body and protruding section
result = result.union(protrusion)