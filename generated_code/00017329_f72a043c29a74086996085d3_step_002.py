import cadquery as cq

# Define dimensions
length = 50.0
width = 50.0
height = 10.0
hole_diameter = 20.0

# Create the base rectangular block
result = cq.Workplane("XY").box(length, width, height)

# Add the circular recess on the top face
result = (
    result.faces(">Z")  # Select the top face
    .workplane()        # Create a workplane on that face
    .hole(hole_diameter) # Create the hole
)

# The hole will be centered automatically on the workplane