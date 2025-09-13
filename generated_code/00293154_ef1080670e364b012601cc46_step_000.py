import cadquery as cq

# Define dimensions
length = 100.0
width = 20.0
height1 = 10.0  # First section height
height2 = 5.0   # Second section height
step_position = length / 2.0  # Position of the step

# Create the base plate with a step
result = (
    cq.Workplane("XY")
    .box(length, width, height1)  # First section
    .faces(">Z")
    .workplane(offset=height1 - height2)  # Move to the step position
    .box(length, width, height2)  # Second section
)

# Ensure the step is a sharp transition by making sure the second section
# is properly positioned to create the right-angled step
result = (
    cq.Workplane("XY")
    .box(length, width, height1)  # First section
    .faces(">Z")
    .workplane(offset=height1 - height2)
    .box(length, width, height2)  # Second section
)

# Alternative approach to create the step more clearly
result = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(height1)
    .faces(">Z")
    .workplane(offset=height1 - height2)
    .rect(length, width)
    .extrude(height2)
)

# Or even more explicitly:
result = (
    cq.Workplane("XY")
    .moveTo(-length/2, -width/2)
    .lineTo(length/2, -width/2)
    .lineTo(length/2, width/2)
    .lineTo(-length/2, width/2)
    .close()
    .extrude(height1)
    .faces(">Z")
    .workplane(offset=height1 - height2)
    .moveTo(-length/2, -width/2)
    .lineTo(length/2, -width/2)
    .lineTo(length/2, width/2)
    .lineTo(-length/2, width/2)
    .close()
    .extrude(height2)
)

# The cleanest approach:
result = (
    cq.Workplane("XY")
    .box(length, width, height1)
    .faces(">Z")
    .workplane(offset=height1 - height2)
    .box(length, width, height2)
)