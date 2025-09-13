import cadquery as cq

# Define dimensions
length = 100.0
width = 60.0
thickness = 5.0

# Define hole parameters
central_hole_diameter = 3.0
edge_hole_diameter = 6.0
slot_width = 8.0
slot_height = 20.0

# Create the base rectangular plate
result = cq.Workplane("XY").box(length, width, thickness)

# Add central grid of small holes
# Create a grid of holes in the center area
grid_spacing = 15.0
grid_offset = 15.0  # Offset from center

# Add holes in a 3x3 grid
for i in [-1, 0, 1]:
    for j in [-1, 0, 1]:
        result = (
            result.faces(">Z")
            .workplane()
            .center(i * grid_spacing, j * grid_spacing)
            .hole(central_hole_diameter)
        )

# Add two elongated slots near the center
# Slot 1 (left side)
result = (
    result.faces(">Z")
    .workplane()
    .center(-20, 0)
    .rect(slot_width, slot_height, forConstruction=True)
    .vertices()
    .hole(3.0)  # Small hole for clearance
)

# Slot 2 (right side)
result = (
    result.faces(">Z")
    .workplane()
    .center(20, 0)
    .rect(slot_width, slot_height, forConstruction=True)
    .vertices()
    .hole(3.0)  # Small hole for clearance
)

# Add edge holes (larger holes for mounting)
# Top edge holes
result = (
    result.faces(">Z")
    .workplane()
    .center(-length/2 + 15, width/2 - 5)
    .hole(edge_hole_diameter)
)
result = (
    result.faces(">Z")
    .workplane()
    .center(length/2 - 15, width/2 - 5)
    .hole(edge_hole_diameter)
)

# Bottom edge holes
result = (
    result.faces(">Z")
    .workplane()
    .center(-length/2 + 15, -width/2 + 5)
    .hole(edge_hole_diameter)
)
result = (
    result.faces(">Z")
    .workplane()
    .center(length/2 - 15, -width/2 + 5)
    .hole(edge_hole_diameter)
)

# Side edge holes
result = (
    result.faces(">Z")
    .workplane()
    .center(-length/2 + 5, 0)
    .hole(edge_hole_diameter)
)
result = (
    result.faces(">Z")
    .workplane()
    .center(length/2 - 5, 0)
    .hole(edge_hole_diameter)
)