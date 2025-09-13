import cadquery as cq

# Dimensions for the flange (left object)
flange_outer_diameter = 20.0
flange_inner_diameter = 8.0
flange_thickness = 5.0
flange_chamfer = 1.0

# Dimensions for the shaft (right object)
shaft_diameter = 7.0
shaft_length = 15.0
shaft_flange_diameter = 18.0
shaft_flange_thickness = 3.0
shaft_chamfer = 0.5

# Create the flange (left object)
flange = (
    cq.Workplane("XY")
    .circle(flange_outer_diameter / 2.0)  # Outer circle
    .circle(flange_inner_diameter / 2.0)   # Inner circle (hole)
    .extrude(flange_thickness)
    .faces(">Z")
    .chamfer(flange_chamfer)  # Chamfer outer edges
    .faces("<Z")
    .chamfer(flange_chamfer)  # Chamfer inner edges
)

# Create the shaft with flange (right object)
shaft = (
    cq.Workplane("XY")
    .circle(shaft_diameter / 2.0)  # Shaft cylinder
    .extrude(shaft_length)
    .faces(">Z")
    .chamfer(shaft_chamfer)  # Chamfer top of shaft
    .faces("<Z")
    .chamfer(shaft_chamfer)  # Chamfer bottom of shaft
    .faces(">Z")
    .workplane()
    .circle(shaft_flange_diameter / 2.0)  # Flange base
    .circle(shaft_diameter / 2.0)  # Central hole for shaft
    .extrude(shaft_flange_thickness)
    .faces(">Z")
    .chamfer(shaft_chamfer)  # Chamfer flange edges
)

# Position the shaft to align with the flange
# Move the shaft to be positioned above the flange
shaft = shaft.translate((0, 0, flange_thickness))

# Combine the two objects for the final result
result = flange.union(shaft)