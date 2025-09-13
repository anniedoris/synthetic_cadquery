import cadquery as cq

# Define dimensions
length = 100.0
width = 60.0
height = 40.0
thickness = 3.0

# Create the main box
result = cq.Workplane("XY").box(length, width, height)

# Create the front panel with cutouts
# Large center cutout
front_cutout_width = 60.0
front_cutout_height = 30.0
result = (
    result.faces(">Z")
    .workplane()
    .center(0, 0)
    .rect(front_cutout_width, front_cutout_height)
    .cutThruAll()
)

# Small cutout above the large cutout
small_cutout_width = 20.0
small_cutout_height = 10.0
result = (
    result.faces(">Z")
    .workplane()
    .center(0, front_cutout_height/2 + small_cutout_height/2 + 5)
    .rect(small_cutout_width, small_cutout_height)
    .cutThruAll()
)

# Add holes on front panel edges
hole_diameter = 2.0
# Top edge holes
result = (
    result.faces(">Z")
    .workplane()
    .center(-front_cutout_width/2 + 10, width/2 - 5)
    .circle(hole_diameter/2)
    .cutThruAll()
)
result = (
    result.faces(">Z")
    .workplane()
    .center(front_cutout_width/2 - 10, width/2 - 5)
    .circle(hole_diameter/2)
    .cutThruAll()
)

# Bottom edge holes
result = (
    result.faces(">Z")
    .workplane()
    .center(-front_cutout_width/2 + 10, -width/2 + 5)
    .circle(hole_diameter/2)
    .cutThruAll()
)
result = (
    result.faces(">Z")
    .workplane()
    .center(front_cutout_width/2 - 10, -width/2 + 5)
    .circle(hole_diameter/2)
    .cutThruAll()
)

# Side panels - add holes in grid pattern
side_hole_spacing_x = 15.0
side_hole_spacing_y = 15.0
side_hole_count_x = 4
side_hole_count_y = 3

# Left side panel holes
for i in range(side_hole_count_x):
    for j in range(side_hole_count_y):
        x_pos = -length/2 + 5 + i * side_hole_spacing_x
        y_pos = -width/2 + 5 + j * side_hole_spacing_y
        result = (
            result.faces("<X")
            .workplane()
            .center(x_pos, y_pos)
            .circle(hole_diameter/2)
            .cutThruAll()
        )

# Right side panel holes
for i in range(side_hole_count_x):
    for j in range(side_hole_count_y):
        x_pos = length/2 - 5 - i * side_hole_spacing_x
        y_pos = -width/2 + 5 + j * side_hole_spacing_y
        result = (
            result.faces(">X")
            .workplane()
            .center(x_pos, y_pos)
            .circle(hole_diameter/2)
            .cutThruAll()
        )

# Right side panel has a cutout near bottom
cutout_width = 20.0
cutout_height = 15.0
result = (
    result.faces(">X")
    .workplane()
    .center(0, -width/2 + cutout_height/2 + 5)
    .rect(cutout_width, cutout_height)
    .cutThruAll()
)

# Back panel with cutouts
# Large center cutout
back_cutout_width = 60.0
back_cutout_height = 30.0
result = (
    result.faces("<Z")
    .workplane()
    .center(0, 0)
    .rect(back_cutout_width, back_cutout_height)
    .cutThruAll()
)

# Add holes on back panel edges
# Top edge holes
result = (
    result.faces("<Z")
    .workplane()
    .center(-back_cutout_width/2 + 10, width/2 - 5)
    .circle(hole_diameter/2)
    .cutThruAll()
)
result = (
    result.faces("<Z")
    .workplane()
    .center(back_cutout_width/2 - 10, width/2 - 5)
    .circle(hole_diameter/2)
    .cutThruAll()
)

# Bottom edge holes
result = (
    result.faces("<Z")
    .workplane()
    .center(-back_cutout_width/2 + 10, -width/2 + 5)
    .circle(hole_diameter/2)
    .cutThruAll()
)
result = (
    result.faces("<Z")
    .workplane()
    .center(back_cutout_width/2 - 10, -width/2 + 5)
    .circle(hole_diameter/2)
    .cutThruAll()
)

# Add slight overhang to top panel
result = (
    result.faces(">Z")
    .workplane()
    .center(0, -width/2 + 10)
    .rect(length - 5, 5)
    .extrude(1.5)
)

# Create angled front and back panels (simulated by removing some material)
# This gives a trapezoidal appearance from the side
result = (
    result.faces(">Z")
    .workplane()
    .center(0, width/2 - 10)
    .rect(length - 10, 10)
    .cutBlind(-5)
)

result = (
    result.faces("<Z")
    .workplane()
    .center(0, -width/2 + 10)
    .rect(length - 10, 10)
    .cutBlind(5)
)

# Add mounting holes to top and bottom panels
top_bottom_hole_positions = [
    (-length/2 + 10, -width/2 + 10),
    (length/2 - 10, -width/2 + 10),
    (-length/2 + 10, width/2 - 10),
    (length/2 - 10, width/2 - 10)
]

for x_pos, y_pos in top_bottom_hole_positions:
    result = (
        result.faces(">Z")
        .workplane()
        .center(x_pos, y_pos)
        .circle(hole_diameter/2)
        .cutThruAll()
    )
    result = (
        result.faces("<Z")
        .workplane()
        .center(x_pos, y_pos)
        .circle(hole_diameter/2)
        .cutThruAll()
    )

# Add a small lip on the front panel for protection or aesthetics
result = (
    result.faces(">Z")
    .workplane()
    .center(0, width/2 - 5)
    .rect(length - 5, 3)
    .extrude(1.0)
)