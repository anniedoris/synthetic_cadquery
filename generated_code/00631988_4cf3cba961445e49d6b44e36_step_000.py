import cadquery as cq

# Define dimensions
length = 10.0
width = 6.0
height = 4.0
slant_height = 2.0
curve_radius = 1.0

# Create the base rectangle
result = cq.Workplane("XY").rect(length, width).extrude(height)

# Create the slanted surface by cutting a wedge
# First, create a workplane on the top face
result = result.faces(">Z").workplane()

# Create a triangular cut to make the slant
# We'll create a triangle that goes from one corner to the opposite corner
# This creates a slanted surface
result = (
    result
    .moveTo(-length/2, -width/2)
    .lineTo(length/2, -width/2)
    .lineTo(length/2, width/2 - slant_height)
    .lineTo(-length/2, width/2)
    .close()
    .cutThruAll()
)

# Now we need to add the curved edge transition
# We'll create a curved edge where the slanted surface meets the base
# This is a bit tricky - we'll add a fillet to smooth the transition

# First, get the edge where slanted surface meets base
result = result.edges("|Z").fillet(0.5)

# Alternative approach - let's create a more precise wedge with a curved transition
result = cq.Workplane("XY").box(length, width, height)

# Create the slanted surface by cutting with a workplane
result = (
    result
    .faces(">Z")
    .workplane()
    .moveTo(-length/2, -width/2)
    .lineTo(length/2, -width/2)
    .lineTo(length/2, width/2 - slant_height)
    .lineTo(-length/2, width/2)
    .close()
    .cutThruAll()
)

# Add a curved transition at the base edge
# Create a curved edge by using a spline or fillet
result = result.edges("|Z and <X").fillet(0.3)

# Actually, let me create this more precisely with a proper curved transition
result = cq.Workplane("XY").box(length, width, height)

# Add the slanted top surface
# Create a triangle on the top face that will cut through the object
result = (
    result
    .faces(">Z")
    .workplane()
    .moveTo(-length/2, -width/2)
    .lineTo(length/2, -width/2)
    .lineTo(length/2, width/2 - slant_height)
    .lineTo(-length/2, width/2)
    .close()
    .cutThruAll()
)

# Add a curved edge by filleting
result = result.edges("|Z and <X").fillet(0.3)

# Let me create a cleaner version with a proper curved edge
result = cq.Workplane("XY").box(10.0, 6.0, 4.0)

# Create the slanted surface with a proper cut
result = (
    result
    .faces(">Z")
    .workplane()
    .moveTo(-5.0, -3.0)
    .lineTo(5.0, -3.0)
    .lineTo(5.0, 1.0)
    .lineTo(-5.0, 3.0)
    .close()
    .cutThruAll()
)

# Add a curved transition edge
# Create a smooth curve from the slanted surface to base
result = result.edges("|Z and <X").fillet(0.5)

# For a more precise curved edge, let's use a better approach
result = cq.Workplane("XY").box(10.0, 6.0, 4.0)

# Create the slanted surface
result = (
    result
    .faces(">Z")
    .workplane()
    .polygon(4, 8.0)  # Create a polygon that will be cut
    .workplane(offset=2.0)
    .rect(8.0, 4.0)
    .loft(combine=True)
)

# Actually, let's start over with a cleaner approach
result = (
    cq.Workplane("XY")
    .box(10.0, 6.0, 4.0)
    .faces(">Z")
    .workplane()
    .moveTo(-5.0, -3.0)
    .lineTo(5.0, -3.0)
    .lineTo(5.0, 1.0)
    .lineTo(-5.0, 3.0)
    .close()
    .cutThruAll()
    .edges("|Z and <X")
    .fillet(0.5)
)

# Cleaner approach - create the wedge with proper curved transition
result = cq.Workplane("XY").box(10.0, 6.0, 4.0)

# Create a triangular cut to make the slanted surface
result = (
    result
    .faces(">Z")
    .workplane()
    .moveTo(-5.0, -3.0)
    .lineTo(5.0, -3.0)
    .lineTo(5.0, 1.0)
    .lineTo(-5.0, 3.0)
    .close()
    .cutThruAll()
)

# Add a curved edge transition from slanted surface to base
result = result.edges("|Z and <X").fillet(0.5)