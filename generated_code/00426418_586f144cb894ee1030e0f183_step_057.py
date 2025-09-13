import cadquery as cq

# Define dimensions
body_length = 80.0
body_width = 30.0
body_height = 10.0

# Cylindrical protrusion dimensions
cylinder_diameter = 8.0
cylinder_height = 15.0

# Rectangular protrusion dimensions
rect_protrusion_length = 12.0
rect_protrusion_width = 8.0
rect_protrusion_height = 10.0

# Hole diameter
hole_diameter = 4.0

# Create the main body
result = cq.Workplane("XY").box(body_length, body_width, body_height)

# Add cylindrical protrusion on the left side
result = (
    result.faces(">X")
    .workplane(offset=-body_height/2)
    .center(-body_length/2 + cylinder_diameter/2, 0)
    .circle(cylinder_diameter/2)
    .extrude(cylinder_height)
)

# Add rectangular protrusion on the right side
result = (
    result.faces(">X")
    .workplane(offset=body_height/2)
    .center(body_length/2 - rect_protrusion_length/2, body_width/2 - rect_protrusion_width/2)
    .rect(rect_protrusion_length, rect_protrusion_width)
    .extrude(rect_protrusion_height)
)

# Drill holes through the main body
# Hole near left cylindrical protrusion
result = (
    result.faces(">X")
    .workplane(offset=-body_height/2)
    .center(-body_length/2 + cylinder_diameter/2, 0)
    .hole(hole_diameter)
)

# Hole near right rectangular protrusion
result = (
    result.faces(">X")
    .workplane(offset=-body_height/2)
    .center(body_length/2 - rect_protrusion_length/2, body_width/2 - rect_protrusion_width/2)
    .hole(hole_diameter)
)

# Add small indentation hole on top surface near right end
result = (
    result.faces(">Z")
    .workplane(offset=body_height/2)
    .center(body_length/2 - 5.0, body_width/2 - 5.0)
    .circle(2.0)
    .cutThruAll()
)