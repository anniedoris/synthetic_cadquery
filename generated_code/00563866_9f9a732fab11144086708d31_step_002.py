import cadquery as cq

# Define dimensions
length = 50.0
width = 30.0
thickness = 5.0
cutout_length = 20.0
cutout_width = 15.0
cutout_offset = 5.0

# Create the main rectangular plate
result = cq.Workplane("XY").box(length, width, thickness)

# Create the cutout feature on one side
# Move to the position where we want to create the cutout
result = (
    result.faces(">Y")  # Select the top face
    .workplane(offset=-thickness/2)  # Move to the bottom of the plate
    .moveTo(-length/2 + cutout_offset, width/2 - cutout_width/2)  # Position at cutout start
    .rect(cutout_length, cutout_width)  # Create the cutout rectangle
    .cutThruAll()  # Cut through the entire plate
)

# Alternative approach - more explicit
# result = (
#     cq.Workplane("XY")
#     .box(length, width, thickness)
#     .faces(">Y")
#     .workplane()
#     .rect(cutout_length, cutout_width)
#     .cutBlind(-thickness)
# )

# The cutout creates a protruding section on the opposite side, which is naturally handled by the 3D modeling
# The resulting object has a flat rectangular plate with a rectangular cutout on one side