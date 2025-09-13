import cadquery as cq

# Define dimensions
main_diameter = 10.0
main_length = 50.0
pin_diameter = 4.0
pin_length = 8.0

# Create the main cylindrical body
result = cq.Workplane("XY").box(main_length, main_diameter, main_diameter)

# Create the left end pin (perpendicular to main body)
result = (
    result.faces("<X")
    .workplane()
    .circle(pin_diameter/2)
    .extrude(pin_length)
)

# Create the right end pin (perpendicular to main body)
result = (
    result.faces(">X")
    .workplane()
    .circle(pin_diameter/2)
    .extrude(pin_length)
)

# Ensure the pins are flush with the main body by trimming if necessary
# The pins are already positioned correctly since we used the face centers
# and extruded along the axis perpendicular to the face