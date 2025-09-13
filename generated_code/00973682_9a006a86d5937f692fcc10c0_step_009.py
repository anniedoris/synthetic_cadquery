import cadquery as cq

# Base dimensions
base_length = 50.0
base_width = 30.0
base_height = 10.0

# Extended section dimensions
ext_length = 20.0
ext_width = 15.0
ext_height = 10.0

# Hole diameter
hole_diameter = 6.0

# Recessed circle diameter
recess_diameter = 20.0

# Create the base
result = cq.Workplane("XY").box(base_length, base_width, base_height)

# Add the recessed circular area on the front face
result = (
    result.faces(">Z")
    .workplane()
    .center(-base_length/2 + recess_diameter/2, 0)
    .circle(recess_diameter/2)
    .cutBlind(-base_height/2)
)

# Add holes on the base top surface
result = (
    result.faces(">Z")
    .workplane()
    .center(-base_length/4, -base_width/4)
    .hole(hole_diameter)
    .center(base_length/2, base_width/4)
    .hole(hole_diameter)
)

# Create the extended section
result = (
    result.faces(">Z")
    .workplane()
    .center(base_length/2, 0)
    .box(ext_length, ext_width, ext_height)
)

# Add hole to the extended section
result = (
    result.faces(">X")
    .workplane()
    .center(0, 0)
    .hole(hole_diameter)
)

# Rotate the object to show the top, front, and side faces
result = result.rotate((0, 0, 0), (0, 1, 0), 30)