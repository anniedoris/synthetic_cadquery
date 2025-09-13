import cadquery as cq

# Define dimensions
length = 100.0
width = 20.0
thickness = 5.0
hole_diameter = 4.0
hole_spacing = 25.0

# Create the rectangular block
result = cq.Workplane("XY").box(length, width, thickness)

# Create holes along the top face
result = (
    result.faces(">Z")
    .workplane()
    .pushPoints([
        (-3 * hole_spacing/2, 0),
        (-hole_spacing/2, 0),
        (hole_spacing/2, 0),
        (3 * hole_spacing/2, 0)
    ])
    .hole(hole_diameter)
)

# Apply a slight tilt to the top face to show perspective
result = result.rotate((0, 0, 0), (1, 0, 0), 10)