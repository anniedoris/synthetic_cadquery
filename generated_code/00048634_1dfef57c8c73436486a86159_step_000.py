import cadquery as cq

# Define dimensions
plate_length = 50.0
plate_width = 30.0
plate_thickness = 5.0
circle_diameter = 10.0
flange_length = 20.0
flange_width = 8.0

# Create the base plate
result = cq.Workplane("XY").box(plate_length, plate_width, plate_thickness)

# Create the circular cutout in the center of the top face
result = (
    result.faces(">Z")
    .workplane()
    .circle(circle_diameter / 2.0)
    .cutThruAll()
)

# Create the flange extending from one edge of the plate
# The flange extends from the right edge (positive X direction)
result = (
    result.faces(">X")
    .workplane(offset=plate_thickness/2.0)
    .rect(flange_length, flange_width, centered=False)
    .extrude(plate_thickness)
)

# Ensure the flange is properly connected to the plate
# The flange should be positioned so that it extends perpendicularly from the plate
# We'll move it to the correct position
result = result.faces(">X").workplane(offset=plate_thickness).rect(flange_length, flange_width, centered=False).extrude(plate_thickness)