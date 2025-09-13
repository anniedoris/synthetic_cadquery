import cadquery as cq

# Define dimensions
height = 20.0
width = 4.0
depth1 = 6.0  # First segment depth
depth2 = 8.0  # Second segment depth
depth3 = 10.0 # Third segment depth
depth4 = 6.0  # Fourth segment depth
depth5 = 8.0  # Fifth segment depth
rounding_radius = 1.0

# Create the base workplane
result = cq.Workplane("XY")

# Create first vertical segment
segment1 = (
    cq.Workplane("XY")
    .box(width, depth1, height)
    .faces(">Z")
    .edges("|X or |Y")
    .fillet(rounding_radius)
)

# Create second vertical segment, offset and rotated
segment2 = (
    cq.Workplane("XY")
    .move(0, 0)
    .box(width, depth2, height)
    .faces(">Z")
    .edges("|X or |Y")
    .fillet(rounding_radius)
    .translate((0, 3, 0))  # Move to create offset
)

# Create third vertical segment, offset and rotated
segment3 = (
    cq.Workplane("XY")
    .move(0, 0)
    .box(width, depth3, height)
    .faces(">Z")
    .edges("|X or |Y")
    .fillet(rounding_radius)
    .translate((0, 6, 0))  # Move to create offset
)

# Create fourth vertical segment, offset and rotated
segment4 = (
    cq.Workplane("XY")
    .move(0, 0)
    .box(width, depth4, height)
    .faces(">Z")
    .edges("|X or |Y")
    .fillet(rounding_radius)
    .translate((0, 9, 0))  # Move to create offset
)

# Create fifth vertical segment, offset and rotated
segment5 = (
    cq.Workplane("XY")
    .move(0, 0)
    .box(width, depth5, height)
    .faces(">Z")
    .edges("|X or |Y")
    .fillet(rounding_radius)
    .translate((0, 12, 0))  # Move to create offset
)

# Combine all segments
result = segment1.union(segment2).union(segment3).union(segment4).union(segment5)

# Add connecting structure between segments
# Create connecting plates
connecting_plate1 = (
    cq.Workplane("XY")
    .move(0, 0)
    .box(width + 2, 1.5, 1.0)
    .translate((0, 1.5, 0))
)

connecting_plate2 = (
    cq.Workplane("XY")
    .move(0, 0)
    .box(width + 2, 1.5, 1.0)
    .translate((0, 4.5, 0))
)

connecting_plate3 = (
    cq.Workplane("XY")
    .move(0, 0)
    .box(width + 2, 1.5, 1.0)
    .translate((0, 7.5, 0))
)

connecting_plate4 = (
    cq.Workplane("XY")
    .move(0, 0)
    .box(width + 2, 1.5, 1.0)
    .translate((0, 10.5, 0))
)

# Add connecting plates to the result
result = result.union(connecting_plate1).union(connecting_plate2).union(connecting_plate3).union(connecting_plate4)

# Final result
result = result