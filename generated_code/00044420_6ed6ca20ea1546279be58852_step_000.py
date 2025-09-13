import cadquery as cq

# Define dimensions
length = 100.0
width = 60.0
thickness = 10.0
hole1_dia = 4.0  # Small hole
hole2_dia = 4.0  # Small hole
hole3_dia = 8.0  # Large center hole
flange_width = 15.0
flange_height = 10.0
flange_thickness = thickness
cutout_width = 6.0
cutout_height = 4.0

# Create the main plate
result = cq.Workplane("XY").box(length, width, thickness)

# Add holes on top surface
# Two small holes near top edge
result = (
    result.faces(">Z")
    .workplane()
    .pushPoints([(-30, 20), (30, 20)])
    .circle(hole1_dia/2)
    .cutThruAll()
)

# One large center hole
result = (
    result.faces(">Z")
    .workplane()
    .center(0, 0)
    .circle(hole3_dia/2)
    .cutThruAll()
)

# Add flange on the left side (negative X direction)
result = (
    result.faces("<X")
    .workplane(offset=-flange_width/2)
    .rect(flange_width, flange_height)
    .extrude(flange_thickness)
)

# Add rectangular cutout to the flange
result = (
    result.faces("<X")
    .workplane(offset=-flange_width/2, centerOption="CenterOfMass")
    .center(0, flange_height/2 - cutout_height/2)
    .rect(cutout_width, cutout_height)
    .cutBlind(-flange_thickness)
)

# Ensure the flange is properly connected to the main plate
result = result.faces("<X").workplane(offset=-flange_width/2).rect(flange_width, flange_height).extrude(flange_thickness)