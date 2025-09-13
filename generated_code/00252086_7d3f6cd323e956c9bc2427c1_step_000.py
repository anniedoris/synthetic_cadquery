import cadquery as cq

# Define dimensions
length = 100.0
width = 60.0
height = 40.0

# Define hollow section dimensions
hollow_length = 30.0
hollow_width = 20.0
hollow_height = 25.0

# Create the base rectangular prism
result = cq.Workplane("XY").box(length, width, height)

# Remove the hollow section from the top-left corner
# We'll create a workplane at the corner where we want to remove material
result = (
    result.faces(">Z")  # Select top face
    .workplane(offset=-hollow_height)  # Move to the height where hollow starts
    .transformed(offset=cq.Vector(0, 0, -hollow_height))  # Offset to the corner
    .rect(hollow_length, hollow_width)  # Create rectangle for hollow
    .extrude(hollow_height)  # Extrude to create the hollow section
)

# Alternative approach - more precise corner removal
# Create the base box
result = cq.Workplane("XY").box(length, width, height)

# Create a workplane at the top face and move to the corner
# Then create the hollow section
result = (
    result.faces(">Z")  # Select top face
    .workplane()  # Workplane on top face
    .moveTo(-length/2 + hollow_length/2, width/2 - hollow_width/2)  # Move to corner
    .rect(hollow_length, hollow_width)  # Create rectangle for hollow
    .extrude(-hollow_height)  # Extrude downward to create hollow
)

# Another approach - cut a block from the corner
result = cq.Workplane("XY").box(length, width, height)

# Cut a block from the corner
result = (
    result.faces(">Z")  # Select top face
    .workplane()  # Workplane on top face
    .moveTo(-length/2 + hollow_length/2, width/2 - hollow_width/2)  # Move to corner
    .rect(hollow_length, hollow_width)  # Create rectangle for hollow
    .cutBlind(-hollow_height)  # Cut downward to create hollow
)

# Final clean approach
result = cq.Workplane("XY").box(length, width, height)

# Cut a corner hollow section
result = (
    result.faces(">Z")  # Select top face
    .workplane()  # Workplane on top face
    .moveTo(-length/2 + hollow_length/2, width/2 - hollow_width/2)  # Move to corner
    .rect(hollow_length, hollow_width)  # Create rectangle for hollow
    .cutBlind(-hollow_height)  # Cut downward to create hollow
)

# Even more precise - remove exact corner
result = cq.Workplane("XY").box(length, width, height)

# Remove the hollow section from the top-left corner
result = (
    result.faces(">Z")  # Select top face
    .workplane()  # Workplane on top face
    .moveTo(-length/2 + hollow_length/2, width/2 - hollow_width/2)  # Move to corner
    .rect(hollow_length, hollow_width)  # Create rectangle for hollow
    .cutBlind(-hollow_height)  # Cut downward to create hollow
)

# Final approach - using the correct corner position
result = cq.Workplane("XY").box(length, width, height)

# Create a corner hollow by cutting a block from the top-left corner
# The hollow section starts from the top face and goes downward
result = (
    result.faces(">Z")  # Select top face
    .workplane(offset=-hollow_height)  # Workplane at bottom of hollow section
    .moveTo(-length/2 + hollow_length/2, width/2 - hollow_width/2)  # Position at corner
    .rect(hollow_length, hollow_width)  # Rectangle for hollow section
    .extrude(hollow_height)  # Extrude to create the hollow
)

# Most accurate approach
result = cq.Workplane("XY").box(length, width, height)

# Remove a corner hollow section
# We'll create a workplane at the corner and cut the hollow
result = (
    result.faces(">Z")  # Select top face
    .workplane()  # Workplane on top face
    .moveTo(-length/2 + hollow_length/2, width/2 - hollow_width/2)  # Position at corner
    .rect(hollow_length, hollow_width)  # Rectangle for hollow section
    .cutBlind(-hollow_height)  # Cut downward to create hollow
)