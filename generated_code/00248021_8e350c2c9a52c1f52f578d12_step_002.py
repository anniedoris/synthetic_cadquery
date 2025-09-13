import cadquery as cq

# Define dimensions
outer_width = 20.0
outer_height = 10.0
thickness = 2.0
length = 50.0

# Create the outer rectangular prism
outer_box = cq.Workplane("XY").box(outer_width, outer_height, length)

# Create the inner hollow portion (subtract this from outer)
inner_width = outer_width - 2 * thickness
inner_height = outer_height - 2 * thickness
inner_box = cq.Workplane("XY").box(inner_width, inner_height, length)

# Subtract the inner box from the outer box to create the hollow section
hollow_section = outer_box.cut(inner_box)

# Remove one face to create the U-shaped open end
# We'll remove the front face (the one facing the user)
result = hollow_section.faces(">Z").workplane().rect(outer_width, outer_height).cutThruAll()

# Actually, let me reconsider. We want one end open, so we should remove a face from one end
# Let's remove the front face (the one with the highest Z coordinate) to create the U-shape
result = hollow_section.faces(">Z").workplane().rect(outer_width, outer_height).cutThruAll()