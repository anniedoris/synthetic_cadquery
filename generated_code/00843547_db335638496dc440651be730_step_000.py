import cadquery as cq

# Define dimensions
prism_length = 50.0
prism_width = 30.0
prism_height = 10.0

cylinder_diameter = 8.0
cylinder_height = 20.0

flange_length = 15.0
flange_width = 8.0
flange_height = 5.0

# Create the main rectangular prism
result = cq.Workplane("XY").box(prism_length, prism_width, prism_height)

# Create the cylindrical protrusion
# Position it on the front face (positive Y direction) and centered on the edge
result = (
    result.faces(">Y")
    .workplane(offset=prism_height/2)
    .center(-prism_length/2 + cylinder_diameter/2, 0)
    .circle(cylinder_diameter/2)
    .extrude(cylinder_height)
)

# Create the small flange on the same face
# Position it on the front face (positive Y direction) and on the opposite side of the cylinder
result = (
    result.faces(">Y")
    .workplane(offset=prism_height/2)
    .center(prism_length/2 - flange_length/2, 0)
    .rect(flange_length, flange_width)
    .extrude(flange_height)
)

# Ensure the object is properly oriented
result = result.rotate((0, 0, 0), (0, 0, 1), 0)