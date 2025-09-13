import cadquery as cq

# Dimensions
plate_width_top = 40.0
plate_width_bottom = 50.0
plate_height = 60.0
plate_thickness = 5.0
support_radius = 25.0
support_thickness = 5.0
hole_diameter = 3.0
cutout_width = 10.0
cutout_height = 15.0

# Create the mounting plate with trapezoidal shape
result = (
    cq.Workplane("XY")
    .rect(plate_width_bottom, plate_height)
    .workplane(offset=plate_thickness)
    .rect(plate_width_top, plate_height)
    .loft(combine=True)
    .faces(">Z")
    .workplane()
)

# Add holes
# Top corner holes
result = result.center(-plate_width_top/2 + 10, plate_height/2 - 10).circle(hole_diameter/2).cutThruAll()
result = result.center(plate_width_top/2 - 10, plate_height/2 - 10).circle(hole_diameter/2).cutThruAll()
# Bottom center hole
result = result.center(0, -plate_height/2 + 15).circle(hole_diameter/2).cutThruAll()

# Create the curved support structure
# Start from the bottom edge of the mounting plate
result = (
    result.faces("<Z")
    .workplane()
    .center(0, -plate_height/2)
    .circle(support_radius)
    .workplane(offset=support_thickness)
    .circle(support_radius)
    .loft(combine=True)
)

# Create the cutout in the support structure
result = (
    result.faces(">Z")
    .workplane()
    .center(0, 0)
    .rect(cutout_width, cutout_height)
    .cutThruAll()
)

# Add fillets for smooth transitions
result = result.edges("|Z").fillet(2.0)