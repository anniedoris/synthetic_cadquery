import cadquery as cq

# Define dimensions
central_cylinder_diameter = 20.0
central_cylinder_height = 30.0
small_cylinder_diameter = 8.0
small_cylinder_height = 15.0
small_cylinder_offset = 10.0
base_length = 30.0
base_width = 25.0
base_height = 5.0
top_protrusion_width = 4.0
top_protrusion_height = 2.0
top_protrusion_depth = 3.0

# Create the central cylinder
result = cq.Workplane("XY").circle(central_cylinder_diameter / 2).extrude(central_cylinder_height)

# Add the smaller cylinder on one side
result = (
    result.faces(">Z")
    .workplane()
    .center(central_cylinder_diameter / 2 + small_cylinder_offset, 0)
    .circle(small_cylinder_diameter / 2)
    .extrude(small_cylinder_height)
)

# Add the rectangular base
result = (
    result.faces("<Z")
    .workplane()
    .rect(base_length, base_width)
    .extrude(-base_height)
)

# Add the rectangular protrusions on top of the central cylinder
result = (
    result.faces(">Z")
    .workplane()
    .center(-top_protrusion_width/2, 0)
    .rect(top_protrusion_width, top_protrusion_height)
    .extrude(top_protrusion_depth)
)

result = (
    result.faces(">Z")
    .workplane()
    .center(top_protrusion_width/2, 0)
    .rect(top_protrusion_width, top_protrusion_height)
    .extrude(top_protrusion_depth)
)