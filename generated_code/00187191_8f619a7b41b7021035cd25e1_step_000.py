import cadquery as cq

# Define dimensions
central_length = 100.0
central_width = 20.0
central_height = 10.0
end_piece_length = 20.0
end_piece_width = 20.0
end_piece_height = 10.0
hole_diameter = 6.0

# Create the central section
result = cq.Workplane("XY").box(central_length, central_width, central_height)

# Add the first end piece (left side)
result = (
    result.faces("<X")
    .workplane()
    .box(end_piece_length, end_piece_width, end_piece_height)
)

# Add the second end piece (right side)
result = (
    result.faces(">X")
    .workplane()
    .box(end_piece_length, end_piece_width, end_piece_height)
)

# Add holes to the end pieces
# Hole in the left end piece
result = (
    result.faces("<X")
    .workplane()
    .hole(hole_diameter)
)

# Hole in the right end piece
result = (
    result.faces(">X")
    .workplane()
    .hole(hole_diameter)
)

# Ensure the holes are centered on the end pieces
# The holes should be at the center of the end pieces, which is already the case
# since the workplane is centered on the face when using default origin