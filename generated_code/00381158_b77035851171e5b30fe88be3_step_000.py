import cadquery as cq

# Define dimensions for the fork-like structure
fork_base_length = 40.0
fork_base_width = 20.0
fork_base_thickness = 3.0
fork_prong_width = 4.0
fork_prong_height = 10.0
fork_prong_thickness = 3.0
fork_gap = 8.0

# Define dimensions for the cylindrical component with protrusion
cylinder_diameter = 12.0
cylinder_height = 8.0
protrusion_diameter = 6.0
protrusion_height = 4.0
protrusion_offset = 2.0

# Define dimensions for the main body
main_body_length = 60.0
main_body_width = 40.0
main_body_height = 15.0

# Create the fork-like structure
fork = cq.Workplane("XY").box(fork_base_length, fork_base_width, fork_base_thickness)
# Create the fork prongs
fork_prong_length = fork_base_length - 2 * fork_gap
fork_prong = cq.Workplane("XY").box(fork_prong_length, fork_prong_width, fork_prong_height)
# Position the prongs
fork = fork.union(fork_prong.translate((0, fork_base_width/2 - fork_prong_width/2, fork_base_thickness)))
fork = fork.union(fork_prong.translate((0, -(fork_base_width/2 - fork_prong_width/2), fork_base_thickness)))

# Create the cylindrical component with protrusion
cylinder = cq.Workplane("XY").cylinder(cylinder_height, cylinder_diameter/2)
protrusion = cq.Workplane("XY").cylinder(protrusion_height, protrusion_diameter/2)
protrusion = protrusion.translate((protrusion_offset, 0, cylinder_height))
cylindrical_component = cylinder.union(protrusion)

# Create the main body with holes
main_body = cq.Workplane("XY").box(main_body_length, main_body_width, main_body_height)

# Add protrusions to the main body
protrusion1 = cq.Workplane("XY").box(8, 8, 5).translate((10, 10, main_body_height))
protrusion2 = cq.Workplane("XY").box(8, 8, 7).translate((20, -10, main_body_height))
protrusion3 = cq.Workplane("XY").box(8, 8, 6).translate((-15, 5, main_body_height))
main_body = main_body.union(protrusion1).union(protrusion2).union(protrusion3)

# Add circular holes to the main body
hole_radius = 2.0
hole_spacing = 10.0
num_holes = 4
for i in range(num_holes):
    hole_x = -main_body_length/2 + 15 + i * hole_spacing
    main_body = main_body.faces(">Y").workplane(offset=-0.1).center(hole_x, 0).hole(hole_radius)

# Position components in assembly
result = fork.translate((0, 0, 0))
result = result.union(cylindrical_component.translate((20, 0, fork_base_thickness + cylinder_height)))
result = result.union(main_body.translate((-30, 0, 0)))

# Ensure the result is properly assembled
result = result.val()