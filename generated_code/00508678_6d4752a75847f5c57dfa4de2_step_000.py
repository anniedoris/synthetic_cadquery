import cadquery as cq

# Define dimensions
length = 100.0
width = 60.0
thickness = 5.0

# Define hole parameters
hole_diameter = 4.0
hole_spacing = 15.0
edge_offset = 10.0

# Create the base plate
result = cq.Workplane("XY").box(length, width, thickness)

# Create hole pattern
# Calculate number of holes in each direction
num_holes_x = int((length - 2 * edge_offset) / hole_spacing) + 1
num_holes_y = int((width - 2 * edge_offset) / hole_spacing) + 1

# Generate hole positions
hole_positions = []
for i in range(num_holes_x):
    for j in range(num_holes_y):
        x = edge_offset + i * hole_spacing - length / 2
        y = edge_offset + j * hole_spacing - width / 2
        hole_positions.append((x, y))

# Add holes to the top face
result = result.faces(">Z").workplane().pushPoints(hole_positions).hole(hole_diameter)

# Add a slight chamfer to the edges for a more realistic look
result = result.edges("|Z").chamfer(0.5)