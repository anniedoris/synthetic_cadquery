import cadquery as cq

# Define dimensions
length = 60.0
width = 20.0
height = 10.0
hole_diameter = 4.0
rounding_radius = 2.0

# Create the base rectangular prism with rounded edges
result = cq.Workplane("XY").box(length, width, height).edges("|Z").fillet(rounding_radius)

# Add the first hole on the front face (visible side)
result = (
    result.faces(">Y")  # Select the front face
    .workplane(offset=0.1)  # Slightly offset to avoid cutting through the part
    .center(-length/2 + 10, 0)  # Position near the edge
    .hole(hole_diameter)
)

# Add the second hole on the back face (other visible side)
result = (
    result.faces("<Y")  # Select the back face
    .workplane(offset=0.1)
    .center(length/2 - 10, 0)  # Position near the edge
    .hole(hole_diameter)
)

# Apply a slight tilt to create the trapezoidal appearance
# Rotate the object around the X-axis to create the skew
result = result.rotate((0, 0, 0), (1, 0, 0), 5)

# Ensure the top and bottom faces are properly aligned with the tilt
# The main body should be a trapezoid when viewed from the side
result = result