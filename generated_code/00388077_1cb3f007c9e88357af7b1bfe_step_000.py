import cadquery as cq

# Base dimensions
base_length = 50.0
base_width = 30.0
base_height = 5.0

# Cylinder dimensions
cylinder_radius = 8.0
cylinder_height = 15.0
cylinder_offset = 10.0  # Distance from base edge

# Hole dimensions
hole_radius = 4.0
hole_offset = 15.0  # Distance from front edge for holes

# Create base with chamfers
result = cq.Workplane("XY").box(base_length, base_width, base_height)

# Add chamfers to edges
result = result.edges("|Z").chamfer(1.0)

# Add holes in base
result = (
    result.faces(">Z")
    .workplane()
    .center(-hole_offset, -base_width/2 + 5.0)
    .circle(hole_radius)
    .center(2*hole_offset, 0)
    .circle(hole_radius)
    .cutThruAll()
)

# Create the connecting section (trapezoidal)
# First, create a workplane on the side where cylinder will be
result = (
    result.faces(">Y")
    .workplane(offset=-cylinder_height/2)
    .center(-base_length/2 + cylinder_offset, 0)
    .rect(20.0, 5.0)
    .extrude(cylinder_height)
)

# Create the cylindrical feature
result = (
    result.faces("<Y")
    .workplane()
    .center(-base_length/2 + cylinder_offset, 0)
    .circle(cylinder_radius)
    .extrude(cylinder_height)
)

# Add hole through cylinder
result = (
    result.faces("<Y")
    .workplane()
    .center(-base_length/2 + cylinder_offset, 0)
    .hole(hole_radius)
)

# Create triangular connecting section
# Create a triangle connecting the cylinder to the base
result = (
    result.faces("<Y")
    .workplane(offset=-cylinder_height/2)
    .center(-base_length/2 + cylinder_offset, 0)
    .polygon(3, 10.0)
    .extrude(5.0)
)

# Add a small triangular feature to complete the connection
result = (
    result.faces("<Y")
    .workplane(offset=-cylinder_height/2 + 2.5)
    .center(-base_length/2 + cylinder_offset + 5.0, 0)
    .polygon(3, 5.0)
    .extrude(2.5)
)

# Add chamfers to the connection area
result = result.edges("|Z").chamfer(0.5)