import cadquery as cq

# Base plate dimensions
base_length = 50.0
base_width = 30.0
base_thickness = 5.0

# Hole parameters
hole_diameter = 4.0
hole_offset = 8.0

# Cylindrical protrusion dimensions
cap_diameter = 6.0
cap_height = 2.0
threaded_diameter = 8.0
threaded_height = 4.0
base_diameter = 10.0
base_height = 3.0

# Create the base plate with rounded edges
result = cq.Workplane("XY").rect(base_length, base_width).extrude(base_thickness)

# Add corner holes
result = (
    result.faces(">Z")
    .workplane()
    .pushPoints([
        (base_length/2 - hole_offset, base_width/2 - hole_offset),
        (-base_length/2 + hole_offset, base_width/2 - hole_offset),
        (-base_length/2 + hole_offset, -base_width/2 + hole_offset),
        (base_length/2 - hole_offset, -base_width/2 + hole_offset)
    ])
    .hole(hole_diameter)
)

# Create the stepped cylindrical protrusion
# Base section
result = (
    result.faces(">Z")
    .workplane()
    .center(0, 0)
    .circle(base_diameter/2)
    .extrude(base_height)
)

# Threaded section
result = (
    result.faces(">Z")
    .workplane()
    .center(0, 0)
    .circle(threaded_diameter/2)
    .extrude(threaded_height)
)

# Cap section
result = (
    result.faces(">Z")
    .workplane()
    .center(0, 0)
    .circle(cap_diameter/2)
    .extrude(cap_height)
)

# Fillet the transitions for smooth edges
result = result.edges("|Z").fillet(0.5)