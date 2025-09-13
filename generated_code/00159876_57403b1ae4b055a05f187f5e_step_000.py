import cadquery as cq

# Dimensions
length = 200.0
width = 100.0
height = 50.0
top_incline = 5.0  # degrees of incline
corner_radius = 5.0
port_width = 8.0
port_height = 3.0
port_depth = 2.0
port_spacing = 12.0
port_rows = 2
port_row_spacing = 20.0

# Create the base rectangular prism with rounded corners
result = cq.Workplane("XY").box(length, width, height)

# Round all edges
result = result.edges().fillet(corner_radius)

# Create the top surface with slight incline
# We'll create a workplane on the top face and offset it
result = (
    result.faces(">Z")
    .workplane()
    .transformed(offset=cq.Vector(0, 0, 0), rotate=cq.Vector(0, top_incline, 0))
    .rect(length, width)
    .extrude(height * 0.1)
    .faces(">Z")
    .workplane()
    .transformed(offset=cq.Vector(0, 0, height - height * 0.1), rotate=cq.Vector(0, -top_incline, 0))
    .rect(length, width)
    .extrude(height * 0.1)
)

# Create the front face with ports
# We'll create a workplane on the front face
result = (
    result.faces(">Y")
    .workplane()
    .rect(length - 10, width - 10, forConstruction=True)
    .vertices()
    .hole(2.0)  # Base hole for ports
)

# Create ports in two rows
result = (
    result.faces(">Y")
    .workplane(offset=1)
    .rect(length - 20, width - 20, forConstruction=True)
    .vertices()
    .circle(1.0)
    .extrude(-port_depth)
)

# Create the front ports with two rows
result = (
    result.faces(">Y")
    .workplane(offset=1)
    .pushPoints([
        (0, -port_row_spacing/2),
        (0, port_row_spacing/2)
    ])
    .rect(port_width * port_rows + (port_rows - 1) * port_spacing, port_height, forConstruction=True)
    .vertices()
    .circle(port_width/2)
    .extrude(-port_depth)
)

# Create a more realistic port arrangement
result = (
    result.faces(">Y")
    .workplane(offset=1)
    .pushPoints([
        (-port_width/2 - port_spacing/2, -port_row_spacing/2),
        (port_width/2 + port_spacing/2, -port_row_spacing/2),
        (-port_width/2 - port_spacing/2, port_row_spacing/2),
        (port_width/2 + port_spacing/2, port_row_spacing/2),
        (-port_width/2 - port_spacing/2 - port_spacing, -port_row_spacing/2),
        (port_width/2 + port_spacing/2 + port_spacing, -port_row_spacing/2),
        (-port_width/2 - port_spacing/2 - port_spacing, port_row_spacing/2),
        (port_width/2 + port_spacing/2 + port_spacing, port_row_spacing/2),
    ])
    .rect(port_width, port_height, forConstruction=True)
    .vertices()
    .circle(port_width/2)
    .extrude(-port_depth)
)

# Create the tapered back face
# We'll subtract a smaller rectangular prism from the back
result = (
    result.faces("<Y")
    .workplane()
    .rect(length * 0.9, width * 0.9)
    .extrude(height)
)

# Refine the shape to make it more realistic
result = result.faces(">Y").workplane().rect(length - 20, width - 20).cutThruAll()

# Final refinement
result = result.edges("|Z").fillet(3.0)

# Ensure we have a clean solid
result = result.clean()

# Assign to result variable
result = result