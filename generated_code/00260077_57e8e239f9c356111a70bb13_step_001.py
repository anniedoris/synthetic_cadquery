import cadquery as cq

# Define dimensions
flat_length = 100.0
flat_width = 20.0
curved_radius = 30.0
thickness = 5.0
hole_diameter = 4.0
hole_spacing = 20.0
notch_width = 8.0
notch_height = 6.0

# Create the base rectangular plate
result = cq.Workplane("XY").box(flat_length, flat_width, thickness)

# Create the curved section by cutting a quarter-circle from the end
# First, create a workplane at the end of the flat section
result = (
    result.faces(">X")
    .workplane()
    .center(0, -flat_width/2)
    .moveTo(0, 0)
    .threePointArc((curved_radius, curved_radius), (curved_radius, 0))
    .close()
    .cutThruAll()
)

# Add holes along the flat section
num_holes = int((flat_length - 20) / hole_spacing) + 1
for i in range(num_holes):
    hole_x = -flat_length/2 + 10 + i * hole_spacing
    result = (
        result.faces(">Z")
        .workplane()
        .center(hole_x, 0)
        .hole(hole_diameter)
    )

# Add holes at the ends of the curved section
result = (
    result.faces(">X")
    .workplane()
    .center(0, -flat_width/2)
    .circle(hole_diameter/2)
    .cutThruAll()
)

result = (
    result.faces("<X")
    .workplane()
    .center(0, -flat_width/2)
    .circle(hole_diameter/2)
    .cutThruAll()
)

# Add notches near the ends of the curved section
result = (
    result.faces(">X")
    .workplane()
    .center(0, -flat_width/2)
    .rect(notch_width, notch_height, forConstruction=True)
    .vertices()
    .hole(3.0)
)

result = (
    result.faces("<X")
    .workplane()
    .center(0, -flat_width/2)
    .rect(notch_width, notch_height, forConstruction=True)
    .vertices()
    .hole(3.0)
)

# Ensure the curved section has a smooth transition by filleting the corner
result = result.edges("|Z").fillet(2.0)