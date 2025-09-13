import cadquery as cq

# Dimensions
length = 100.0
width = 60.0
height = 40.0
thickness = 3.0
door_width = 50.0
door_height = 30.0
hinge_width = 5.0
latch_width = 4.0
latch_height = 8.0
lip_depth = 5.0
foot_height = 5.0
foot_width = 10.0

# Create the main body
result = cq.Workplane("XY").box(length, width, height)

# Create the front lip
front_lip = (
    cq.Workplane("XY")
    .box(length + lip_depth, width, thickness)
    .translate((lip_depth/2, 0, height - thickness))
)
result = result.union(front_lip)

# Create the recessed front panel for the door
recess_depth = 2.0
door_recess = (
    cq.Workplane("XY")
    .box(door_width, width, recess_depth)
    .translate(((length - door_width)/2, 0, height - recess_depth))
)
result = result.cut(door_recess)

# Create the door
door = (
    cq.Workplane("XY")
    .box(door_width, width, thickness)
    .translate(((length - door_width)/2, 0, height - thickness))
)
result = result.union(door)

# Create the hinge on the right side of the door
hinge_x = (length + door_width)/2 - hinge_width/2
hinge_y = width/2
hinge = (
    cq.Workplane("XY")
    .box(hinge_width, 2, 3)
    .translate((hinge_x, hinge_y, height - thickness + 1))
)
result = result.union(hinge)

# Create the hinge pin (metal rod)
hinge_pin = (
    cq.Workplane("XY")
    .circle(1.5)
    .extrude(2)
    .translate((hinge_x + hinge_width/2, hinge_y, height - thickness + 1))
)
result = result.union(hinge_pin)

# Create the latch on the left side of the door
latch_x = (length - door_width)/2 - latch_width/2
latch_y = width/2
latch = (
    cq.Workplane("XY")
    .box(latch_width, 2, 3)
    .translate((latch_x, latch_y, height - thickness + 1))
)
result = result.union(latch)

# Create the latch mechanism (flip mechanism)
latch_flip = (
    cq.Workplane("XY")
    .box(2, 2, 2)
    .translate((latch_x + latch_width/2, latch_y, height - thickness + 3))
)
result = result.union(latch_flip)

# Create small rectangular cutouts on the door (for ventilation, labeling, or mounting)
cutout_width = 8.0
cutout_height = 4.0
cutout_x = (length - door_width)/2 + 10
cutout_y = width/2
cutout = (
    cq.Workplane("XY")
    .box(cutout_width, 2, 2)
    .translate((cutout_x, cutout_y, height - thickness + 1))
)
result = result.cut(cutout)

# Create the bottom foot on the left side
foot_x = (length - door_width)/2 - foot_width/2
foot_y = -foot_width/2
foot = (
    cq.Workplane("XY")
    .box(foot_width, foot_width, foot_height)
    .translate((foot_x, foot_y, 0))
)
result = result.union(foot)

# Create small rectangular cutouts on the door near the top (ventilation, labeling, mounting)
cutout2_x = (length - door_width)/2 + 30
cutout2 = (
    cq.Workplane("XY")
    .box(cutout_width, 2, 2)
    .translate((cutout2_x, cutout_y, height - thickness + 1))
)
result = result.cut(cutout2)

# Create the door frame to make the recessed area more visible
frame_thickness = 1.0
door_frame = (
    cq.Workplane("XY")
    .box(door_width + 2*frame_thickness, width, frame_thickness)
    .translate(((length - door_width)/2 - frame_thickness, 0, height - frame_thickness))
)
result = result.union(door_frame)

# Remove the inner part of the frame to create the actual door recess
frame_recess = (
    cq.Workplane("XY")
    .box(door_width, width, frame_thickness)
    .translate(((length - door_width)/2, 0, height - frame_thickness))
)
result = result.cut(frame_recess)

# Final result
result = result