import cadquery as cq

# Define dimensions for the cylindrical rod
diameter = 10.0
length = 50.0
radius = diameter / 2.0

# Create a cylindrical rod with the specified dimensions
# Using Workplane("XY") as the base plane
result = cq.Workplane("XY").circle(radius).extrude(length)

# Rotate the cylinder to achieve the diagonal perspective view
# This creates a more visually interesting representation with one end closer to the viewer
result = result.rotate((0, 0, 0), (0, 0, 1), 30)
result = result.rotate((0, 0, 0), (1, 0, 0), 15)