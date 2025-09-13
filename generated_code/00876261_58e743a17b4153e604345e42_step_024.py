import cadquery as cq

# Define dimensions
length = 10.0
width = 2.0
height = 2.0

# Create the rectangular prism
result = cq.Workplane("XY").box(length, width, height)

# Rotate to achieve diagonal orientation
# Rotate around the Z axis to create a diagonal appearance
result = result.rotate((0, 0, 0), (0, 0, 1), 30)

# Also rotate around X axis to enhance the diagonal effect
result = result.rotate((0, 0, 0), (1, 0, 0), 15)