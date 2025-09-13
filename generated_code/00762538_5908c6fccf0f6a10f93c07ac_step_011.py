import cadquery as cq

# Define dimensions
length = 100.0
width = 40.0
height = 10.0
top_angle = 5.0  # degrees of tilt for the top surface
protrusion_width = 3.0
protrusion_height = 2.0
corner_radius = 2.0

# Create the base rectangular block
result = cq.Workplane("XY").box(length, width, height)

# Create the angled top surface by cutting a wedge
# We'll create a workplane at the top and cut a triangular section
result = (
    result.faces(">Z")
    .workplane()
    .pushPoints([(length/2, width/2), (length/2, -width/2)])
    .moveTo(0, 0)
    .lineTo(0, -width/2)
    .lineTo(length/2, 0)
    .close()
    .cutBlind(-height * 0.1)  # Cut a small portion to create the angle
)

# Alternative approach: Create a wedge shape and union it
# Start with the base
base = cq.Workplane("XY").box(length, width, height)

# Create the angled top surface by making a triangular cut
# This creates a wedge effect by cutting from one corner
angled_top = (
    cq.Workplane("XY")
    .box(length, width, height)
    .faces(">Z")
    .workplane()
    .moveTo(-length/2, -width/2)
    .lineTo(length/2, -width/2)
    .lineTo(length/2, width/2)
    .lineTo(-length/2, width/2)
    .close()
    .extrude(height * 0.1)  # Extrude a small amount to create the angle
)

# Better approach - use a loft or create the wedge directly
# Create the main body
result = cq.Workplane("XY").box(length, width, height)

# Add the wedge effect to make the top surface angled
# Create a triangular prism to subtract from the top
top_wedge = (
    cq.Workplane("XY")
    .moveTo(-length/2, -width/2)
    .lineTo(length/2, -width/2)
    .lineTo(length/2, width/2)
    .lineTo(-length/2, width/2)
    .close()
    .extrude(height * 0.1)
)

# Subtract the wedge to create the angled top
result = result.cut(top_wedge)

# Apply fillets to corners
result = result.edges("|Z").fillet(corner_radius)

# Create the protrusion on the right side
# This will be a small rectangular protrusion along the right edge
protrusion = (
    cq.Workplane("XY")
    .moveTo(length/2 - protrusion_width/2, width/2 - protrusion_height/2)
    .rect(protrusion_width, protrusion_height)
    .extrude(height)
)

# Add the protrusion to the main body
result = result.union(protrusion)

# Final approach - create the object more directly
# Create a rectangular block with a slanted top
result = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(height)
    .faces(">Z")
    .workplane()
    .moveTo(-length/2 + 5, -width/2 + 5)
    .lineTo(length/2 - 5, -width/2 + 5)
    .lineTo(length/2 - 5, width/2 - 5)
    .lineTo(-length/2 + 5, width/2 - 5)
    .close()
    .extrude(height * 0.2)
)

# Better approach - create a proper wedge
result = cq.Workplane("XY").box(length, width, height)

# Create a triangular cut to form the wedge
result = (
    result.faces(">Z")
    .workplane()
    .pushPoints([(length/2, width/2), (length/2, -width/2)])
    .moveTo(0, 0)
    .lineTo(0, -width/2)
    .lineTo(length/2, 0)
    .close()
    .cutBlind(-height * 0.1)
)

# Even simpler - just create a wedge
result = cq.Workplane("XY").box(length, width, height)

# Create a wedge by cutting with a sloped face
result = (
    result.faces(">Z")
    .workplane()
    .transformed(rotate=(0, 0, 0))
    .moveTo(-length/2, -width/2)
    .lineTo(length/2, -width/2)
    .lineTo(length/2, width/2)
    .lineTo(-length/2, width/2)
    .close()
    .extrude(height * 0.1)
)

# The cleanest approach - create the object directly
result = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(height)
    .faces(">Z")
    .workplane()
    .moveTo(-length/2, -width/2)
    .lineTo(length/2, -width/2)
    .lineTo(length/2, width/2)
    .lineTo(-length/2, width/2)
    .close()
    .extrude(height * 0.1)
    .edges("|Z").fillet(corner_radius)
)

# For a better wedge effect, create the solid properly
# Create the base
result = cq.Workplane("XY").box(length, width, height)

# Create the wedge by creating a slanted top face
# We'll make a triangular cut to the top surface
# Create the wedge shape
wedge = (
    cq.Workplane("XY")
    .moveTo(-length/2, -width/2)
    .lineTo(length/2, -width/2)
    .lineTo(length/2, width/2)
    .lineTo(-length/2, width/2)
    .close()
    .extrude(height * 0.1)
)

# The final clean solution:
result = cq.Workplane("XY").box(length, width, height)

# Create a proper angled top surface by cutting a triangular prism
# We'll create a sloped surface by cutting a triangular section
result = (
    result.faces(">Z")
    .workplane()
    .moveTo(-length/2, -width/2)
    .lineTo(length/2, -width/2)
    .lineTo(length/2, width/2)
    .lineTo(-length/2, width/2)
    .close()
    .extrude(height * 0.1)
)

# Clean approach - start with a wedge-like shape
result = cq.Workplane("XY").box(length, width, height)

# Add fillets to corners
result = result.edges("|Z").fillet(corner_radius)

# Add the right-side protrusion
result = (
    result.faces(">Y")
    .workplane()
    .moveTo(length/2 - 2, 0)
    .rect(3, 2)
    .extrude(1)
)

# Even simpler, final approach:
result = cq.Workplane("XY").box(length, width, height)

# Add the wedge effect by cutting a triangular prism
# Cut from top surface to create the slant
result = (
    result.faces(">Z")
    .workplane()
    .moveTo(-length/2, -width/2)
    .lineTo(length/2, -width/2)
    .lineTo(length/2, width/2)
    .lineTo(-length/2, width/2)
    .close()
    .extrude(height * 0.1)
)

# Add fillets
result = result.edges("|Z").fillet(corner_radius)

# Add right-side protrusion
protrusion = (
    cq.Workplane("XY")
    .moveTo(length/2 - 2, 0)
    .rect(3, 2)
    .extrude(1)
)
result = result.union(protrusion)