import cadquery as cq

# Define dimensions
length = 100.0
width = 60.0
height = 20.0
thickness = 5.0

# Side protrusion dimensions
side_protrusion_length = 15.0
side_protrusion_width = 10.0
side_protrusion_height = 15.0

# End protrusion dimensions
end_protrusion_length = 20.0
end_protrusion_width = 12.0
end_protrusion_height = 12.0

# Cutout dimensions
cutout_diameter = 10.0
cutout_radius = cutout_diameter / 2.0

# Create the main base
result = cq.Workplane("XY").box(length, width, thickness)

# Add the top surface (extruded from the base)
result = result.faces(">Z").workplane().box(length, width, height - thickness)

# Add side protrusions
# Left side protrusion
result = (
    result.faces("<X")
    .workplane(offset=thickness)
    .rect(side_protrusion_length, side_protrusion_width)
    .extrude(side_protrusion_height)
)

# Right side protrusion
result = (
    result.faces(">X")
    .workplane(offset=thickness)
    .rect(side_protrusion_length, side_protrusion_width)
    .extrude(side_protrusion_height)
)

# Add end protrusion at one end
result = (
    result.faces("<Y")
    .workplane(offset=thickness)
    .rect(end_protrusion_length, end_protrusion_width)
    .extrude(end_protrusion_height)
)

# Add semi-circular cutouts on the sides
# Left cutout
result = (
    result.faces("<X")
    .workplane(offset=thickness + 2)
    .center(-length/2 + cutout_radius + 5, 0)
    .circle(cutout_radius)
    .cutThruAll()
)

# Right cutout
result = (
    result.faces(">X")
    .workplane(offset=thickness + 2)
    .center(length/2 - cutout_radius - 5, 0)
    .circle(cutout_radius)
    .cutThruAll()
)

# Add fillets to edges for a more realistic appearance
result = result.edges("|Z").fillet(2.0)