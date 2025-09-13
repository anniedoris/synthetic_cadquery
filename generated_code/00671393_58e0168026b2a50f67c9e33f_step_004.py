import cadquery as cq

# Define dimensions
length = 100.0
width = 20.0
height = 10.0

# Create the main rectangular prism
result = cq.Workplane("XY").box(length, width, height)

# Add a seam line by cutting a groove along the length
# The groove is offset slightly from center to create the seam appearance
groove_width = 2.0
groove_depth = 1.0

# Create a workplane on the top face and make a groove
result = (
    result.faces(">Z")
    .workplane()
    .center(0, -height/4)  # Offset the groove slightly from center
    .rect(groove_width, 5.0, forConstruction=True)  # Width of groove
    .vertices()
    .hole(groove_depth)
)

# To create the diagonal perspective effect, we'll rotate the object
# This creates a diagonal orientation with the closer end appearing larger
result = result.rotate((0, 0, 0), (1, 0, 0), 30)
result = result.rotate((0, 0, 0), (0, 1, 0), 15)

# Alternative approach: Create a more realistic diagonal beam with perspective
# by using a slightly skewed approach
result = cq.Workplane("XY").box(length, width, height)

# Add the seam line as a thin cutout
result = (
    result.faces(">Z")
    .workplane()
    .center(0, -height/4)  # Offset to create the seam appearance
    .rect(length, 1.0)     # Long thin rectangle for the seam
    .cutThruAll()
)

# Apply rotation to get the diagonal perspective
result = result.rotate((0, 0, 0), (1, 0, 0), 25)
result = result.rotate((0, 0, 0), (0, 1, 0), 10)