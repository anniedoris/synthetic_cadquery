import cadquery as cq

# Dimensions for the larger rectangular prism (beam/block)
large_length = 100.0
large_width = 20.0
large_height = 20.0

# Dimensions for the smaller object (bracket/support)
small_length = 40.0
small_width = 30.0
small_height = 15.0

# Create the larger rectangular prism (beam)
large_object = cq.Workplane("XY").box(large_length, large_width, large_height)

# Create the smaller object (bracket)
# Start with the main body
small_object = cq.Workplane("XY").box(small_length, small_width, small_height)

# Add rectangular cutout on one face
cutout_length = 20.0
cutout_width = 10.0
small_object = (
    small_object.faces(">Z")
    .workplane()
    .rect(cutout_length, cutout_width)
    .cutThruAll()
)

# Add smaller notch/cutout on adjacent face
notch_length = 8.0
notch_width = 5.0
small_object = (
    small_object.faces(">Y")
    .workplane(offset=-small_height/2 + 2)
    .rect(notch_length, notch_width)
    .cutThruAll()
)

# Add two protruding cylinders (peg features) on top face
peg_diameter = 4.0
peg_offset_x = 10.0
peg_offset_y = 5.0

small_object = (
    small_object.faces(">Z")
    .workplane()
    .center(peg_offset_x, peg_offset_y)
    .circle(peg_diameter/2)
    .extrude(5.0)
    .faces(">Z")
    .workplane()
    .center(-2*peg_offset_x, -2*peg_offset_y)
    .circle(peg_diameter/2)
    .extrude(5.0)
)

# Position the smaller object near the larger one
# Place it at one end of the larger object
result = large_object.union(small_object.translate((large_length/2 + small_length/2, 0, 0)))