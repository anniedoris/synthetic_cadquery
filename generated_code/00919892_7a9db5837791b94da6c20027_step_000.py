import cadquery as cq

# Plate dimensions
length = 100.0
width = 100.0
thickness = 10.0

# Hole parameters
hole_diameter = 12.0
hole_offset = 15.0

# Create the plate
result = cq.Workplane("XY").box(length, width, thickness)

# Add the four holes in a symmetrical pattern
result = (
    result.faces(">Z")
    .workplane()
    .center(-hole_offset, -hole_offset)
    .circle(hole_diameter/2)
    .center(2*hole_offset, 0)
    .circle(hole_diameter/2)
    .center(0, 2*hole_offset)
    .circle(hole_diameter/2)
    .center(-2*hole_offset, 0)
    .circle(hole_diameter/2)
    .cutThruAll()
)