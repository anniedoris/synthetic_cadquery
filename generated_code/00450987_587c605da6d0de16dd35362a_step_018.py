import cadquery as cq

# Dimensions
length = 80.0
width = 40.0
thickness = 5.0
circle_hole_dia = 12.0
small_hole_dia = 4.0
small_hole_spacing = 15.0
small_hole_offset = 20.0

# Create the rectangular plate
result = cq.Workplane("XY").box(length, width, thickness)

# Add the large circular hole near one end
result = (
    result.faces(">Z")
    .workplane()
    .moveTo(-length/2 + small_hole_offset, 0)
    .circle(circle_hole_dia/2)
    .cutThruAll()
)

# Add the four smaller holes in a rectangular pattern
# Top row of small holes
result = (
    result.faces(">Z")
    .workplane()
    .moveTo(-length/2 + small_hole_offset, width/2 - small_hole_spacing)
    .circle(small_hole_dia/2)
    .cutThruAll()
)
result = (
    result.faces(">Z")
    .workplane()
    .moveTo(-length/2 + small_hole_offset, -(width/2 - small_hole_spacing))
    .circle(small_hole_dia/2)
    .cutThruAll()
)

# Add slight fillet to corners for stress reduction
result = result.edges("|Z").fillet(1.0)

# Rotate the plate to create the angled orientation
result = result.rotate((0, 0, 0), (1, 0, 0), 15)