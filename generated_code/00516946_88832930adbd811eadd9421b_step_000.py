import cadquery as cq

# Define dimensions
length = 10.0
width = 2.0  
height = 2.0

# Create the rectangular prism
result = cq.Workplane("XY").box(length, width, height)

# Rotate the prism to create the tilted effect
# Rotate around the Y-axis by 30 degrees to tilt one face
result = result.rotate((0, 0, 0), (0, 1, 0), 30)

# Also rotate around the X-axis to further enhance the tilted appearance
result = result.rotate((0, 0, 0), (1, 0, 0), 15)