import cadquery as cq

# Define dimensions
block_length = 50.0
block_width = 30.0
block_height = 20.0
hole_diameter = 4.0
shaft_diameter = 6.0
shaft_height = 15.0
cap_diameter = 8.0

# Create the main rectangular block
result = cq.Workplane("XY").box(block_length, block_width, block_height)

# Add mounting holes at the corners of the top surface
hole_radius = hole_diameter / 2.0
result = (
    result.faces(">Z")
    .workplane()
    .rect(block_length - hole_diameter, block_width - hole_diameter, forConstruction=True)
    .vertices()
    .hole(hole_diameter)
)

# Add the cylindrical shaft
result = (
    result.faces(">Z")
    .workplane()
    .center(0, 0)
    .circle(shaft_diameter / 2.0)
    .extrude(shaft_height)
)

# Add the hemispherical cap on top of the shaft
result = (
    result.faces(">Z")
    .workplane()
    .center(0, 0)
    .circle(cap_diameter / 2.0)
    .extrude(cap_diameter / 2.0)
)

# Ensure the cap is a proper hemisphere by filleting the edges
result = result.faces(">Z").edges().fillet(cap_diameter / 4.0)