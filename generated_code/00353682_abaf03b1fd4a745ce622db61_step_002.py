import cadquery as cq

# Define dimensions
main_length = 100.0
main_width = 30.0
main_height = 10.0

protrusion_length = 40.0
protrusion_width = 20.0
protrusion_height = 15.0

cutout_width = 10.0
cutout_height = 5.0
cutout_depth = 5.0

notch_width = 8.0
notch_height = 3.0
notch_depth = 3.0

# Create main body
result = cq.Workplane("XY").box(main_length, main_width, main_height)

# Add protrusions
# Position protrusions towards the back, offset from center
protrusion_offset = (main_length - protrusion_length) / 2 - 10.0

result = (
    result.faces(">Z")
    .workplane()
    .transformed(offset=cq.Vector(protrusion_offset, 0, 0))
    .box(protrusion_length, protrusion_width, protrusion_height)
    .transformed(offset=cq.Vector(0, 0, protrusion_height))
    .box(protrusion_length, protrusion_width, protrusion_height)
)

# Add cutout on main body (side, near bottom)
result = (
    result.faces(">Y")
    .workplane(offset=-cutout_depth/2)
    .transformed(offset=cq.Vector(0, -main_width/2 + cutout_width/2, -main_height/2 + cutout_height/2))
    .rect(cutout_width, cutout_height)
    .cutBlind(-cutout_depth)
)

# Add notches on protrusions
# Notches at the back end of each protrusion
notch_offset = protrusion_length - notch_depth

result = (
    result.faces(">Z")
    .workplane()
    .transformed(offset=cq.Vector(protrusion_offset + notch_offset, 0, 0))
    .rect(notch_width, notch_height)
    .cutBlind(notch_depth)
)

result = (
    result.faces(">Z")
    .workplane()
    .transformed(offset=cq.Vector(protrusion_offset + notch_offset, 0, protrusion_height))
    .rect(notch_width, notch_height)
    .cutBlind(notch_depth)
)

# Ensure all edges and corners are sharp by not applying fillets