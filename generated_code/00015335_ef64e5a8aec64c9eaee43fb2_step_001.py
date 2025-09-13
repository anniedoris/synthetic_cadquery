import cadquery as cq

# Define dimensions for the rectangular plate
length = 10.0
width = 3.0
thickness = 0.5

# Create the rectangular plate and tilt it
result = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(thickness)
    .rotate((0, 0, 0), (1, 1, 0), 30)  # Rotate 30 degrees around the diagonal axis
)