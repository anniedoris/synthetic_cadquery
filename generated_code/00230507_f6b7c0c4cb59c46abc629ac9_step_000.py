import cadquery as cq

# Define dimensions
base_length = 100.0
base_width = 60.0
base_height = 20.0

platform_length = 80.0
platform_width = 40.0
platform_height = 5.0

cutout_height = 10.0
cutout_width = 15.0
cutout_spacing = 15.0

circle_diameter = 20.0
circle_offset = 10.0

# Create the base rectangular prism
result = cq.Workplane("XY").box(base_length, base_width, base_height)

# Add rectangular cutouts on the side
cutout_y_positions = [
    base_height - cutout_height - 5.0,  # Top cutout
    base_height - 2 * cutout_height - 10.0,
    base_height - 3 * cutout_height - 15.0,
    base_height - 4 * cutout_height - 20.0
]

for y_pos in cutout_y_positions:
    result = (
        result.faces(">Y")
        .workplane(offset=y_pos)
        .rect(cutout_width, cutout_height, forConstruction=True)
        .vertices()
        .hole(2.0)  # Small hole for clearance, or just cut the rectangle
    )

# Add circular cutout on front face
result = (
    result.faces(">Z")
    .workplane(offset=-circle_offset)
    .circle(circle_diameter / 2.0)
    .cutThruAll()
)

# Add flat platform on top
result = (
    result.faces(">Z")
    .workplane(offset=base_height)
    .rect(platform_length, platform_width)
    .extrude(platform_height)
)

# Add red reference lines (triangular shape on the side)
# This is a simplified representation - in reality, this would be 3D lines
# For visualization purposes, we'll add a triangular pattern on one side
result = (
    result.faces(">X")
    .workplane(offset=base_height/2)
    .moveTo(-base_length/2 + 5, base_width/2 - 5)
    .lineTo(-base_length/2 + 15, base_width/2 - 15)
    .lineTo(-base_length/2 + 5, base_width/2 - 15)
    .close()
    .extrude(2)
)

# Ensure all edges are sharp (no fillets)
# The default CadQuery behavior already produces sharp edges
# unless explicitly filleted

# Final result
result = result