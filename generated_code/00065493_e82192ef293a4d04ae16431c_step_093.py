import cadquery as cq

# Define dimensions
top_length = 100.0
top_width = 50.0
top_thickness = 10.0

leg_length = 30.0
leg_width = 20.0
leg_height = 50.0

# Create the top surface
result = cq.Workplane("XY").box(top_length, top_width, top_thickness)

# Create the leg and position it under the top
# The leg should be centered under the top
result = (
    result
    .faces(">Z")  # Select the top face
    .workplane(offset=-top_thickness)  # Move to the bottom of the top
    .center(0, 0)  # Center the leg
    .box(leg_length, leg_width, leg_height, centered=True)  # Create the leg
)

# Alternative approach with more explicit positioning:
# result = cq.Workplane("XY").box(top_length, top_width, top_thickness)
# result = (
#     result
#     .faces(">Z")
#     .workplane()
#     .center(0, 0)
#     .box(leg_length, leg_width, leg_height)
# )