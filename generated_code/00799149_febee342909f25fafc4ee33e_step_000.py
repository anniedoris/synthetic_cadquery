import cadquery as cq

# Dimensions
length = 100.0
width = 60.0
thickness = 3.0
taper_height = 5.0  # Height of the taper/bevel

# Create the base rectangular plate with taper
result = (
    cq.Workplane("XY")
    .rect(length, width)
    .workplane(offset=thickness)
    .rect(length - taper_height, width)
    .loft(combine=True)
)

# Add the five large circular cutouts
cutout_positions = [
    (20, 15),   # Bottom left
    (80, 15),   # Bottom right
    (50, 30),   # Center
    (20, 45),   # Top left
    (80, 45),   # Top right
]

for x, y in cutout_positions:
    result = (
        result.faces(">Z")
        .workplane(centerOption="CenterOfMass")
        .center(x - length/2, y - width/2)
        .circle(8.0)
        .cutThruAll()
    )

# Add the three smaller holes
hole_positions = [
    (15, 55),   # Top left corner
    (85, 55),   # Top right corner
    (50, 55),   # Center top
]

for x, y in hole_positions:
    result = (
        result.faces(">Z")
        .workplane(centerOption="CenterOfMass")
        .center(x - length/2, y - width/2)
        .circle(2.0)
        .cutThruAll()
    )

# Add fillets to edges for a more realistic appearance (optional)
# result = result.edges("|Z").fillet(0.5)