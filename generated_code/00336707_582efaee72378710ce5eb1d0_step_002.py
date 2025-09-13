import cadquery as cq

# Define dimensions
length = 100.0
width = 30.0
height = 20.0
cylinder_radius = 8.0
cylinder_length = 20.0
joint_radius = 6.0
rod_radius = 3.0
rod_length = 40.0
cutout_radius = 4.0
cutout_depth = 8.0

# Create the left main section
left_section = (
    cq.Workplane("XY")
    .box(length/2, width, height)
    .faces(">X")
    .workplane()
    .circle(cylinder_radius)
    .extrude(cylinder_length)
    .faces(">X")
    .workplane()
    .circle(cylinder_radius)
    .extrude(cylinder_length)
    .faces(">X")
    .workplane()
    .rect(cylinder_radius*2, cylinder_radius*2)
    .cutBlind(-cylinder_length)
    .faces("<X")
    .workplane()
    .rect(cylinder_radius*2, cylinder_radius*2)
    .cutBlind(-cylinder_length)
)

# Create the right main section
right_section = (
    cq.Workplane("XY")
    .box(length/2, width, height)
    .faces("<X")
    .workplane()
    .circle(cylinder_radius)
    .extrude(cylinder_length)
    .faces("<X")
    .workplane()
    .circle(cylinder_radius)
    .extrude(cylinder_length)
    .faces("<X")
    .workplane()
    .rect(cylinder_radius*2, cylinder_radius*2)
    .cutBlind(-cylinder_length)
    .faces(">X")
    .workplane()
    .rect(cylinder_radius*2, cylinder_radius*2)
    .cutBlind(-cylinder_length)
)

# Create the central joint
joint = (
    cq.Workplane("XY")
    .box(length/4, width, height)
    .faces(">Z")
    .workplane()
    .circle(joint_radius)
    .extrude(10)
    .faces("<Z")
    .workplane()
    .circle(joint_radius)
    .extrude(10)
    .faces(">Z")
    .workplane()
    .rect(joint_radius*2, joint_radius*2)
    .cutBlind(-10)
    .faces("<Z")
    .workplane()
    .rect(joint_radius*2, joint_radius*2)
    .cutBlind(-10)
)

# Create connecting rods
rod1 = (
    cq.Workplane("XY")
    .box(rod_length, rod_radius*2, rod_radius*2)
    .faces(">X")
    .workplane()
    .circle(rod_radius)
    .extrude(10)
    .faces("<X")
    .workplane()
    .circle(rod_radius)
    .extrude(10)
    .faces(">X")
    .workplane()
    .rect(rod_radius*2, rod_radius*2)
    .cutBlind(-10)
    .faces("<X")
    .workplane()
    .rect(rod_radius*2, rod_radius*2)
    .cutBlind(-10)
)

# Position and combine the components
result = (
    left_section
    .union(right_section)
    .union(joint)
    .union(rod1)
    .translate((-length/4, 0, 0))
)

# Add internal cutouts to main sections
result = (
    result
    .faces("<X")
    .workplane()
    .circle(cutout_radius)
    .cutBlind(-cutout_depth)
    .faces(">X")
    .workplane()
    .circle(cutout_radius)
    .cutBlind(-cutout_depth)
    .faces("<Y")
    .workplane()
    .circle(cutout_radius)
    .cutBlind(-cutout_depth)
    .faces(">Y")
    .workplane()
    .circle(cutout_radius)
    .cutBlind(-cutout_depth)
)

# Add fillets to edges
result = result.edges("|Z").fillet(2.0)