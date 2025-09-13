import cadquery as cq

# Define dimensions
head_diameter = 10.0
head_height = 2.0
body_diameter = 6.0
body_length = 8.0
side_hole_diameter = 1.5
base_diameter = 8.0
base_height = 3.0

# Create the head
result = cq.Workplane("XY").circle(head_diameter/2).extrude(head_height)

# Create the cylindrical body
result = result.faces(">Z").workplane().circle(body_diameter/2).extrude(body_length)

# Add the side hole
result = (
    result.faces(">Z")
    .workplane(offset=body_length/2)
    .center(body_diameter/2, 0)
    .circle(side_hole_diameter/2)
    .cutThruAll()
)

# Create the base section with square cross-section
result = (
    result.faces(">Z")
    .workplane(offset=body_length)
    .rect(base_diameter, base_diameter, forConstruction=True)
    .vertices()
    .circle(base_diameter/2)
    .extrude(base_height)
)

# Apply fillet to smooth transitions
result = result.edges("|Z").fillet(0.5)