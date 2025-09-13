import cadquery as cq

# Define dimensions
total_length = 50.0
bore_diameter = 8.0
front_face_diameter = 20.0
flange1_diameter = 25.0
flange2_diameter = 22.0
flange3_diameter = 18.0
back_ring_diameter = 30.0
back_protrusion_diameter = 6.0
back_protrusion_length = 10.0
indentation_diameter = 3.0
indentation_depth = 2.0

# Create the main body
result = cq.Workplane("XY").box(total_length, total_length, total_length)

# Create the central bore
result = result.faces(">Z").workplane().circle(bore_diameter/2).cutThruAll()

# Create the main body with flanges
# Start with the front face
result = (
    cq.Workplane("XY")
    .box(total_length, total_length, total_length)
    .faces(">Z")
    .workplane()
    .circle(bore_diameter/2)
    .cutThruAll()
)

# Create the front face with central hole and indentations
result = (
    result.faces(">Z")
    .workplane()
    .circle(front_face_diameter/2)
    .extrude(1.0)
    .faces(">Z")
    .workplane()
    .circle(bore_diameter/2)
    .cutThruAll()
    .faces(">Z")
    .workplane()
    .pushPoints([(-3.0, 0), (3.0, 0)])
    .circle(indentation_diameter/2)
    .cutBlind(-indentation_depth)
)

# Create the flanges
# Flange 1 (largest)
result = (
    result.faces("<Z")
    .workplane(offset=-5.0)
    .circle(flange1_diameter/2)
    .extrude(5.0)
)

# Flange 2 
result = (
    result.faces("<Z")
    .workplane(offset=-5.0)
    .circle(flange2_diameter/2)
    .extrude(5.0)
)

# Flange 3 (smallest)
result = (
    result.faces("<Z")
    .workplane(offset=-5.0)
    .circle(flange3_diameter/2)
    .extrude(5.0)
)

# Create the back end with ring and protrusion
# Back ring
result = (
    result.faces("<Z")
    .workplane(offset=-5.0)
    .circle(back_ring_diameter/2)
    .extrude(5.0)
)

# Back protrusion (off-center)
result = (
    result.faces("<Z")
    .workplane(offset=-5.0)
    .moveTo(back_ring_diameter/2 - back_protrusion_diameter - 2.0, 0)
    .circle(back_protrusion_diameter/2)
    .extrude(back_protrusion_length)
)

# Clean up to get the final shape
result = result.faces(">Z").workplane().circle(bore_diameter/2).cutThruAll()
result = result.faces("<Z").workplane().circle(back_ring_diameter/2).cutThruAll()

# Let's rebuild this more carefully
result = cq.Workplane("XY").box(total_length, total_length, total_length)

# Create the central bore
result = result.faces(">Z").workplane().circle(bore_diameter/2).cutThruAll()

# Create the main body with flanges
# Front face
result = result.faces(">Z").workplane().circle(front_face_diameter/2).extrude(2.0)

# First flange (largest)
result = result.faces("<Z").workplane(offset=-5.0).circle(flange1_diameter/2).extrude(5.0)

# Second flange
result = result.faces("<Z").workplane(offset=-5.0).circle(flange2_diameter/2).extrude(5.0)

# Third flange (smallest)
result = result.faces("<Z").workplane(offset=-5.0).circle(flange3_diameter/2).extrude(5.0)

# Back ring
result = result.faces("<Z").workplane(offset=-5.0).circle(back_ring_diameter/2).extrude(5.0)

# Back protrusion (off-center)
result = result.faces("<Z").workplane(offset=-5.0).moveTo(back_ring_diameter/2 - back_protrusion_diameter - 2.0, 0).circle(back_protrusion_diameter/2).extrude(back_protrusion_length)

# Create the central hole in the front face
result = result.faces(">Z").workplane().circle(bore_diameter/2).cutBlind(-2.0)

# Create the indentations
result = result.faces(">Z").workplane().pushPoints([(-3.0, 0), (3.0, 0)]).circle(indentation_diameter/2).cutBlind(-indentation_depth)

# Final clean up to ensure proper geometry
result = result.faces(">Z").workplane().circle(bore_diameter/2).cutThruAll()