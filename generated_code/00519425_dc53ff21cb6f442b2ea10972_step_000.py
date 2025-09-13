import cadquery as cq

# Define dimensions
length = 100.0
width = 60.0
height = 20.0
thickness = 5.0

# Create the base box
result = cq.Workplane("XY").box(length, width, height)

# Create the inner cutout to make it an open-top container with walls of uniform thickness
# We need to cut out a smaller box from the inside
inner_length = length - 2 * thickness
inner_width = width - 2 * thickness
inner_height = height

# Cut out the inner volume to create the walls
result = result.faces(">Z").workplane().rect(inner_length, inner_width).extrude(inner_height)