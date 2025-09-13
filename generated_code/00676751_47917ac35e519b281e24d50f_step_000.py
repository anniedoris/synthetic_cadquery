import cadquery as cq

# Define dimensions
width = 20.0      # Width of both sections
length_horizontal = 40.0  # Length of horizontal section
length_vertical = 30.0    # Length of vertical section
thickness = 5.0   # Thickness of the bracket

# Create the L-shaped bracket
# Start with the horizontal section
result = (
    cq.Workplane("XY")
    .rect(length_horizontal, width)
    .extrude(thickness)
    .faces(">Z")
    .workplane()
    .rect(width, length_vertical)
    .extrude(thickness)
)

# The above creates an L-shape where:
# - First extrusion creates the horizontal part (length_horizontal x width x thickness)
# - Second extrusion creates the vertical part (width x length_vertical x thickness)
# - The two parts are joined at the corner where they meet