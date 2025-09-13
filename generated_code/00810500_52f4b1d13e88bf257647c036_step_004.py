import cadquery as cq

# Define dimensions
length = 100.0
width = 20.0
height = 10.0

# Main body
result = cq.Workplane("XY").box(length, width, height)

# Perpendicular attachment at one end
attachment_length = 30.0
attachment_width = 25.0
attachment_height = 15.0
result = (
    result.faces(">X")
    .workplane(offset=attachment_length/2)
    .rect(attachment_width, attachment_height)
    .extrude(attachment_length)
)

# L-shaped brackets at the other end
bracket_height = 8.0
bracket_width = 12.0
bracket_depth = 5.0

# First bracket
result = (
    result.faces("<X")
    .workplane(offset=-bracket_depth)
    .rect(bracket_width, bracket_height)
    .extrude(-bracket_depth)
)

# Second bracket (angled)
result = (
    result.faces("<X")
    .workplane(offset=-bracket_depth-5)
    .transformed(rotate=cq.Vector(0, 30, 0))
    .rect(bracket_width, bracket_height)
    .extrude(-bracket_depth)
)

# Support structures on the side
support_length = 15.0
support_width = 8.0
support_height = 5.0

# First support
result = (
    result.faces(">Y")
    .workplane(offset=height/2)
    .center(-20, 0)
    .rect(support_width, support_height)
    .extrude(support_length)
)

# Second support
result = (
    result.faces(">Y")
    .workplane(offset=height/2)
    .center(20, 0)
    .rect(support_width, support_height)
    .extrude(support_length)
)

# Protrusions on supports
protrusion_width = 3.0
protrusion_height = 2.0
protrusion_length = 4.0

# First protrusion
result = (
    result.faces(">Y")
    .workplane(offset=height/2+support_height/2)
    .center(-20, 0)
    .rect(protrusion_width, protrusion_height)
    .extrude(protrusion_length)
)

# Second protrusion
result = (
    result.faces(">Y")
    .workplane(offset=height/2+support_height/2)
    .center(20, 0)
    .rect(protrusion_width, protrusion_height)
    .extrude(protrusion_length)
)

# Cutouts
# Rectangular cutout in main body
cutout_width = 25.0
cutout_height = 8.0
result = (
    result.faces(">Z")
    .workplane(offset=height/2)
    .center(0, 0)
    .rect(cutout_width, cutout_height)
    .cutThruAll()
)

# Circular holes
hole_diameter = 3.0
result = (
    result.faces(">Z")
    .workplane(offset=height/2)
    .center(-30, 0)
    .hole(hole_diameter)
)

result = (
    result.faces(">Z")
    .workplane(offset=height/2)
    .center(30, 0)
    .hole(hole_diameter)
)

# Additional hole in support
result = (
    result.faces(">Y")
    .workplane(offset=height/2+support_height/2)
    .center(-20, 0)
    .hole(hole_diameter)
)

# Fillet edges for smoother transitions
result = result.edges("|Z").fillet(1.0)

# Ensure the result is assigned to the variable 'result'
result = result