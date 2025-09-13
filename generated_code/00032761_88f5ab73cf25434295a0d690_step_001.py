import cadquery as cq

# Define dimensions
length = 100.0    # Overall length
width = 20.0      # Width of the horizontal section
height = 20.0     # Height of the horizontal section
wall_thickness = 2.0  # Thickness of the walls
cutout_width = 40.0   # Width of the central cutout
cutout_height = 12.0  # Height of the central cutout

# Create the base solid (outer rectangular prism)
result = cq.Workplane("XY").box(length, width, height)

# Create the hollow structure by cutting out the inner dimensions
inner_length = length - 2 * wall_thickness
inner_width = width - 2 * wall_thickness
inner_height = height - 2 * wall_thickness

# Cut out the inner hollow portion
result = result.faces(">Z").workplane(offset=wall_thickness).rect(inner_length, inner_width).extrude(inner_height)

# Create the vertical sections at each end
# First vertical section (left end)
result = (
    result.faces("<X")
    .workplane(offset=-wall_thickness)
    .rect(wall_thickness, width)
    .extrude(height)
)

# Second vertical section (right end)
result = (
    result.faces(">X")
    .workplane(offset=wall_thickness)
    .rect(wall_thickness, width)
    .extrude(height)
)

# Create the central cutout in the horizontal section
# The cutout should be centered in the middle of the horizontal section
cutout_offset = 0  # Since we want it centered along the length
result = (
    result.faces(">Z")
    .workplane(offset=wall_thickness)
    .rect(cutout_width, cutout_height)
    .cutThruAll()
)

# Ensure the cutout is properly centered in the horizontal section
# The cutout is already centered in the middle of the horizontal section
# because we used the face that's centered in the Z direction

# The final result is a hollow rectangular frame with a central cutout
# and vertical sections at each end
result = result