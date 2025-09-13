import cadquery as cq

# Define dimensions
body_length = 50.0
body_width = 10.0
body_height = 5.0

protruding_length = 15.0
protruding_width = 8.0
protruding_height = 5.0

# Create the main body
result = cq.Workplane("XY").box(body_length, body_width, body_height)

# Add the protruding section at one end
# Move to the end of the body and create the protruding section
result = (
    result.faces(">X")
    .workplane(offset=body_height/2)
    .rect(protruding_length, protruding_width)
    .extrude(protruding_height)
)

# The protruding section is already positioned correctly with a right-angle connection
# The small flat surface on the protruding section is naturally created by the extrusion
# that's parallel to the main body's surface

# Ensure the protruding section is properly aligned
result = (
    result.faces(">X")
    .workplane(offset=body_height/2)
    .rect(protruding_length, protruding_width)
    .extrude(protruding_height)
)