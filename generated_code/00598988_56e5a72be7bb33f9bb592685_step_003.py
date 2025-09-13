import cadquery as cq

# Define dimensions
length = 100.0
width = 50.0
thickness = 5.0
fillet_radius = 2.0

# Create the rectangular plate with filleted edges
result = (
    cq.Workplane("XY")
    .box(length, width, thickness)
    .edges("|Z").fillet(fillet_radius)
)

# Rotate to give 3D perspective view
result = result.rotate((0, 0, 0), (1, 0, 0), 30)
result = result.rotate((0, 0, 0), (0, 1, 0), 15)