import cadquery as cq

# Define dimensions
shaft_diameter = 6.0
shaft_length = 80.0
box_length = 12.0
box_width = 8.0
box_height = 6.0
cap_radius = 2.0
box_cutout_width = 4.0
box_cutout_height = 3.0

# Create the shaft with rounded ends
result = cq.Workplane("XY").circle(shaft_diameter/2).extrude(shaft_length)

# Add rounded caps at both ends
result = result.faces("<Z").workplane().circle(cap_radius).extrude(cap_radius)
result = result.faces(">Z").workplane().circle(cap_radius).extrude(cap_radius)

# Rotate the shaft to create the angle (30 degrees from vertical)
result = result.rotate((0, 0, 0), (1, 0, 0), 30)

# Position the box at one end of the shaft
# First create the box structure
box = cq.Workplane("XY").box(box_length, box_width, box_height)

# Create the hollow interior by cutting out a portion
box_hollow = (
    box.faces(">Z")
    .workplane()
    .rect(box_cutout_width, box_cutout_height)
    .cutBlind(-box_height)
)

# Position the box perpendicular to the shaft at the end
# The shaft is at an angle, so we need to properly orient the box
box = box_hollow.translate((0, 0, shaft_length/2 + box_height/2))

# Rotate and position the box properly
box = box.rotate((0, 0, 0), (0, 1, 0), 90)  # Rotate to align with shaft
box = box.translate((0, 0, shaft_length/2 + box_height/2))

# Combine the shaft and box
result = result.union(box)

# Ensure the final result is properly oriented
result = result.rotate((0, 0, 0), (1, 0, 0), -30)

# For better visualization, we'll also add a reference to the shaft's axis
# This is not necessary for the geometry but helps in understanding
result = result.faces(">Z").workplane().circle(shaft_diameter/2).extrude(2)

# Clean up and finalize
result = result.clean()