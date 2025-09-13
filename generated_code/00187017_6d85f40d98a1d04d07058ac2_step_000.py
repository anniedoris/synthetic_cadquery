import cadquery as cq

# Define dimensions
length = 100.0
width = 60.0
thickness = 10.0
hole_diameter = 8.0
hole_spacing_x = 40.0
hole_spacing_y = 30.0
hole_offset_x = 20.0
hole_offset_y = 15.0

# Create the base rectangular block
result = cq.Workplane("XY").box(length, width, thickness)

# Add holes to the front face (>Z)
result = (
    result.faces(">Z")
    .workplane()
    .pushPoints([
        (-hole_offset_x, -hole_offset_y),
        (hole_offset_x, -hole_offset_y),
        (-hole_offset_x, hole_offset_y),
        (hole_offset_x, hole_offset_y)
    ])
    .hole(hole_diameter)
)

# Add holes to the back face (<Z)
result = (
    result.faces("<Z")
    .workplane()
    .pushPoints([
        (-hole_offset_x, -hole_offset_y),
        (hole_offset_x, -hole_offset_y),
        (-hole_offset_x, hole_offset_y),
        (hole_offset_x, hole_offset_y)
    ])
    .hole(hole_diameter)
)

# Ensure the holes go through the entire thickness
result = result.faces(">Z").workplane().hole(hole_diameter)