import cadquery as cq

# Define dimensions for each layer
base_length = 40.0
base_width = 30.0
base_height = 5.0

layer2_length = 30.0
layer2_width = 22.0
layer2_height = 5.0

layer3_length = 20.0
layer3_width = 14.0
layer3_height = 5.0

layer4_length = 10.0
layer4_width = 6.0
layer4_height = 5.0

# Create the base layer
result = cq.Workplane("XY").box(base_length, base_width, base_height)

# Add second layer, offset from center
result = (
    result.faces(">Z")
    .workplane(offset=base_height)
    .center(-(base_length - layer2_length)/2, -(base_width - layer2_width)/2)
    .box(layer2_length, layer2_width, layer2_height)
)

# Add third layer, offset from center
result = (
    result.faces(">Z")
    .workplane(offset=layer2_height)
    .center(-(layer2_length - layer3_length)/2, -(layer2_width - layer3_width)/2)
    .box(layer3_length, layer3_width, layer3_height)
)

# Add fourth layer, offset from center
result = (
    result.faces(">Z")
    .workplane(offset=layer3_height)
    .center(-(layer3_length - layer4_length)/2, -(layer3_width - layer4_width)/2)
    .box(layer4_length, layer4_width, layer4_height)
)

# Add L-shaped notch on the side of the base layer
# The notch is located near bottom right corner
notch_depth = 3.0
notch_height = 2.0
notch_width = 4.0

# Cut out the L-shaped notch
result = (
    result.faces("<Y")  # Select the back face (assuming Y is the width dimension)
    .workplane(offset=-base_height)
    .center(base_length/2 - notch_depth/2, -base_width/2 + notch_width/2)
    .rect(notch_depth, notch_width)
    .cutBlind(-notch_height)
)

# Alternative approach for the L-shaped notch - cutting from the side
# Create the L-shape by cutting two rectangles
result = (
    result.faces(">X")  # Select the right face
    .workplane(offset=-base_height)
    .center(-base_length/2 + notch_depth/2, base_width/2 - notch_width/2)
    .rect(notch_depth, notch_width)
    .cutBlind(-notch_height)
)

# Final result
result = result