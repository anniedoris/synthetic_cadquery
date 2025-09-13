import cadquery as cq

# Define dimensions
length = 40.0
width = 30.0
height = 10.0
hole_diameter = 6.0

# Create the main rectangular prism
result = cq.Workplane("XY").box(length, width, height)

# Add the cylindrical hole near one edge of the top face
# Position the hole near the corner (10mm from the edge)
result = (
    result.faces(">Z")  # Select the top face
    .workplane()        # Create a workplane on the top face
    .center(-length/2 + 10, -width/2 + 10)  # Position near the corner
    .hole(hole_diameter)  # Create through-hole
)

# The hole will automatically go through the entire thickness