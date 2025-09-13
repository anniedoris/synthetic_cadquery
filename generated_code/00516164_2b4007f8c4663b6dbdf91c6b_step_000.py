import cadquery as cq

# Define dimensions
base_length = 50.0
base_width = 30.0
base_thickness = 5.0

vertical1_height = 40.0
vertical1_width = 20.0
vertical1_thickness = 5.0

vertical2_height = 35.0
vertical2_width = 25.0
vertical2_thickness = 5.0

cutout_width = 8.0
cutout_height = 10.0
cutout_offset = 5.0

# Create the base plate
result = cq.Workplane("XY").box(base_length, base_width, base_thickness)

# Create the first vertical section (perpendicular to base)
result = (
    result.faces(">Z")
    .workplane()
    .rect(vertical1_width, vertical1_height, forConstruction=True)
    .vertices()
    .rect(vertical1_width - 2 * cutout_offset, cutout_height, forConstruction=True)
    .vertices("<XY")
    .hole(cutout_width, cutout_height)
    .transformed(offset=cq.Vector(0, base_width/2 - vertical1_height/2, base_thickness))
    .rect(vertical1_width, vertical1_height)
    .extrude(vertical1_thickness)
)

# Create the second vertical section (perpendicular to base and first vertical)
result = (
    result.faces(">Z")
    .workplane()
    .rect(vertical2_width, vertical2_height, forConstruction=True)
    .vertices()
    .rect(vertical2_width - 2 * cutout_offset, cutout_height, forConstruction=True)
    .vertices("<XY")
    .hole(cutout_width, cutout_height)
    .transformed(offset=cq.Vector(base_length/2 - vertical2_width/2, 0, base_thickness))
    .rect(vertical2_width, vertical2_height)
    .extrude(vertical2_thickness)
)

# Add the base cutout
result = (
    result.faces("<Z")
    .workplane()
    .rect(base_length - 2 * cutout_offset, cutout_height, forConstruction=True)
    .vertices("<XY")
    .hole(cutout_width, cutout_height)
)

# Ensure all intersections are clean and precise
result = result.edges("|Z").fillet(1.0)