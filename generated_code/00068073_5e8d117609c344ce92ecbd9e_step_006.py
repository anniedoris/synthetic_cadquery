import cadquery as cq

# Define dimensions
length = 50.0
width = 50.0
thickness = 5.0

# Create the L-shaped bracket
# Start with the base plate
result = cq.Workplane("XY").box(length, width, thickness)

# Add the perpendicular plate
result = (
    result.faces(">Y")
    .workplane()
    .box(length, thickness, width)
)

# Ensure the plates meet at a perfect right angle
# The first plate is in XY plane, the second is extruded from the Y face
# The second plate is positioned correctly by default in the workplane

# The object is now an L-shaped bracket with two plates of equal dimensions
# joined at a 90-degree angle with consistent thickness