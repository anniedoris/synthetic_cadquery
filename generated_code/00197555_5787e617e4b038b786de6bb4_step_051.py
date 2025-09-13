import cadquery as cq
from math import pi, cos, sin

# Parameters
base_diameter = 40.0
base_height = 10.0
groove_depth = 1.0
groove_count = 8
groove_width = 2.0
secondary_diameter = 15.0
secondary_height = 20.0
secondary_offset = 10.0
rect_width = 8.0
rect_height = 12.0
rect_depth = 5.0
protrusion_diameter = 4.0
protrusion_height = 3.0

# Create the main cylindrical base
result = cq.Workplane("XY").circle(base_diameter/2).extrude(base_height)

# Create grooves on the base
groove_angle = 2 * pi / groove_count
for i in range(groove_count):
    angle = i * groove_angle
    x = (base_diameter/2 - groove_depth) * cos(angle)
    y = (base_diameter/2 - groove_depth) * sin(angle)
    result = result.faces(">Z").workplane(offset=base_height/2).moveTo(x, y).rect(groove_width, groove_depth*2, forConstruction=True).vertices().hole(groove_depth)

# Create the center bore
result = result.faces(">Z").workplane().circle(base_diameter/4).cutThruAll()

# Create the flat bottom with lip
result = result.faces("<Z").workplane().rect(base_diameter, base_diameter, forConstruction=True).vertices().hole(base_diameter/2 - 2)

# Create the secondary cylinder
result = (
    result.faces(">Z")
    .workplane(offset=base_height/2)
    .moveTo(secondary_offset, 0)
    .circle(secondary_diameter/2)
    .extrude(secondary_height)
)

# Create grooves on the secondary cylinder
for i in range(groove_count):
    angle = i * groove_angle
    x = secondary_diameter/2 * cos(angle)
    y = secondary_diameter/2 * sin(angle)
    result = result.faces(">Z").workplane(offset=secondary_height/2).moveTo(x, y).rect(groove_width, groove_depth*2, forConstruction=True).vertices().hole(groove_depth)

# Create the flat end surface with lip
result = result.faces(">Z").workplane().rect(secondary_diameter, secondary_diameter, forConstruction=True).vertices().hole(secondary_diameter/2 - 2)

# Create the rectangular section
result = (
    result.faces(">Z")
    .workplane(offset=secondary_height/2)
    .moveTo(secondary_offset + secondary_diameter/2, 0)
    .rect(rect_width, rect_height)
    .extrude(rect_depth)
)

# Create the overhang on the rectangular section
result = result.faces(">Z").workplane(offset=rect_depth/2).rect(rect_width/2, rect_height, forConstruction=True).vertices().hole(1)

# Create the cylindrical protrusion
result = (
    result.faces(">Z")
    .workplane(offset=rect_depth/2)
    .moveTo(secondary_offset + secondary_diameter/2 + rect_width/2, 0)
    .circle(protrusion_diameter/2)
    .extrude(protrusion_height)
)

# Add a slight overhang to the end of the protrusion
result = result.faces(">Z").workplane(offset=protrusion_height/2).circle(protrusion_diameter/2 - 0.5).extrude(0.5)