import cadquery as cq

# Define dimensions
length = 10.0
width = 10.0
height = 10.0
hole_diameter = 3.0

# Create the base box
result = cq.Workplane("XY").box(length, width, height)

# Add the centered circular hole on the top surface
result = (
    result.faces(">Z")
    .workplane()
    .circle(hole_diameter / 2.0)
    .cutThruAll()
)