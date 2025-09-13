import cadquery as cq

# Define dimensions
horizontal_length = 50.0
horizontal_width = 10.0
horizontal_thickness = 3.0

vertical_length = 30.0
vertical_width = 8.0
vertical_thickness = 3.0

# Groove dimensions
groove_width = 2.0
groove_depth = 1.0

# Hole diameter
hole_diameter = 4.0

# Protrusion dimensions
protrusion_width = 2.0
protrusion_height = 2.0

# Create the base L-shaped object
result = (
    cq.Workplane("XY")
    # Create horizontal section
    .box(horizontal_length, horizontal_width, horizontal_thickness)
    # Create vertical section
    .faces(">Z")
    .workplane(offset=horizontal_thickness)
    .box(vertical_length, vertical_width, vertical_thickness)
)

# Add groove to horizontal section
result = (
    result.faces(">Z")
    .workplane(offset=horizontal_thickness - groove_depth)
    .rect(horizontal_length, groove_width, forConstruction=True)
    .vertices()
    .hole(groove_width)
)

# Add groove to vertical section
result = (
    result.faces(">Y")
    .workplane(offset=vertical_thickness - groove_depth)
    .rect(vertical_length, groove_width, forConstruction=True)
    .vertices()
    .hole(groove_width)
)

# Add hole near far end of horizontal section
result = (
    result.faces(">X")
    .workplane(offset=horizontal_thickness)
    .center(horizontal_length/2 - 10, 0)
    .hole(hole_diameter)
)

# Add hole near top of vertical section
result = (
    result.faces(">Y")
    .workplane(offset=vertical_thickness)
    .center(0, vertical_length/2 - 10)
    .hole(hole_diameter)
)

# Add protrusions at connection points
# Protrusion on horizontal section
result = (
    result.faces(">Y")
    .workplane(offset=horizontal_thickness)
    .center(horizontal_length/2 - 5, 0)
    .rect(protrusion_width, protrusion_height, forConstruction=True)
    .vertices()
    .hole(protrusion_width)
)

# Protrusion on vertical section
result = (
    result.faces("<X")
    .workplane(offset=vertical_thickness)
    .center(0, vertical_length/2 - 5)
    .rect(protrusion_width, protrusion_height, forConstruction=True)
    .vertices()
    .hole(protrusion_width)
)

# Ensure sharp edges and corners
result = result.edges("|Z").fillet(0.1)