import cadquery as cq

# Define dimensions
length = 100.0
width = 60.0
height = 40.0
thickness = 3.0
handle_length = 20.0
handle_width = 8.0
handle_radius = 2.0
mount_hole_diameter = 4.0

# Create the main box
result = cq.Workplane("XY").box(length, width, height)

# Create the hollow interior
result = result.faces(">Z").workplane().rect(length - 2*thickness, width - 2*thickness).extrude(height - 2*thickness)

# Create handles on top face
# Left handle
result = (
    result.faces(">Z")
    .workplane()
    .moveTo(-length/2 + handle_length/2 + 5, 0)
    .rect(handle_length, handle_width)
    .extrude(thickness)
    .faces(">Z")
    .workplane()
    .circle(handle_radius)
    .extrude(thickness)
)

# Right handle
result = (
    result.faces(">Z")
    .workplane()
    .moveTo(length/2 - handle_length/2 - 5, 0)
    .rect(handle_length, handle_width)
    .extrude(thickness)
    .faces(">Z")
    .workplane()
    .circle(handle_radius)
    .extrude(thickness)
)

# Create mounting holes on bottom face
result = (
    result.faces("<Z")
    .workplane()
    .moveTo(-length/2 + mount_hole_diameter + 5, -width/2 + mount_hole_diameter + 5)
    .circle(mount_hole_diameter/2)
    .extrude(thickness)
)

result = (
    result.faces("<Z")
    .workplane()
    .moveTo(length/2 - mount_hole_diameter - 5, -width/2 + mount_hole_diameter + 5)
    .circle(mount_hole_diameter/2)
    .extrude(thickness)
)

# Add fillets to edges for better appearance
result = result.edges("|Z").fillet(2.0)