import cadquery as cq

# Define dimensions for the rectangular prisms
prism_length = 10.0
prism_width = 2.0
prism_height = 2.0

# Number of prisms in the bundle
num_prisms = 5

# Create the first prism
result = cq.Workplane("XY").box(prism_length, prism_width, prism_height)

# Create additional prisms and position them in a line
for i in range(1, num_prisms):
    prism = cq.Workplane("XY").box(prism_length, prism_width, prism_height).translate((i * (prism_length + 0.1), 0, 0))
    result = result.union(prism)

# Rotate the bundle to create the diagonal orientation
result = result.rotate((0, 0, 0), (1, 0, 0), 30)
result = result.rotate((0, 0, 0), (0, 1, 0), 15)