import cadquery as cq

# Define dimensions
length = 10.0
width = 6.0
height = 4.0
chamfer_size = 1.0

# Create the base rectangular prism
result = cq.Workplane("XY").box(length, width, height)

# Create the chamfered edge on the top face
# Select the top face and create a workplane on it
result = (
    result.faces(">Z")
    .workplane()
    .pushPoints([(length/2 - chamfer_size/2, width/2), 
                 (length/2 - chamfer_size/2, -width/2)])
    .lineTo(length/2, -width/2)
    .lineTo(length/2, width/2)
    .close()
    .extrude(-chamfer_size)
)

# Alternative approach using a more direct chamfer method
# Reset and create the object with proper chamfer
result = cq.Workplane("XY").box(length, width, height)

# Add chamfer to one edge of the top face
# We'll chamfer along the front edge (positive Y direction)
result = (
    result.faces(">Z")
    .workplane()
    .transformed(offset=cq.Vector(0, width/2 - chamfer_size/2, 0))
    .rect(chamfer_size, chamfer_size)
    .extrude(-chamfer_size)
    .faces(">Z")
    .workplane()
    .transformed(offset=cq.Vector(0, -width/2 + chamfer_size/2, 0))
    .rect(chamfer_size, chamfer_size)
    .extrude(-chamfer_size)
)

# Actually, let's simplify this with a cleaner approach
# Create base
result = cq.Workplane("XY").box(length, width, height)

# Add chamfer to top face along one edge
# First create a workplane on the top face
result = (
    result.faces(">Z")
    .workplane()
    .transformed(offset=cq.Vector(0, width/2 - chamfer_size, 0))
    .moveTo(0, 0)
    .lineTo(chamfer_size, 0)
    .lineTo(0, -chamfer_size)
    .close()
    .extrude(-chamfer_size)
)

# Even simpler - use a single chamfer operation
# Start fresh
result = cq.Workplane("XY").box(length, width, height)

# Chamfer one edge of the top face - the edge along the positive Y direction
# We'll use the edges() method to select the appropriate edge
result = (
    result.faces(">Z")
    .edges("|Y")
    .chamfer(chamfer_size)
)

# This will create a chamfer on the top edge that runs along the Y-axis
# This is a cleaner approach using CadQuery's built-in chamfer functionality
result = cq.Workplane("XY").box(length, width, height).faces(">Z").edges("|Y").chamfer(chamfer_size)