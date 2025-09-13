import cadquery as cq

# Dimensions
base_length = 100.0
base_width = 60.0
base_height = 40.0
lid_thickness = 5.0
compartment1_width = 60.0
compartment2_width = 30.0
compartment_height = 30.0
cylinder_diameter = 10.0
cutout_width = 15.0
cutout_height = 20.0
screw_diameter = 3.0
screw_head_diameter = 6.0
side_cutout_width = 20.0
side_cutout_height = 15.0

# Create the base
result = cq.Workplane("XY").box(base_length, base_width, base_height)

# Create the lid
lid = cq.Workplane("XY").box(base_length, base_width, lid_thickness)

# Position the lid on top of the base
result = result.union(lid.translate((0, 0, base_height)))

# Create internal compartments
# Left compartment (larger)
compartment1 = cq.Workplane("XY").box(compartment1_width, base_width, compartment_height)
compartment1 = compartment1.translate(((base_length - compartment1_width) / 2, 0, base_height))

# Right compartment (smaller)
compartment2 = cq.Workplane("XY").box(compartment2_width, base_width, compartment_height)
compartment2 = compartment2.translate(((base_length - compartment2_width) / 2, 0, base_height))

# Cut out the compartments from the base
result = result.cut(compartment1)
result = result.cut(compartment2)

# Create cylindrical holder in right compartment
cylinder_holder = cq.Workplane("XY").circle(cylinder_diameter / 2).extrude(compartment_height)
cylinder_holder = cylinder_holder.translate(((base_length - compartment2_width) / 2 + compartment2_width - cylinder_diameter, 0, base_height))

# Cut out the cylinder holder
result = result.cut(cylinder_holder)

# Create rectangular cutout in right compartment
cutout = cq.Workplane("XY").rect(cutout_width, cutout_height).extrude(compartment_height)
cutout = cutout.translate(((base_length - compartment2_width) / 2 + compartment2_width - cutout_width, 0, base_height))

# Cut out the cutout
result = result.cut(cutout)

# Create side cutout on left side
left_side_cutout = cq.Workplane("YZ").rect(side_cutout_width, side_cutout_height).extrude(base_height)
left_side_cutout = left_side_cutout.translate((-base_length/2 + side_cutout_width/2, 0, base_height/2))

# Cut out the left side cutout
result = result.cut(left_side_cutout)

# Create vertical slots on right side
slot_width = 2.0
slot_height = 10.0
slot_spacing = 8.0
for i in range(4):
    slot = cq.Workplane("YZ").rect(slot_width, slot_height).extrude(base_height)
    slot = slot.translate((base_length/2 - slot_width/2, 0, base_height/2 + (i - 1.5) * slot_spacing))
    result = result.cut(slot)

# Create screw holes on top surface
# Front screws
result = (
    result.faces(">Z")
    .workplane()
    .center(-base_length/4, base_width/4)
    .circle(screw_head_diameter/2)
    .circle(screw_diameter/2)
    .extrude(lid_thickness)
)

result = (
    result.faces(">Z")
    .workplane()
    .center(base_length/4, base_width/4)
    .circle(screw_head_diameter/2)
    .circle(screw_diameter/2)
    .extrude(lid_thickness)
)

# Back screws
result = (
    result.faces(">Z")
    .workplane()
    .center(-base_length/4, -base_width/4)
    .circle(screw_head_diameter/2)
    .circle(screw_diameter/2)
    .extrude(lid_thickness)
)

result = (
    result.faces(">Z")
    .workplane()
    .center(base_length/4, -base_width/4)
    .circle(screw_head_diameter/2)
    .circle(screw_diameter/2)
    .extrude(lid_thickness)
)

# Create lid screw holes
result = (
    result.faces(">Z")
    .workplane()
    .center(-base_length/4, base_width/4)
    .circle(screw_head_diameter/2)
    .circle(screw_diameter/2)
    .extrude(lid_thickness)
)

result = (
    result.faces(">Z")
    .workplane()
    .center(base_length/4, base_width/4)
    .circle(screw_head_diameter/2)
    .circle(screw_diameter/2)
    .extrude(lid_thickness)
)

# Create the final object
result = result