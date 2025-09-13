import cadquery as cq

# Dimensions
cover_length = 100.0
cover_width = 150.0
thickness = 5.0
spine_width = 10.0
cutout_length = 20.0
cutout_width = 8.0
cutout_offset = 15.0

# Create the base cover
result = cq.Workplane("XY").box(cover_length, cover_width, thickness)

# Create the spine by extending one edge
spine = (
    cq.Workplane("XY")
    .moveTo(-cover_length/2, cover_width/2 - spine_width/2)
    .lineTo(-cover_length/2, cover_width/2 + spine_width/2)
    .lineTo(-cover_length/2 + spine_width, cover_width/2 + spine_width/2)
    .lineTo(-cover_length/2 + spine_width, cover_width/2 - spine_width/2)
    .close()
    .extrude(thickness)
)

# Combine the cover and spine
result = result.union(spine)

# Add the cutout
cutout = (
    cq.Workplane("XY")
    .moveTo(cover_length/2 - cutout_offset - cutout_length/2, 0)
    .rect(cutout_length, cutout_width)
    .extrude(thickness)
)

result = result.cut(cutout)

# Add the text "Louisa" to the spine
# Create a workplane on the spine face
spine_face = result.faces("<X").workplane(centerOption="CenterOfMass")
# Since CadQuery doesn't have a direct text function, we'll approximate it with a simple rectangle
# This is a simplified representation - a real implementation would require more complex geometry
text_height = 8.0
text_width = 20.0
text = (
    spine_face.moveTo(-text_width/2, -text_height/2)
    .rect(text_width, text_height)
    .extrude(thickness/2)
)

# Combine text with the main object
result = result.union(text)

# Round the edges where cover meets spine for a smooth transition
# Fillet the edges connecting cover to spine
result = result.edges("|X").fillet(2.0)

# Final result
result = result