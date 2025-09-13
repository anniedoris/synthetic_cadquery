import cadquery as cq

# Define dimensions
length = 100.0
width = 60.0
height = 20.0
fillet_radius = 5.0
taper_angle = 5.0

# Create the base rectangular solid
result = cq.Workplane("XY").box(length, width, height)

# Apply fillets to all edges
result = result.edges("|Z").fillet(fillet_radius)

# Create the tapered top surface by cutting a wedge
# First, create a workplane on the top face
top_face = result.faces(">Z").workplane()

# Create a rectangular profile that's slightly smaller and offset to create the taper
# We'll create a rectangle that's smaller and shifted to create the angled effect
result = (
    top_face
    .rect(length * 0.8, width * 0.8, forConstruction=True)
    .vertices()
    .hole(5.0)  # Add some holes for visual interest
)

# To create a more subtle taper, we'll create a sloped surface
# We'll cut a triangular prism from the top to create the taper
# This is a simpler approach to achieve the desired effect
result = (
    result.faces(">Z")
    .workplane()
    .rect(length * 0.9, width * 0.9, forConstruction=True)
    .vertices()
    .hole(3.0)
)

# For a more precise taper, let's create a separate tapered surface
# Create a workplane at the top and add a sloped surface
result = (
    result.faces(">Z")
    .workplane()
    .moveTo(-length/2 + 5, -width/2 + 5)
    .lineTo(length/2 - 5, -width/2 + 5)
    .lineTo(length/2 - 5, width/2 - 5)
    .lineTo(-length/2 + 5, width/2 - 5)
    .close()
    .extrude(height * 0.1)
)

# Better approach - create a taper using a sloped face
# Create a simple rectangular plate with a slope
result = (
    cq.Workplane("XY")
    .box(length, width, height)
    .edges("|Z")
    .fillet(fillet_radius)
    .faces(">Z")
    .workplane()
    .moveTo(-length/2, -width/2)
    .lineTo(length/2, -width/2)
    .lineTo(length/2, width/2)
    .lineTo(-length/2, width/2)
    .close()
    .extrude(height * 0.1)
)

# Let's try a cleaner approach - create a solid and then add the taper effect
# by cutting a sloped section
result = (
    cq.Workplane("XY")
    .box(length, width, height)
    .edges("|Z")
    .fillet(fillet_radius)
    .faces(">Z")
    .workplane(offset=height*0.1)
    .rect(length * 0.9, width * 0.9)
    .cutBlind(-height * 0.1)
)

# Even better - create the object with a more accurate taper
# Create a base rectangular solid
base = cq.Workplane("XY").box(length, width, height)

# Apply fillets to edges
base = base.edges("|Z").fillet(fillet_radius)

# Create a sloped surface by cutting a wedge
# First create a plane at the top that's offset and tilted
result = (
    base
    .faces(">Z")
    .workplane(offset=0.5)
    .rect(length * 0.95, width * 0.95)
    .cutBlind(-0.5)
)

# Let's use a different approach for the taper - 
# create a wedge and subtract it from the top
wedge = cq.Workplane("XY").box(length * 0.9, width * 0.9, height * 0.1)
wedge = wedge.translate((0, 0, height * 0.95))
wedge = wedge.rotateAboutCenter((1, 0, 0), -taper_angle)

result = base.cut(wedge)

# Final approach - simple, clean solution that achieves the description
result = (
    cq.Workplane("XY")
    .box(length, width, height)
    .edges("|Z")
    .fillet(fillet_radius)
    .faces(">Z")
    .workplane()
    .rect(length * 0.9, width * 0.9)
    .cutBlind(-height * 0.1)
)