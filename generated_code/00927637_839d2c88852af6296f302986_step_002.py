import cadquery as cq

# Define dimensions
base_length = 40.0
top_length = 20.0
height = 30.0
thickness = 5.0
cutout_diameter = 12.0
inner_cutout_diameter = 4.0
detail_hole_diameter = 3.0

# Create the base trapezoid profile
# Start with a workplane
result = cq.Workplane("XY")

# Draw the trapezoidal profile
# Bottom edge
result = result.lineTo(base_length, 0)
# Slanted edge to top right
result = result.lineTo(top_length, height)
# Top edge
result = result.lineTo(0, height)
# Slanted edge back to bottom left
result = result.lineTo(0, 0)
# Close the profile
result = result.close()

# Extrude to create the 3D object
result = result.extrude(thickness)

# Create the slanted surface by working on the top face
# Select the top face and create a workplane on it
result = (
    result.faces(">Z")
    .workplane()
    .center(-10, -5)  # Position the cutout near center
    .circle(cutout_diameter / 2)
    .cutThruAll()
)

# Add the inner circular detail
result = (
    result.faces(">Z")
    .workplane()
    .center(-10, -5)
    .circle(inner_cutout_diameter / 2)
    .cutThruAll()
)

# Add the small circular detail near the lower right edge
result = (
    result.faces(">Z")
    .workplane()
    .center(top_length - 5, 5)
    .circle(detail_hole_diameter / 2)
    .cutThruAll()
)

# Round the edges for a smoother appearance
result = result.edges("|Z").fillet(1.0)

# The final object is stored in result