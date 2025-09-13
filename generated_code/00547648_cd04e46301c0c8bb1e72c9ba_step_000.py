import cadquery as cq
from math import sin, cos, pi

# Define dimensions
fuselage_length = 120.0
fuselage_radius = 8.0
upper_wing_length = 80.0
upper_wing_width = 15.0
lower_wing_length = 80.0
lower_wing_width = 15.0
wing_thickness = 2.0
strut_diameter = 2.0
tail_length = 40.0
tail_width = 20.0
tail_height = 15.0
propeller_diameter = 15.0
propeller_blade_length = 8.0
propeller_blade_width = 3.0

# Create fuselage
fuselage = cq.Workplane("XY").box(fuselage_length, fuselage_radius * 2, fuselage_radius * 2)

# Create upper wing
upper_wing = (
    cq.Workplane("XY")
    .center(0, fuselage_radius + 5)
    .rect(upper_wing_length, upper_wing_width)
    .extrude(wing_thickness)
    .faces(">Z")
    .workplane()
    .circle(upper_wing_width/2)
    .extrude(wing_thickness)
    .faces("<Z")
    .workplane()
    .circle(upper_wing_width/2)
    .extrude(wing_thickness)
)

# Create lower wing
lower_wing = (
    cq.Workplane("XY")
    .center(0, -(fuselage_radius + 5))
    .rect(lower_wing_length, lower_wing_width)
    .extrude(wing_thickness)
    .faces(">Z")
    .workplane()
    .circle(lower_wing_width/2)
    .extrude(wing_thickness)
    .faces("<Z")
    .workplane()
    .circle(lower_wing_width/2)
    .extrude(wing_thickness)
)

# Create struts
strut1 = (
    cq.Workplane("XY")
    .center(upper_wing_length/2 - 5, fuselage_radius + 5)
    .circle(strut_diameter/2)
    .extrude(-10)
)

strut2 = (
    cq.Workplane("XY")
    .center(-upper_wing_length/2 + 5, fuselage_radius + 5)
    .circle(strut_diameter/2)
    .extrude(-10)
)

strut3 = (
    cq.Workplane("XY")
    .center(upper_wing_length/2 - 5, -(fuselage_radius + 5))
    .circle(strut_diameter/2)
    .extrude(10)
)

strut4 = (
    cq.Workplane("XY")
    .center(-upper_wing_length/2 + 5, -(fuselage_radius + 5))
    .circle(strut_diameter/2)
    .extrude(10)
)

# Create tail section
tail = (
    cq.Workplane("XY")
    .center(fuselage_length/2 + tail_length/2, 0)
    .rect(tail_length, tail_width)
    .extrude(tail_height)
    .faces(">Z")
    .workplane()
    .rect(tail_length, tail_width/2)
    .extrude(tail_height)
)

# Create vertical stabilizer
vertical_stabilizer = (
    cq.Workplane("XY")
    .center(fuselage_length/2 + tail_length, 0)
    .rect(tail_length/3, tail_height)
    .extrude(tail_width)
)

# Create propeller
propeller_hub = cq.Workplane("XY").center(-fuselage_length/2, 0).circle(propeller_diameter/4).extrude(2)

# Create propeller blades
blade1 = (
    cq.Workplane("XY")
    .center(-fuselage_length/2, 0)
    .moveTo(-propeller_diameter/4, 0)
    .lineTo(-propeller_diameter/4, propeller_blade_length)
    .lineTo(-propeller_diameter/4 + propeller_blade_width, propeller_blade_length)
    .lineTo(-propeller_diameter/4 + propeller_blade_width, 0)
    .close()
    .extrude(2)
)

blade2 = (
    cq.Workplane("XY")
    .center(-fuselage_length/2, 0)
    .moveTo(-propeller_diameter/4, 0)
    .lineTo(-propeller_diameter/4, propeller_blade_length)
    .lineTo(-propeller_diameter/4 + propeller_blade_width, propeller_blade_length)
    .lineTo(-propeller_diameter/4 + propeller_blade_width, 0)
    .close()
    .extrude(2)
    .rotateAboutCenter((0, 0, 1), 120)
)

blade3 = (
    cq.Workplane("XY")
    .center(-fuselage_length/2, 0)
    .moveTo(-propeller_diameter/4, 0)
    .lineTo(-propeller_diameter/4, propeller_blade_length)
    .lineTo(-propeller_diameter/4 + propeller_blade_width, propeller_blade_length)
    .lineTo(-propeller_diameter/4 + propeller_blade_width, 0)
    .close()
    .extrude(2)
    .rotateAboutCenter((0, 0, 1), 240)
)

# Combine all parts
result = (
    fuselage
    .union(upper_wing)
    .union(lower_wing)
    .union(strut1)
    .union(strut2)
    .union(strut3)
    .union(strut4)
    .union(tail)
    .union(vertical_stabilizer)
    .union(propeller_hub)
    .union(blade1)
    .union(blade2)
    .union(blade3)
)

# Move the entire assembly to the origin
result = result.translate((-fuselage_length/2, 0, 0))