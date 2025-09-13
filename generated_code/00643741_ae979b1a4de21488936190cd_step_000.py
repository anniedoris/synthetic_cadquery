import cadquery as cq

# Define dimensions
main_width = 40.0
main_height = 60.0
main_depth = 10.0

protrusion_width = 20.0
protrusion_height = 15.0
protrusion_depth = 8.0

# Create the main body
result = cq.Workplane("XY").box(main_width, main_depth, main_height)

# Create the protrusion on top
result = (
    result.faces(">Z")
    .workplane()
    .rect(protrusion_width, protrusion_depth, forConstruction=True)
    .vertices()
    .moveTo(0, 0)
    .rect(protrusion_width, protrusion_depth)
    .extrude(protrusion_height)
)