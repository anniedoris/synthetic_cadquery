import cadquery as cq

# Define dimensions
cylinder_diameter = 20.0
cylinder_length = 50.0
hole_diameter = 8.0
chamfer_length = 5.0

# Create the main cylindrical body
result = cq.Workplane("XY").circle(cylinder_diameter/2).extrude(cylinder_length - chamfer_length)

# Add the chamfer at one end
# Create a tapered section
result = (
    result.faces("<Z")
    .workplane()
    .circle(cylinder_diameter/2 - chamfer_length)
    .extrude(chamfer_length)
)

# Add the hole at the other end
result = (
    result.faces(">Z")
    .workplane()
    .hole(hole_diameter)
)

# The chamfer is already created by the extrusion of the smaller circle
# The hole is already created with the hole() method