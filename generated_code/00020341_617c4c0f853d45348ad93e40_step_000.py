import cadquery as cq

# Define dimensions
length = 100.0
width = 50.0
height = 20.0
bevel_height = 5.0
bevel_width = 10.0

# Create the base rectangular prism
result = cq.Workplane("XY").box(length, width, height)

# Create a beveled edge on one side
# We'll create a triangular section to simulate the bevel
# This will be a cut operation that removes material to create the bevel
bevel_face = (
    cq.Workplane("XY")
    .moveTo(length/2, -width/2)  # Start at bottom edge
    .lineTo(length/2 - bevel_width, -width/2)  # Horizontal line
    .lineTo(length/2 - bevel_width, -width/2 + bevel_height)  # Vertical line
    .close()
)

# Cut this bevel from the side face
result = (
    result.faces(">Y")  # Select the right face
    .workplane(offset=-height/2)
    .pushPoints([(length/2 - bevel_width/2, -width/2 + bevel_height/2)])
    .rect(bevel_width, bevel_height)
    .cutBlind(-height/2)
)

# Alternative approach: Create the bevel more directly
# Start with the base box
result = cq.Workplane("XY").box(length, width, height)

# Create a beveled edge by adding a triangular cut
# This creates a more realistic bevel by cutting a triangular section
result = (
    result.faces(">Y")  # Select the right face
    .workplane()
    .moveTo(0, -width/2)  # Move to bottom edge
    .lineTo(-bevel_width, -width/2)  # Horizontal
    .lineTo(-bevel_width, -width/2 + bevel_height)  # Vertical
    .close()
    .cutBlind(height)
)

# Actually, let me create a cleaner bevel by adding a proper angled face
# Create the main body
result = cq.Workplane("XY").box(length, width, height)

# Add the bevel by creating a triangular cut on one side
# This creates a beveled edge on the right side
result = (
    result.faces(">Y")  # Right face
    .workplane()
    .moveTo(0, -width/2 + bevel_height)
    .lineTo(-bevel_width, -width/2 + bevel_height)
    .lineTo(-bevel_width, -width/2)
    .lineTo(0, -width/2)
    .close()
    .cutBlind(height)
)

# Even simpler approach - create a more realistic beveled object
# Start with base box
result = cq.Workplane("XY").box(length, width, height)

# Create the bevel by cutting a triangular section from the side
# This creates a beveled edge on the right side
result = (
    result.faces(">Y")
    .workplane()
    .moveTo(-length/2, -width/2)
    .lineTo(-length/2 + bevel_width, -width/2)
    .lineTo(-length/2 + bevel_width, -width/2 + bevel_height)
    .lineTo(-length/2, -width/2 + bevel_height)
    .close()
    .cutBlind(height)
)

# Or, a cleaner approach using a proper triangular extrusion
# Create the main box
result = cq.Workplane("XY").box(length, width, height)

# Add a triangular bevel on one side face
result = (
    result.faces(">Y")  # Select right face
    .workplane()
    .polygon(3, 10)  # Create triangle for bevel
    .cutBlind(height/2)  # Cut half the height
)

# Let me create a simpler, cleaner version that matches the description better
# Create a rectangular prism and add a simple bevel
result = cq.Workplane("XY").box(100, 50, 20)

# Create a bevel on the right edge by cutting a triangular section
# This creates a right triangle that bevels the edge
result = (
    result.faces(">Y")
    .workplane()
    .moveTo(0, -25)
    .lineTo(-10, -25)
    .lineTo(-10, -20)
    .close()
    .cutBlind(20)
)