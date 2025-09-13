import cadquery as cq

# Define dimensions
length = 80.0
width = 40.0
thickness = 5.0
hole_diameter = 8.0

# Create the base plate
result = cq.Workplane("XY").box(length, width, thickness)

# Add four circular cutouts in two rows
# Top row cutouts
result = (
    result.faces(">Z")
    .workplane()
    .pushPoints([
        (-length/4, width/4),  # Top left
        (length/4, width/4)    # Top right
    ])
    .circle(hole_diameter/2)
    .cutThruAll()
)

# Bottom row cutouts
result = (
    result.faces(">Z")
    .workplane()
    .pushPoints([
        (-length/4, -width/4),  # Bottom left
        (length/4, -width/4)    # Bottom right
    ])
    .circle(hole_diameter/2)
    .cutThruAll()
)