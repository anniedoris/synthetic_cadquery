import cadquery as cq

# Define dimensions
base_length = 50.0
base_width = 30.0
base_thickness = 5.0

side_wall_height_long = 20.0
side_wall_height_short = 15.0
side_wall_thickness = 3.0

protrusion1_length = 8.0
protrusion1_width = 4.0
protrusion1_height = 6.0
protrusion1_offset_y = 5.0

protrusion2_length = 6.0
protrusion2_width = 3.0
protrusion2_height = 4.0
protrusion2_offset_y = 12.0

protrusion3_length = 5.0
protrusion3_width = 2.5
protrusion3_height = 3.0
protrusion3_offset_y = 10.0

notch1_length = 6.0
notch1_width = 3.0
notch1_depth = 2.0
notch1_offset_y = 2.0

notch2_length = 4.0
notch2_width = 2.0
notch2_depth = 1.5
notch2_offset_y = 18.0

# Create the base plate
result = cq.Workplane("XY").box(base_length, base_width, base_thickness)

# Add the longer side wall
result = (
    result.faces(">Z")
    .workplane(offset=base_thickness)
    .rect(base_length, side_wall_height_long, forConstruction=True)
    .vertices()
    .rect(side_wall_thickness, side_wall_height_long - side_wall_thickness)
    .extrude(side_wall_thickness)
)

# Add the shorter side wall
result = (
    result.faces(">Z")
    .workplane(offset=base_thickness)
    .rect(base_length, side_wall_height_short, forConstruction=True)
    .vertices("<XY")
    .rect(side_wall_thickness, side_wall_height_short - side_wall_thickness)
    .extrude(side_wall_thickness)
)

# Add protrusions to the longer side wall
# First protrusion
result = (
    result.faces(">Z")
    .workplane(offset=base_thickness + side_wall_thickness)
    .moveTo(0, protrusion1_offset_y)
    .rect(protrusion1_length, protrusion1_width)
    .extrude(protrusion1_height)
)

# Second protrusion
result = (
    result.faces(">Z")
    .workplane(offset=base_thickness + side_wall_thickness)
    .moveTo(0, protrusion2_offset_y)
    .rect(protrusion2_length, protrusion2_width)
    .extrude(protrusion2_height)
)

# Add protrusion to the shorter side wall
result = (
    result.faces(">Z")
    .workplane(offset=base_thickness + side_wall_thickness)
    .moveTo(0, protrusion3_offset_y)
    .rect(protrusion3_length, protrusion3_width)
    .extrude(protrusion3_height)
)

# Add notches
# Notch on the shorter side wall
result = (
    result.faces(">Z")
    .workplane(offset=base_thickness + side_wall_thickness)
    .moveTo(0, notch1_offset_y)
    .rect(notch1_length, notch1_width)
    .cutBlind(-notch1_depth)
)

# Notch on the longer side wall
result = (
    result.faces(">Z")
    .workplane(offset=base_thickness + side_wall_thickness)
    .moveTo(0, notch2_offset_y)
    .rect(notch2_length, notch2_width)
    .cutBlind(-notch2_depth)
)

# Add fillets to improve aesthetics and remove sharp edges
result = result.edges("|Z").fillet(1.0)