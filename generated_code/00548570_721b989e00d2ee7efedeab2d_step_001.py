import cadquery as cq

# Define dimensions
top_length = 100.0
top_width = 60.0
depth = 40.0
top_height = 10.0
front_recess = 5.0
hole_diameter = 6.0
hole_offset = 10.0

# Create the base box
result = cq.Workplane("XY").box(top_length, top_width, depth)

# Create the top surface with inclination
# We'll create a trapezoidal cross-section by offsetting the top face
result = (
    result.faces(">Z")
    .workplane()
    .rect(top_length, top_width)
    .workplane(offset=top_height)
    .rect(top_length - front_recess, top_width)
    .loft(combine=True)
)

# Create the front opening with a recess
result = (
    result.faces(">X")
    .workplane()
    .rect(top_length - front_recess, top_width)
    .cutBlind(-depth)
)

# Add the circular hole near the bottom-left corner of the front opening
result = (
    result.faces(">X")
    .workplane(offset=-depth + hole_offset)
    .center(-top_length/2 + hole_offset, top_width/2 - hole_offset)
    .circle(hole_diameter/2)
    .cutThruAll()
)

# Create the side walls
# The side walls are already formed by the box extrusion, but we can add some details

# Add a slight overhang to the top surface
result = (
    result.faces(">Z")
    .workplane(offset=top_height)
    .rect(top_length + 2, top_width + 2)
    .workplane(offset=-top_height)
    .rect(top_length, top_width)
    .loft(combine=True)
)

# Adjust to make the front slightly open with a step
result = (
    result.faces(">X")
    .workplane(offset=-front_recess)
    .rect(top_length - front_recess, top_width)
    .cutBlind(-depth)
)

# Ensure we're working with the correct final shape
result = result.faces(">Z").workplane().rect(top_length, top_width).extrude(top_height)

# Remove the front face to create the open front
result = (
    result.faces(">X")
    .workplane()
    .rect(top_length - front_recess, top_width)
    .cutBlind(-depth)
)

# Create the final shape by subtracting the front opening
result = (
    result.faces(">X")
    .workplane(offset=-front_recess)
    .rect(top_length - front_recess, top_width)
    .cutBlind(-depth)
)

# Add the hole in the front opening
result = (
    result.faces(">X")
    .workplane(offset=-depth + hole_offset)
    .center(-top_length/2 + hole_offset, top_width/2 - hole_offset)
    .circle(hole_diameter/2)
    .cutThruAll()
)