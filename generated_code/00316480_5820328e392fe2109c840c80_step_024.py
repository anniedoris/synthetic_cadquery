import cadquery as cq

# Define dimensions
base_width = 50.0
base_height = 30.0
base_depth = 10.0

# Cutout dimensions
cutout_width = 20.0
cutout_height = 15.0
cutout_depth = 8.0

# Protrusion dimensions
protrusion_width = 10.0
protrusion_height = 12.0
protrusion_depth = 15.0

# Create the base
result = cq.Workplane("XY").box(base_width, base_height, base_depth)

# Add the first cutout (left side)
result = (
    result.faces(">Z")
    .workplane()
    .moveTo(-(base_width/2 - cutout_width/2 - 5), 0)
    .rect(cutout_width, cutout_height)
    .cutBlind(-cutout_depth)
)

# Add the second cutout (right side)
result = (
    result.faces(">Z")
    .workplane()
    .moveTo((base_width/2 - cutout_width/2 - 5), 0)
    .rect(cutout_width, cutout_height)
    .cutBlind(-cutout_depth)
)

# Add left protrusion
result = (
    result.faces(">Z")
    .workplane()
    .moveTo(-(base_width/2 + protrusion_width/2 + 5), 0)
    .rect(protrusion_width, protrusion_height)
    .extrude(protrusion_depth)
)

# Add right protrusion
result = (
    result.faces(">Z")
    .workplane()
    .moveTo((base_width/2 + protrusion_width/2 + 5), 0)
    .rect(protrusion_width, protrusion_height)
    .extrude(protrusion_depth)
)

# Add a fillet to the top edges for a more realistic look
result = result.edges("|Z").fillet(2.0)