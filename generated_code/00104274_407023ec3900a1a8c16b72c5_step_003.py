import cadquery as cq

# Define dimensions
length = 4.0
width = 4.0
height = 3.0

# Create the base box
result = cq.Workplane("XY").box(length, width, height)

# Apply a transformation to give it a perspective view
# Rotate around the X-axis to tilt the top face toward the viewer
result = result.rotate((0, 0, 0), (1, 0, 0), 15)

# Then rotate around the Y-axis to show the side face
result = result.rotate((0, 0, 0), (0, 1, 0), 15)