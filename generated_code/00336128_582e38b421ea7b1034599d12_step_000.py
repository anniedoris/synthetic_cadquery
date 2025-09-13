import cadquery as cq

# Define dimensions
shaft_diameter = 2.0
shaft_length = 20.0
cap_width = 1.0
cap_thickness = 0.3
bottom_h_width = 1.5
bottom_h_thickness = 0.3
bottom_v_height = 1.0
bottom_v_thickness = 0.3

# Create the main shaft
result = cq.Workplane("XY").circle(shaft_diameter/2).extrude(shaft_length)

# Add the top cap
result = (
    result.faces(">Z")
    .workplane()
    .rect(cap_width, cap_thickness)
    .extrude(cap_thickness)
)

# Add the bottom feature (L-shape)
result = (
    result.faces("<Z")
    .workplane(offset=-0.5)
    .rect(bottom_h_width, bottom_h_thickness)
    .extrude(bottom_h_thickness)
    .faces("<Y")
    .workplane()
    .rect(bottom_v_thickness, bottom_v_height)
    .extrude(bottom_v_height)
)

# Ensure the bottom feature is properly connected to the shaft
result = (
    result.faces("<Z")
    .workplane(offset=-bottom_v_height)
    .rect(bottom_v_thickness, bottom_h_width)
    .extrude(bottom_v_height)
)