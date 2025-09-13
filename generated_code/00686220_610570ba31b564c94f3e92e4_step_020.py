import cadquery as cq

# Define dimensions
length = 100.0
width = 20.0
height = 10.0
protrusion_width = 12.0
protrusion_height = 6.0
protrusion_length = 8.0

# Create the main body
result = cq.Workplane("XY").box(length, width, height)

# Create the first end protrusion
result = (
    result.faces("<X")
    .workplane(offset=-protrusion_length/2)
    .rect(protrusion_width, protrusion_height)
    .extrude(protrusion_length)
)

# Create the second end protrusion
result = (
    result.faces(">X")
    .workplane(offset=protrusion_length/2)
    .rect(protrusion_width, protrusion_height)
    .extrude(protrusion_length)
)

# Ensure the protrusions are properly aligned and connected
# The main body has dimensions: length x width x height
# The protrusions are added at each end with dimensions: protrusion_width x protrusion_height x protrusion_length