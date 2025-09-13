import cadquery as cq

# Define dimensions
prism_length = 80.0
prism_width = 20.0
prism_height = 10.0
cylinder_diameter = 8.0
cylinder_length = 15.0

# Create the main rectangular prism
result = cq.Workplane("XY").box(prism_length, prism_width, prism_height)

# Add cylindrical protrusions on both ends
# First cylinder at one end
result = (
    result.faces(">X")
    .workplane()
    .circle(cylinder_diameter/2)
    .extrude(cylinder_length)
)

# Second cylinder at the opposite end
result = (
    result.faces("<X")
    .workplane()
    .circle(cylinder_diameter/2)
    .extrude(cylinder_length)
)

# Rotate to achieve the diagonal orientation shown in the description
result = result.rotate((0, 0, 0), (1, 0, 0), 15)
result = result.rotate((0, 0, 0), (0, 1, 0), 15)