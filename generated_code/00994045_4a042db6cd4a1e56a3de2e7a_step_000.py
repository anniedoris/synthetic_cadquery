import cadquery as cq

# Define dimensions
cylinder_diameter = 20.0
cylinder_length = 60.0
protrusion_diameter = 8.0
protrusion_height = 5.0

# Create the main cylindrical body
result = cq.Workplane("XY").circle(cylinder_diameter/2).extrude(cylinder_length)

# Create the protruding feature on one end
# Move to the end of the cylinder and create the protrusion
result = (
    result.faces(">Z")
    .workplane()
    .circle(protrusion_diameter/2)
    .extrude(protrusion_height)
)

# Rotate the object to achieve the diagonal orientation
result = result.rotate((0, 0, 0), (1, 1, 0), 30)

# Ensure the end caps are flush by checking the faces and making sure they're properly aligned
# The default extrude operation already creates flush end caps, so no additional action needed