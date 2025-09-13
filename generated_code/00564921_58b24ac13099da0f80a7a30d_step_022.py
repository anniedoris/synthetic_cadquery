import cadquery as cq

# Define dimensions
base_length = 80.0
base_width = 40.0
base_thickness = 10.0
block_length = 30.0
block_width = 20.0
block_height = 25.0
hole_diameter = 6.0

# Create the base plate
result = cq.Workplane("XY").box(base_length, base_width, base_thickness)

# Add the circular hole near one corner
result = (
    result.faces(">Z")
    .workplane()
    .moveTo(-base_length/2 + 15, -base_width/2 + 15)
    .hole(hole_diameter)
)

# Add the protruding block
# Position the block on the top face of the base plate
result = (
    result.faces(">Z")
    .workplane(offset=base_thickness)
    .moveTo(0, -base_width/2 + block_width/2)
    .box(block_length, block_width, block_height)
)

# Rotate the entire assembly to give it the angled orientation described
result = result.rotate((0, 0, 0), (0, 0, 1), 15)