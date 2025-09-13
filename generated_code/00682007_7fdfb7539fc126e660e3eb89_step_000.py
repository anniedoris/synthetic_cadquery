import cadquery as cq

# Define dimensions
base_width = 40.0
base_length = 60.0
base_thickness = 10.0

intermediate_length = 40.0
intermediate_thickness = 10.0

vertical_height = 80.0
vertical_thickness = 10.0

# Create the base section
result = cq.Workplane("XY").box(base_width, base_length, base_thickness)

# Create the intermediate section (step/ledge)
# Position it to connect base and vertical sections
intermediate_offset = (base_length - intermediate_length) / 2
result = (
    result
    .faces(">Z")
    .workplane(offset=base_thickness)
    .center(0, intermediate_offset)
    .box(base_width, intermediate_length, intermediate_thickness)
)

# Create the vertical section
# Position it to rise from one end of the base
result = (
    result
    .faces(">Z")
    .workplane(offset=base_thickness + intermediate_thickness)
    .center(0, base_length/2)
    .box(base_width, vertical_thickness, vertical_height)
)

# The result should be an L-shaped structure with three sections