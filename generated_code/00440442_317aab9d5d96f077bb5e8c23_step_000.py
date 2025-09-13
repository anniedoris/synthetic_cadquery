import cadquery as cq

# Define dimensions
length = 100.0
width = 20.0
height = 10.0
slot_width = 8.0
slot_height = 6.0
protrusion_width = 4.0
protrusion_height = 4.0
notch_width = 6.0
notch_height = 3.0
corner_radius = 2.0
indentation_width = 8.0
indentation_depth = 1.0

# Create the base rectangular prism with rounded corners
result = cq.Workplane("XY").box(length, width, height).edges("|Z").fillet(corner_radius)

# Create the central rectangular slot
result = (
    result.faces(">Z")
    .workplane(offset=-height/2 + slot_height/2)
    .rect(slot_width, slot_height, forConstruction=True)
    .vertices()
    .hole(slot_width, slot_height)
)

# Add the protrusion at one end
result = (
    result.faces("<X")
    .workplane(offset=-slot_height/2)
    .rect(protrusion_width, protrusion_height, forConstruction=True)
    .vertices()
    .hole(protrusion_width, protrusion_height)
)

# Add the notch at the opposite end
result = (
    result.faces(">X")
    .workplane(offset=slot_height/2)
    .rect(notch_width, notch_height, forConstruction=True)
    .vertices()
    .hole(notch_width, notch_height)
)

# Add the indentation on the top surface
result = (
    result.faces(">Z")
    .workplane(offset=-height/2 + indentation_depth/2)
    .rect(indentation_width, indentation_depth, forConstruction=True)
    .vertices()
    .hole(indentation_width, indentation_depth)
)

# Final result
result = result