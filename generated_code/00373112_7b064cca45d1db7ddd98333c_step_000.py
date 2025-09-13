import cadquery as cq

# Define dimensions
length = 10.0
width = 6.0
depth = 6.0
hole_diameter = 2.0

# Create the rectangular prism
result = cq.Workplane("XY").box(length, width, depth)

# Add the cylindrical hole through the center
result = (
    result.faces(">Z")
    .workplane()
    .hole(hole_diameter)
)

# The hole will be centered and go through the entire length
# The hole is created on the top face and goes through the entire part