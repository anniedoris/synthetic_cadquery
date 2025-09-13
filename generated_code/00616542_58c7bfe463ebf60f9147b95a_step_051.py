import cadquery as cq

# Define dimensions
plate_length = 50.0
plate_width = 30.0
plate_thickness = 5.0
cylinder_diameter = 12.0
cylinder_height = 8.0

# Create the rectangular plate
result = cq.Workplane("XY").box(plate_length, plate_width, plate_thickness)

# Create the cylindrical protrusion at the center
result = (
    result.faces(">Z")
    .workplane()
    .center(0, 0)
    .circle(cylinder_diameter / 2.0)
    .extrude(cylinder_height)
)