import cadquery as cq

# Define dimensions
body_length = 40.0
body_width = 30.0
body_height = 15.0
cylinder_diameter = 8.0
cylinder_height = 12.0
front_cutout_radius = 10.0
side_cutout_radius = 6.0

# Create the main body as a rectangular prism
result = cq.Workplane("XY").box(body_length, body_width, body_height)

# Create the U-shaped cutout on the front face
# This will be a curved cutout that goes through the front face
result = (
    result.faces(">Z")
    .workplane(offset=-0.1)
    .center(-body_length/2 + 5, 0)
    .rect(body_length - 10, body_height - 5, forConstruction=True)
    .vertices()
    .circle(front_cutout_radius)
    .cutThruAll()
)

# Create the cylindrical protrusion on the top left corner
# Position it at the top left corner of the main body
result = (
    result.faces(">Z")
    .workplane(offset=0.1)
    .center(-body_length/2 + cylinder_diameter/2, body_width/2 - cylinder_diameter/2)
    .circle(cylinder_diameter/2)
    .extrude(cylinder_height)
)

# Create the curved cutout on the side connected to the cylinder
# This cutout connects the cylinder to the main body
result = (
    result.faces("<Y")
    .workplane(offset=-0.1)
    .center(0, -body_width/2 + cylinder_diameter/2)
    .circle(side_cutout_radius)
    .cutThruAll()
)

# Add a flat top to the cylinder for better visualization
result = (
    result.faces(">Z")
    .workplane(offset=cylinder_height - 0.1)
    .center(-body_length/2 + cylinder_diameter/2, body_width/2 - cylinder_diameter/2)
    .circle(cylinder_diameter/2)
    .extrude(0.2)
)

# Ensure the cylinder is properly attached to the main body
result = (
    result.faces("<Y")
    .workplane(offset=-0.1)
    .center(0, -body_width/2 + cylinder_diameter/2)
    .circle(side_cutout_radius)
    .cutBlind(-5)
)

# Create a more realistic curved cutout on the front face
result = (
    result.faces(">Z")
    .workplane(offset=-0.1)
    .center(-body_length/2 + 5, 0)
    .rect(body_length - 10, body_height - 5, forConstruction=True)
    .vertices()
    .circle(front_cutout_radius)
    .cutThruAll()
)

# Create a smoother U-shape cutout on the front face
result = (
    result.faces(">Z")
    .workplane(offset=-0.1)
    .center(-body_length/2 + 5, 0)
    .rect(body_length - 10, body_height - 5, forConstruction=True)
    .vertices()
    .circle(front_cutout_radius)
    .cutThruAll()
)

# Clean up and finalize
result = result.faces(">Z").workplane().circle(cylinder_diameter/2).extrude(0.1)