import cadquery as cq

# Define dimensions
top_length = 100.0
top_width = 20.0
top_thickness = 5.0

central_height = 60.0
central_width = 15.0
central_thickness = 5.0

inclined_length = 50.0
inclined_angle = 45.0
inclined_thickness = 5.0

bottom_height = 20.0
bottom_width = 15.0
bottom_thickness = 5.0

# Create the top horizontal section
result = cq.Workplane("XY").box(top_length, top_width, top_thickness)

# Add the central vertical section
result = (
    result.faces(">Z")
    .workplane()
    .rect(central_width, central_height, forConstruction=True)
    .vertices()
    .rect(central_width, central_height)
    .extrude(central_height)
)

# Add the inclined plate
result = (
    result.faces(">Z")
    .workplane(offset=central_height)
    .transformed(rotate=cq.Vector(0, 0, -inclined_angle))
    .rect(inclined_length, inclined_thickness, forConstruction=True)
    .vertices()
    .rect(inclined_length, inclined_thickness)
    .extrude(inclined_length)
)

# Add the bottom vertical plate
result = (
    result.faces(">Z")
    .workplane(offset=inclined_length)
    .rect(bottom_width, bottom_height, forConstruction=True)
    .vertices()
    .rect(bottom_width, bottom_height)
    .extrude(bottom_height)
)

# Ensure all edges are sharp and clean by not adding fillets