import cadquery as cq

# Define dimensions
prism_width = 10.0
prism_depth = 5.0
prism_length = 50.0
num_prisms = 5
gap_between_prisms = 2.0
top_plate_thickness = 3.0

# Create the base plate (top connection)
top_plate = cq.Workplane("XY").box(
    num_prisms * prism_width + (num_prisms - 1) * gap_between_prisms,
    prism_depth,
    top_plate_thickness
)

# Create individual prisms
prisms = cq.Workplane("XY")
for i in range(num_prisms):
    x_pos = i * (prism_width + gap_between_prisms) - (num_prisms - 1) * (prism_width + gap_between_prisms) / 2
    prism = cq.Workplane("XY").translate((x_pos, 0, 0)).box(prism_width, prism_depth, prism_length)
    prisms = prisms.union(prism)

# Create bottom plate (separate from prisms)
bottom_plate = cq.Workplane("XY").box(
    num_prisms * prism_width + (num_prisms - 1) * gap_between_prisms,
    prism_depth,
    top_plate_thickness
).translate((0, 0, -prism_length))

# Combine top plate and prisms
result = top_plate.union(prisms).union(bottom_plate)

# Remove bottom plate from prisms to create the gap effect
result = result.cut(bottom_plate)