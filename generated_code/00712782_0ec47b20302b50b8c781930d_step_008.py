import cadquery as cq

# Define dimensions for the rectangular prism
length = 4.0
width = 3.0
height = 1.0

# Create the base box
result = cq.Workplane("XY").box(length, width, height)

# Apply a rotation to create the angled perspective effect
# Rotate around the X-axis to tilt the top face up and bottom face down
result = result.rotate((0, 0, 0), (1, 0, 0), 15)

# Apply a rotation around the Y-axis to give it the side tilt
result = result.rotate((0, 0, 0), (0, 1, 0), 10)