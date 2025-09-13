import cadquery as cq

# Define dimensions
length = 100.0
width = 20.0
thickness = 5.0
hole_diameter = 3.0
hole_spacing = 15.0
num_holes = 6
corner_radius = 2.0
protrusion_length = 10.0
protrusion_width = 8.0

# Create the base plate
result = cq.Workplane("XY").box(length, width, thickness)

# Round the corners
result = result.edges("|Z").fillet(corner_radius)

# Add holes in parallel rows
# Create a workplane for the top face
result = result.faces(">Z").workplane()

# Add holes along the length
for i in range(num_holes):
    x_pos = -length/2 + (i * hole_spacing) + hole_spacing/2
    result = result.center(x_pos, 0).circle(hole_diameter/2).cutThruAll()

# Add protrusion on one end
result = result.faces("<X").workplane(offset=-thickness/2).rect(protrusion_length, protrusion_width).extrude(thickness/2)

# Ensure the protrusion is properly connected
result = result.faces("<X").workplane(offset=-thickness/2).rect(protrusion_length, protrusion_width).extrude(thickness/2)

# Alternative approach for the protrusion - add it as a separate feature
# Create the main plate again to start fresh
result = cq.Workplane("XY").box(length, width, thickness)

# Round the corners
result = result.edges("|Z").fillet(corner_radius)

# Add holes
for i in range(num_holes):
    x_pos = -length/2 + (i * hole_spacing) + hole_spacing/2
    result = result.faces(">Z").workplane().center(x_pos, 0).circle(hole_diameter/2).cutThruAll()

# Add protrusion on one end (left side)
result = result.faces("<X").workplane(offset=thickness/2).rect(protrusion_length, protrusion_width).extrude(-thickness/2)

# Final result
result = result.faces("<X").workplane(offset=thickness/2).rect(protrusion_length, protrusion_width).extrude(-thickness/2)