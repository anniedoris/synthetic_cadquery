import cadquery as cq

# Define dimensions
length = 50.0
width = 10.0
thickness = 5.0
large_hole_diameter = 8.0
small_hole_diameter = 4.0
hole_radius = large_hole_diameter / 2.0
small_hole_radius = small_hole_diameter / 2.0

# Create the base plate
result = cq.Workplane("XY").box(length, width, thickness)

# Create the large cylindrical hole at one end
result = (
    result.faces(">Z")
    .workplane()
    .circle(hole_radius)
    .cutThruAll()
)

# Create the small cylindrical hole at the other end
result = (
    result.faces("<Z")
    .workplane()
    .circle(small_hole_radius)
    .cutThruAll()
)

# Add fillets to the edges of the cylindrical holes for smooth transitions
result = result.edges("|Z").fillet(1.0)

# Add fillets to the edges of the central flat section
result = result.edges("#Z").fillet(1.0)