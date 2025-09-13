import cadquery as cq

# Define dimensions
wall_width = 100.0
wall_height = 80.0
wall_thickness = 10.0
opening_width = 20.0
opening_height = 30.0
ledge_width = 100.0
ledge_depth = 15.0
ledge_height = 5.0
protrusion_width = 8.0
protrusion_depth = 12.0

# Create the main wall
result = cq.Workplane("XY").box(wall_width, wall_thickness, wall_height)

# Create the first opening
result = (
    result.faces(">Y")
    .workplane(offset=-wall_thickness/2)
    .moveTo(-wall_width/2 + opening_width/2, wall_height/2 - opening_height/2)
    .rect(opening_width, opening_height)
    .cutThruAll()
)

# Create the second opening
result = (
    result.faces(">Y")
    .workplane(offset=-wall_thickness/2)
    .moveTo(wall_width/2 - opening_width/2, wall_height/2 - opening_height/2)
    .rect(opening_width, opening_height)
    .cutThruAll()
)

# Add the base ledge
result = (
    result.faces("<Y")
    .workplane(offset=-ledge_height)
    .rect(ledge_width, ledge_depth)
    .extrude(ledge_height)
)

# Add the protrusion on the right side
result = (
    result.faces(">X")
    .workplane(offset=wall_thickness/2)
    .moveTo(wall_width/2 - protrusion_width/2, wall_height/2 - protrusion_depth/2)
    .rect(protrusion_width, protrusion_depth)
    .extrude(wall_thickness/2)
)

# Add a small extension on the left side to represent a corner
result = (
    result.faces("<X")
    .workplane(offset=wall_thickness/2)
    .moveTo(-wall_width/2 + protrusion_width/2, wall_height/2 - protrusion_depth/2)
    .rect(protrusion_width, protrusion_depth)
    .extrude(wall_thickness/2)
)