import cadquery as cq

# Create a rectangular prism with dimensions
length = 4.0
width = 3.0
height = 2.0

# Create the base box
result = cq.Workplane("XY").box(length, width, height)

# Apply a rotation to give it a slanted perspective (tilt to the left and forward)
# Rotate around the Y-axis to tilt forward and around the Z-axis to tilt left
result = result.rotate((0, 0, 0), (0, 1, 0), 15)  # Tilt forward 15 degrees
result = result.rotate((0, 0, 0), (0, 0, 1), -10)  # Tilt left 10 degrees