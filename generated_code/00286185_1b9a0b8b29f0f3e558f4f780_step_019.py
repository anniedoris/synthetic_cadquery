import cadquery as cq

# Define dimensions
length = 10.0
width = 5.0
height = 2.0
fillet_radius = 0.5

# Create the rectangular prism with rounded edges
result = (
    cq.Workplane("XY")
    .box(length, width, height)
    .edges("|Z")  # Select all edges perpendicular to Z (the vertical edges)
    .fillet(fillet_radius)  # Apply fillet to all vertical edges
    .edges("#Z")  # Select edges parallel to Z (top and bottom edges)
    .fillet(fillet_radius)  # Apply fillet to top and bottom edges
)

# The object is already oriented with the top face visible, 
# and the angle is naturally achieved by the 3D perspective
# when viewed in a CAD environment