import cadquery as cq

# Define dimensions
height = 100.0
width = 20.0
depth = 20.0
hole_diameter = 4.0
hole_spacing = 20.0
flange_height = 2.0

# Create the main column
result = cq.Workplane("XY").box(width, depth, height)

# Add flanges at top and bottom
result = (
    result.faces(">Z")
    .workplane(offset=flange_height)
    .rect(width, depth)
    .extrude(flange_height)
)

result = (
    result.faces("<Z")
    .workplane(offset=-flange_height)
    .rect(width, depth)
    .extrude(-flange_height)
)

# Add holes on the front face
result = (
    result.faces(">X")
    .workplane()
    .pushPoints([
        (0, -2 * hole_spacing),
        (0, -1 * hole_spacing),
        (0, 0),
        (0, 1 * hole_spacing),
        (0, 2 * hole_spacing)
    ])
    .circle(hole_diameter / 2)
    .cutThruAll()
)

# Add a small fillet to the edges for a more realistic look
result = result.edges("|Z").fillet(1.0)