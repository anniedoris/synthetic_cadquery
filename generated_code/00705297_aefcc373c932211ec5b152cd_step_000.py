import cadquery as cq

# Define dimensions
base_length = 50.0
base_width = 30.0
base_height = 10.0

vertical_length = 30.0
vertical_width = 30.0
vertical_height = 40.0

# Create the base rectangular prism
result = cq.Workplane("XY").box(base_length, base_width, base_height)

# Create the vertical rectangular prism attached to the base
# Position it so that it's attached to the shorter side of the base
result = (
    result.faces(">Z")
    .workplane()
    .moveTo(0, base_width/2)  # Move to the center of the shorter side
    .box(vertical_length, vertical_width, vertical_height, centered=False)
)