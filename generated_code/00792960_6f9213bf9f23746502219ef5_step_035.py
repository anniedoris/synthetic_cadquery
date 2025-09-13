import cadquery as cq

# Define the dimensions for the vertical line segment
length = 10.0    # Length of the line (height)
width = 1.0      # Width of the line
thickness = 1.0  # Thickness of the line

# Create a vertical line segment represented as a rectangular prism
result = cq.Workplane("XY").box(width, thickness, length)