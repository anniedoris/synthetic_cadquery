import cadquery as cq

# Create the rectangular prism
prism_length = 4.0
prism_width = 2.0
prism_height = 1.0

# Create the cylinder
cylinder_radius = 1.0
cylinder_height = 2.0

# Create the rectangular prism
prism = cq.Workplane("XY").box(prism_length, prism_width, prism_height)

# Create the cylinder and position it adjacent to the prism
# We'll tilt the cylinder and position it next to the prism
cylinder = (
    cq.Workplane("XY")
    .center(prism_length/2 + cylinder_radius + 0.5, 0)
    .circle(cylinder_radius)
    .extrude(cylinder_height)
    .rotate((0, 0, 0), (0, 0, 1), 30)  # Rotate the cylinder
)

# Combine the two components
result = prism.union(cylinder)