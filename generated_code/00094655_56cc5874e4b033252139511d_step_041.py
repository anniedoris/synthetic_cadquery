import cadquery as cq

# Define dimensions
block_length = 40.0
block_width = 20.0
block_height = 10.0
recess_length = 12.0
recess_width = 8.0
recess_depth = 3.0
cylinder_diameter = 8.0
cylinder_height = 6.0
hole_diameter = 4.0
mounting_hole_offset = 15.0
mounting_hole_depth = 8.0

# Create the first rectangular block
block1 = (
    cq.Workplane("XY")
    .box(block_length, block_width, block_height)
    .faces(">Z")
    .workplane()
    .rect(recess_length, recess_width, forConstruction=True)
    .vertices()
    .hole(recess_depth)
    .faces(">Z")
    .workplane()
    .circle(hole_diameter/2)
    .cutBlind(-mounting_hole_depth)
    .faces("<Y")
    .workplane()
    .circle(hole_diameter/2)
    .cutBlind(-mounting_hole_depth)
    .faces(">Y")
    .workplane()
    .circle(hole_diameter/2)
    .cutBlind(-mounting_hole_depth)
)

# Create the second rectangular block (mirror of the first)
block2 = block1.mirror(mirrorPlane="YZ", basePointVector=(0, 0, 0))

# Create the central cylindrical joint
joint = (
    cq.Workplane("XY")
    .circle(cylinder_diameter/2)
    .extrude(cylinder_height)
    .faces(">Z")
    .workplane()
    .rect(cylinder_diameter, cylinder_diameter, forConstruction=True)
    .vertices()
    .hole(2.0)
)

# Position the blocks and joint
result = block1.translate((0, 0, 0))
result = result.union(block2.translate((0, 0, 0)))

# Add the joint in the center
joint_pos = (0, 0, block_height/2 + cylinder_height/2)
result = result.union(joint.translate(joint_pos))

# Add additional features to the joint
result = (
    result.faces(">Z")
    .workplane()
    .rect(cylinder_diameter, cylinder_diameter, forConstruction=True)
    .vertices()
    .hole(2.0)
)

# Make the joint flat on top to fit into the recess
result = (
    result.faces(">Z")
    .workplane()
    .rect(recess_length, recess_width)
    .cutBlind(-recess_depth)
)