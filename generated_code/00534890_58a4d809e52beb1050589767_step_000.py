import cadquery as cq

# Define dimensions
outer_diameter = 20.0
inner_diameter = 12.0
length = 30.0
wall_thickness = (outer_diameter - inner_diameter) / 2

# Create the tilted tube
# Start with a workplane at an angle
result = (
    cq.Workplane("XY")
    .center(0, 0)
    .circle(outer_diameter/2)
    .extrude(length)
    .faces(">Z")
    .workplane()
    .circle(inner_diameter/2)
    .extrude(length)
    .faces("<Z")
    .workplane()
    .circle(outer_diameter/2)
    .extrude(length)
    .faces("<Z")
    .workplane()
    .circle(inner_diameter/2)
    .extrude(length)
    .cut(cq.Workplane("XY").center(0, 0).circle(inner_diameter/2).extrude(length))
    .rotate((0, 0, 0), (1, 1, 0), 30)
)

# More precise approach using a single cylinder with shell
result = (
    cq.Workplane("XY")
    .circle(outer_diameter/2)
    .extrude(length)
    .faces(">Z")
    .workplane()
    .circle(inner_diameter/2)
    .extrude(length)
    .cut(cq.Workplane("XY").center(0, 0).circle(inner_diameter/2).extrude(length))
    .rotate((0, 0, 0), (1, 1, 0), 30)
)

# Even better approach - create the tube directly
result = (
    cq.Workplane("XY")
    .circle(outer_diameter/2)
    .extrude(length)
    .shell(-wall_thickness)
    .rotate((0, 0, 0), (1, 1, 0), 30)
)