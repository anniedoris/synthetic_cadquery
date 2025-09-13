import cadquery as cq

# Define dimensions
length = 100.0
width = 20.0
height = 10.0
cylinder_diameter = 4.0
cylinder_height = 3.0
num_cylinders = 16
cylinders_per_row = 8

# Create the main rectangular prism
result = cq.Workplane("XY").box(length, width, height)

# Create the two rows of cylinders
# First row (top row)
first_row_y = width/2 - cylinder_diameter
# Second row (bottom row)
second_row_y = -width/2 + cylinder_diameter

# Spacing between cylinder centers
spacing = length / (cylinders_per_row - 1)

# Add cylinders to first row
for i in range(cylinders_per_row):
    x = -length/2 + i * spacing
    result = (
        result.faces(">Z")
        .workplane(offset=0.01, centerOption="CenterOfBoundBox")
        .center(x, first_row_y)
        .circle(cylinder_diameter/2)
        .extrude(cylinder_height)
    )

# Add cylinders to second row
for i in range(cylinders_per_row):
    x = -length/2 + i * spacing
    result = (
        result.faces(">Z")
        .workplane(offset=0.01, centerOption="CenterOfBoundBox")
        .center(x, second_row_y)
        .circle(cylinder_diameter/2)
        .extrude(cylinder_height)
    )

# Round the corners slightly
result = result.edges("|Z").fillet(1.0)