import cadquery as cq

# Define dimensions
length = 100.0
width = 60.0
thickness = 5.0

# Define hole parameters
hole_diameter = 4.0
hole_spacing = 10.0

# Create the base rectangle
result = cq.Workplane("XY").box(length, width, thickness)

# Create a grid of holes
# Calculate number of holes in each direction
num_holes_x = int(length / hole_spacing) - 1
num_holes_y = int(width / hole_spacing) - 1

# Create the hole pattern
for i in range(num_holes_x):
    for j in range(num_holes_y):
        # Calculate hole position
        x_pos = -length/2 + (i + 1) * hole_spacing
        y_pos = -width/2 + (j + 1) * hole_spacing
        
        # Add hole at this position
        result = (
            result.faces(">Z")
            .workplane(offset=0.1)
            .center(x_pos, y_pos)
            .hole(hole_diameter)
        )

# Add a slight tilt for 3D appearance
result = result.rotate((0, 0, 0), (1, 0, 0), 10)

# Add a slight perspective effect by slightly skewing the edges
result = result.translate((0, 0, 0))