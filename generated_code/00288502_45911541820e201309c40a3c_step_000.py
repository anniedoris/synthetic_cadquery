import cadquery as cq

# Define dimensions
l_width = 10.0
l_thickness = 5.0
vertical_leg_length = 20.0
horizontal_leg_length = 30.0
projection_width = 8.0
projection_length = 15.0
projection_thickness = 5.0

# Create the L-shaped base
# Start with a rectangle for the vertical leg
result = (
    cq.Workplane("XY")
    .rect(l_width, vertical_leg_length)
    .extrude(l_thickness)
)

# Add the horizontal leg extending from the top of the vertical leg
result = (
    result.faces(">Z")
    .workplane()
    .moveTo(0, vertical_leg_length)
    .rect(l_width, horizontal_leg_length)
    .extrude(l_thickness)
)

# Add rectangular projection at the end of the vertical leg (bottom)
result = (
    result.faces("<Z")
    .workplane(offset=-l_thickness)
    .moveTo(0, -l_thickness)
    .rect(projection_width, projection_length)
    .extrude(projection_thickness)
)

# Add rectangular projection at the end of the horizontal leg (right)
result = (
    result.faces(">Y")
    .workplane()
    .moveTo(horizontal_leg_length, 0)
    .rect(projection_length, projection_width)
    .extrude(projection_thickness)
)

# Ensure the projections are properly aligned with the L-shape
# The projections should be perpendicular to their respective legs
# We'll make sure the dimensions are correct by checking the final result