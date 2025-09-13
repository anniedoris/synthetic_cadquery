import cadquery as cq

# Create a cylinder with specified dimensions
# Using reasonable dimensions for a visible 3D object
height = 10.0
radius = 3.0

# Create the cylinder
result = cq.Workplane("XY").cylinder(height, radius, centered=False)

# Rotate the cylinder to create the angled perspective
# This rotates around the X-axis by 30 degrees and Y-axis by 45 degrees
result = result.rotate((0, 0, 0), (1, 0, 0), 30)
result = result.rotate((0, 0, 0), (0, 1, 0), 45)