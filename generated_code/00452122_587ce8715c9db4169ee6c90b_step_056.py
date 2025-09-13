import cadquery as cq

# Define dimensions
length = 80.0
width = 60.0
thickness = 10.0

# Define hole dimensions
small_hole_dia = 6.0
large_hole_dia = 12.0

# Create the base rectangular block
result = cq.Workplane("XY").box(length, width, thickness)

# Add the small hole to the top face (near corner)
# Position it near the top-left corner
result = (
    result.faces(">Z")
    .workplane()
    .center(-length/2 + 15, width/2 - 15)
    .hole(small_hole_dia)
)

# Add the large hole to the front face (near bottom edge)
# Position it near the bottom center of the front face
result = (
    result.faces(">Y")
    .workplane()
    .center(0, -width/2 + 20)
    .hole(large_hole_dia)
)

# Add slight fillets to corners for better appearance
result = result.edges("|Z").fillet(1.0)