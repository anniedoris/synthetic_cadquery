import cadquery as cq

# Define dimensions
vertical_width = 20.0
vertical_depth = 10.0
vertical_height = 30.0
horizontal_length = 25.0
horizontal_depth = 10.0
horizontal_height = 15.0

# Create the main vertical section
result = cq.Workplane("XY").box(vertical_width, vertical_depth, vertical_height)

# Add the horizontal section extending from the top
result = (
    result.faces(">Z")
    .workplane()
    .rect(horizontal_length, horizontal_depth)
    .extrude(horizontal_height)
)

# Ensure the horizontal section is centered on the vertical section
result = (
    result.faces(">Z")
    .workplane()
    .center(-vertical_width/2 + horizontal_length/2, 0)
    .rect(horizontal_length, horizontal_depth)
    .extrude(horizontal_height)
)

# Alternative approach - simpler and more direct
result = cq.Workplane("XY").box(vertical_width, vertical_depth, vertical_height)
result = (
    result.faces(">Z")
    .workplane()
    .center(-vertical_width/2 + horizontal_length/2, 0)
    .rect(horizontal_length, horizontal_depth)
    .extrude(horizontal_height)
)