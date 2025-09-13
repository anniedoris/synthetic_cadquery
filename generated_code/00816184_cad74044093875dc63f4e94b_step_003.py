import cadquery as cq

# Define dimensions for the rectangular prism
length = 10.0  # Length along the bar
width = 2.0    # Width of the square cross-section
height = 2.0   # Height of the square cross-section

# Create the rectangular prism
result = cq.Workplane("XY").box(length, width, height)

# Rotate it to create the diagonal/angled appearance
# This will tilt the bar to show it at an angle
result = result.rotate((0, 0, 0), (1, 0, 0), 30)  # Rotate around X-axis by 30 degrees
result = result.rotate((0, 0, 0), (0, 1, 0), 15)  # Rotate around Y-axis by 15 degrees