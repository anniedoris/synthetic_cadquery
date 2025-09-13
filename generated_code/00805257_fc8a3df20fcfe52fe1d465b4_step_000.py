import cadquery as cq

# Define dimensions
base_length = 40.0
base_width = 20.0
base_height = 5.0

arrow_body_length = 25.0
arrow_body_width = 8.0
arrow_body_height = 3.0

arrow_head_width = 12.0
arrow_head_height = 8.0

# Create the base rectangular prism
result = cq.Workplane("XY").box(base_length, base_width, base_height)

# Create the arrow body
arrow_body = (
    cq.Workplane("XY")
    .moveTo(base_length/2 - arrow_body_length/2, 0)
    .rect(arrow_body_length, arrow_body_width)
    .extrude(arrow_body_height)
)

# Create the arrow head
arrow_head = (
    cq.Workplane("XY")
    .moveTo(base_length/2 + arrow_body_length/2, 0)
    .polygon(3, arrow_head_width)
    .extrude(arrow_head_height)
    .translate((0, 0, arrow_body_height/2))
)

# Combine the base with the arrow features
result = result.union(arrow_body).union(arrow_head)

# Add fillets to the edges for a more refined look
result = result.edges("|Z").fillet(1.0)