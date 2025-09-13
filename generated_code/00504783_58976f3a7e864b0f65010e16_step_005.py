import cadquery as cq

# Define dimensions
length = 40.0
width = 20.0
height = 5.0
step_height = 2.0
step_length = 10.0

# Create the main body
result = cq.Workplane("XY").box(length, width, height)

# Create the elevated/recessed section
# Add a smaller rectangle on one end (let's say at the positive X end)
# This creates an elevated section
result = (
    result.faces(">X")
    .workplane(offset=step_length)
    .rect(step_length, width, forConstruction=True)
    .vertices()
    .hole(1.0)  # Add a hole to make it more realistic
)

# Actually, let me create a more precise step feature
# Start with the base
result = cq.Workplane("XY").box(length, width, height)

# Create a step by cutting a section
step_face = result.faces(">X").val()
result = result.faces(">X").workplane(offset=step_length).rect(step_length, width).extrude(step_height)

# Or better yet, create a recessed feature by cutting
result = cq.Workplane("XY").box(length, width, height)
# Cut a recess on one end
result = (
    result.faces(">X")
    .workplane()
    .rect(step_length, width)
    .cutBlind(-step_height)
)

# Actually, let me create a more accurate elevated/recessed section
result = cq.Workplane("XY").box(length, width, height)

# Add an elevated section at one end
# First create the elevated part
elevated_part = (
    cq.Workplane("XY")
    .rect(step_length, width)
    .extrude(step_height)
    .translate((length/2 - step_length/2, 0, height))
)

# Subtract the elevated part to create a recess, or add it to create an elevation
# Let's create a recessed section
result = (
    result.faces(">X")
    .workplane()
    .rect(step_length, width)
    .cutBlind(step_height)
)

# But the description says "elevated or recessed" - let me create a simple, clear example
# Create a main rectangular block
result = cq.Workplane("XY").box(length, width, height)

# Add a recessed section on one end (subtract material)
result = (
    result.faces(">X")
    .workplane()
    .rect(step_length, width)
    .cutBlind(-step_height)
)

# Or create an elevated section by adding material
# Let me go with a recessed section for clarity
result = cq.Workplane("XY").box(length, width, height)

# Create a recessed section
recess = cq.Workplane("XY").rect(step_length, width).extrude(-step_height).translate((length/2 - step_length/2, 0, 0))
result = result.cut(recess)

# But this creates a hole, not a step. Let me reconsider.
# Better approach - create a rectangular block and add a smaller rectangular block to create a step

# Create main body
result = cq.Workplane("XY").box(length, width, height)

# Create the elevated/recessed section using a difference operation
# Create a smaller rectangular block that will be subtracted (recess) or added (elevation)
if True:  # Making it recessed
    step_block = cq.Workplane("XY").rect(step_length, width).extrude(step_height).translate((length/2 - step_length/2, 0, 0))
    result = result.cut(step_block)
else:  # Making it elevated
    step_block = cq.Workplane("XY").rect(step_length, width).extrude(step_height).translate((length/2 - step_length/2, 0, height))
    result = result.union(step_block)

# Simpler and clearer approach - just a recessed step
result = cq.Workplane("XY").box(length, width, height)

# Create a recessed step on the right side
result = (
    result.faces(">X")
    .workplane()
    .rect(step_length, width)
    .cutBlind(-step_height)
)

# Actually, I want to make a clean, clear mechanical part with a step feature
# Let's start with a clean approach

# Main body
result = cq.Workplane("XY").box(40.0, 20.0, 5.0)

# Add a recessed section on one end (10mm wide step with 2mm depth)
result = (
    result.faces(">X")
    .workplane()
    .rect(10.0, 20.0)
    .cutBlind(-2.0)
)