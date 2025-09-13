import cadquery as cq

# Define dimensions
width = 40.0
height = 20.0
thickness = 5.0
protrusion_diameter = 8.0
protrusion_height = 6.0
cutout_diameter = 4.0
central_axis_diameter = 6.0
rounding_radius = 2.0

# Create the base workplane
result = cq.Workplane("XY")

# Create the top section
top_section = (
    cq.Workplane("XY")
    .box(width, height, thickness)
    .edges("|Z")
    .fillet(rounding_radius)
)

# Add the cylindrical protrusion to the top section
top_protrusion = (
    top_section
    .faces(">Z")
    .workplane()
    .center(-width/4, 0)
    .circle(protrusion_diameter/2)
    .extrude(protrusion_height)
)

# Add the central axis
central_axis = (
    top_protrusion
    .faces(">Z")
    .workplane()
    .center(-width/4, 0)
    .circle(central_axis_diameter/2)
    .extrude(protrusion_height + thickness)
)

# Add cutouts to the top section
top_cutouts = (
    central_axis
    .faces(">Z")
    .workplane()
    .center(-width/4, 0)
    .circle(protrusion_diameter/2)
    .extrude(protrusion_height)
    .faces(">Z")
    .workplane()
    .center(-width/4, 0)
    .circle(cutout_diameter/2)
    .cutThruAll()
)

# Add additional cutouts on the sides of the top section
top_side_cutouts = (
    top_cutouts
    .faces(">Y")
    .workplane()
    .center(-width/4, 0)
    .circle(cutout_diameter/2)
    .cutThruAll()
)

# Create the bottom section (mirror of the top)
bottom_section = (
    top_side_cutouts
    .mirror(mirrorPlane="XY", basePointVector=(0, 0, 0))
    .translate((0, 0, -thickness))
)

# Create the complete object by combining both sections
result = bottom_section.union(top_side_cutouts)

# Add the cylindrical protrusion to the bottom section
bottom_protrusion = (
    result
    .faces("<Z")
    .workplane()
    .center(-width/4, 0)
    .circle(protrusion_diameter/2)
    .extrude(protrusion_height)
)

# Add cutouts to the bottom section
bottom_cutouts = (
    bottom_protrusion
    .faces("<Z")
    .workplane()
    .center(-width/4, 0)
    .circle(cutout_diameter/2)
    .cutThruAll()
)

# Add side cutouts to the bottom section
final_result = (
    bottom_cutouts
    .faces("<Y")
    .workplane()
    .center(-width/4, 0)
    .circle(cutout_diameter/2)
    .cutThruAll()
)

# Ensure the final result is correct
result = final_result