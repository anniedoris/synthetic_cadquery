import cadquery as cq

# Dimensions
base_length = 50.0
base_width = 20.0
base_height = 10.0

arm_length = 80.0
arm_width = 15.0
arm_height = 20.0

protrusion_diameter = 8.0
protrusion_height = 15.0
bolt_diameter = 4.0

hollow_width = 12.0
hollow_height = 18.0
hollow_depth = 5.0

roller_diameter = 6.0
bracket_width = 10.0
bracket_height = 8.0
bracket_thickness = 5.0

# Create the base rectangular prism
result = cq.Workplane("XY").box(base_length, base_width, base_height)

# Add the longer arm rectangular prism at right angle
result = (
    result.faces(">Z")
    .workplane()
    .transformed(offset=cq.Vector(0, base_width/2, 0), rotate=cq.Vector(0, 90, 0))
    .box(arm_length, arm_width, arm_height)
)

# Add the cylindrical protrusion on the base
result = (
    result.faces(">Z")
    .workplane()
    .transformed(offset=cq.Vector(base_length/2, 0, 0), rotate=cq.Vector(0, 0, 90))
    .circle(protrusion_diameter/2)
    .extrude(protrusion_height)
)

# Add the bolt-like detail on the protrusion
result = (
    result.faces(">Z")
    .workplane()
    .transformed(offset=cq.Vector(base_length/2, 0, protrusion_height), rotate=cq.Vector(0, 0, 90))
    .circle(bolt_diameter/2)
    .extrude(2)
)

# Create the hollow section in the arm
result = (
    result.faces(">Y")
    .workplane()
    .transformed(offset=cq.Vector(arm_length/2, 0, 0), rotate=cq.Vector(0, 0, 90))
    .rect(hollow_width, hollow_height)
    .extrude(hollow_depth)
)

# Add the roller near the open end of the arm
result = (
    result.faces(">Y")
    .workplane()
    .transformed(offset=cq.Vector(arm_length/2, 0, 0), rotate=cq.Vector(0, 0, 90))
    .circle(roller_diameter/2)
    .extrude(arm_height)
)

# Add the L-shaped bracket at the far end of the arm
result = (
    result.faces(">Y")
    .workplane()
    .transformed(offset=cq.Vector(arm_length/2, 0, 0), rotate=cq.Vector(0, 0, 90))
    .rect(bracket_width, bracket_height)
    .extrude(bracket_thickness)
)

# Add the small protrusion on the bracket
result = (
    result.faces(">Z")
    .workplane()
    .transformed(offset=cq.Vector(arm_length/2, bracket_height/2, bracket_thickness), rotate=cq.Vector(0, 0, 90))
    .circle(3.0)
    .extrude(3)
)

result = result