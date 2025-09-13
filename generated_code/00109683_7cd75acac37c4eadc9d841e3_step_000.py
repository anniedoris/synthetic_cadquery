import cadquery as cq

# Dimensions
length = 80.0
width = 60.0
thickness = 10.0
large_hole_dia = 20.0
large_recess_dia = 25.0
small_hole_dia = 10.0
small_recess_dia = 12.0
protrusion_width = 20.0
protrusion_height = 15.0
protrusion_depth = 25.0
counter_sink_dia = 6.0
counter_sink_depth = 2.0

# Create the base L-shaped bracket
result = cq.Workplane("XY").box(length, width, thickness)

# Create the large through-hole on the left side
result = (
    result.faces(">Z")
    .workplane()
    .moveTo(-length/2 + 30, 0)
    .circle(large_hole_dia/2)
    .cutThruAll()
)

# Create the large recess around the hole
result = (
    result.faces(">Z")
    .workplane()
    .moveTo(-length/2 + 30, 0)
    .circle(large_recess_dia/2)
    .cutBlind(-thickness)
)

# Add countersunk holes around the large hole
# Place 4 countersunk holes evenly around the large hole
hole_positions = [
    (-length/2 + 30, large_recess_dia/2 + 5),
    (-length/2 + 30, -large_recess_dia/2 - 5),
    (large_recess_dia/2 + 5, 0),
    (-large_recess_dia/2 - 5, 0)
]

for x, y in hole_positions:
    result = (
        result.faces(">Z")
        .workplane()
        .moveTo(x, y)
        .cskHole(counter_sink_dia/2, counter_sink_dia, counter_sink_depth)
    )

# Create the smaller through-hole on the right side
result = (
    result.faces(">Z")
    .workplane()
    .moveTo(length/2 - 30, 0)
    .circle(small_hole_dia/2)
    .cutThruAll()
)

# Create the smaller recess around the hole
result = (
    result.faces(">Z")
    .workplane()
    .moveTo(length/2 - 30, 0)
    .circle(small_recess_dia/2)
    .cutBlind(-thickness)
)

# Add countersunk holes around the small hole
small_hole_positions = [
    (length/2 - 30, small_recess_dia/2 + 5),
    (length/2 - 30, -small_recess_dia/2 - 5),
    (small_recess_dia/2 + 5, 0),
    (-small_recess_dia/2 - 5, 0)
]

for x, y in small_hole_positions:
    result = (
        result.faces(">Z")
        .workplane()
        .moveTo(x, y)
        .cskHole(counter_sink_dia/2, counter_sink_dia, counter_sink_depth)
    )

# Create the rectangular protrusion on the right side
# Move to the right side and create the protrusion
result = (
    result.faces(">X")
    .workplane(offset=thickness/2)
    .moveTo(0, 0)
    .rect(protrusion_width, protrusion_height)
    .extrude(protrusion_depth)
)

# Create the hole in the protrusion
result = (
    result.faces(">Z")
    .workplane(offset=protrusion_depth/2)
    .moveTo(length/2 - 30, 0)
    .circle(small_hole_dia/2)
    .cutThruAll()
)

# Add countersunk holes on top of the protrusion
protrusion_top_positions = [
    (length/2 - 30 - 5, protrusion_height/2 - 5),
    (length/2 - 30 + 5, protrusion_height/2 - 5),
    (length/2 - 30 - 5, -protrusion_height/2 + 5),
    (length/2 - 30 + 5, -protrusion_height/2 + 5)
]

for x, y in protrusion_top_positions:
    result = (
        result.faces(">Z")
        .workplane(offset=protrusion_depth)
        .moveTo(x, y)
        .cskHole(counter_sink_dia/2, counter_sink_dia, counter_sink_depth)
    )

# Add a flat surface on top of the protrusion
result = (
    result.faces(">Z")
    .workplane(offset=protrusion_depth)
    .moveTo(length/2 - 30, 0)
    .rect(10, 10, forConstruction=True)
    .vertices()
    .hole(2.0)
)

result = result