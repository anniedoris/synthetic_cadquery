import cadquery as cq

# Define dimensions
central_length = 100.0
central_width = 30.0
extension_length = 20.0
extension_width = 15.0
thickness = 5.0

# Create the base plate
result = cq.Workplane("XY").box(central_length, central_width, thickness)

# Add the left extension
result = (
    result.faces("<X")
    .workplane(offset=-extension_length/2)
    .rect(extension_length, extension_width, forConstruction=True)
    .vertices()
    .rect(extension_length, extension_width)
    .extrude(thickness)
)

# Add the right extension
result = (
    result.faces(">X")
    .workplane(offset=extension_length/2)
    .rect(extension_length, extension_width, forConstruction=True)
    .vertices()
    .rect(extension_length, extension_width)
    .extrude(thickness)
)

# Ensure symmetry by checking that the extensions are properly aligned
# The central plate is centered at (0,0,0) with dimensions (100,30,5)
# The extensions are added at the left and right faces, each with dimensions (20,15,5)
# The extensions are positioned so that they extend from the edges of the central plate