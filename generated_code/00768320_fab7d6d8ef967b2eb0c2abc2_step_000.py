import cadquery as cq

# Define dimensions for the rectangular prism
length = 10.0   # Vertical dimension (longer)
width = 3.0     # Horizontal dimension
depth = 3.0     # Horizontal dimension (equal to width for square cross-section)

# Create the rectangular prism
result = cq.Workplane("XY").box(length, width, depth)