import cadquery as cq

# Define dimensions
width = 40.0
height = 30.0
depth = 10.0
opening_width = 20.0
opening_height = 15.0
slope_height = 8.0

# Create the main rectangular prism
result = cq.Workplane("XY").box(width, height, depth)

# Create the rectangular opening through the thickness
# This opening is centered in the main body
result = (
    result.faces(">Z")
    .workplane()
    .rect(opening_width, opening_height)
    .cutThruAll()
)

# Create the sloped triangular section on top
# This creates a triangular prism that slopes from one side of the opening to the other
result = (
    result.faces(">Z")
    .workplane(offset=depth)
    .moveTo(-opening_width/2, opening_height/2)
    .lineTo(opening_width/2, opening_height/2)
    .lineTo(0, opening_height/2 + slope_height)
    .close()
    .extrude(depth)
)

# Create the triangular internal section within the opening
# This triangle has its base parallel to the bottom edge of the opening
result = (
    result.faces(">Z")
    .workplane()
    .moveTo(-opening_width/2, -opening_height/2)
    .lineTo(opening_width/2, -opening_height/2)
    .lineTo(0, opening_height/2)
    .close()
    .extrude(depth)
)

# Remove the internal triangle from the opening (cutting it out)
result = (
    result.faces(">Z")
    .workplane()
    .moveTo(-opening_width/2, -opening_height/2)
    .lineTo(opening_width/2, -opening_height/2)
    .lineTo(0, opening_height/2)
    .close()
    .cutThruAll()
)