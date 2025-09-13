import cadquery as cq

# Define dimensions
length = 50.0
width = 20.0
height = 10.0
circle_diameter = 8.0
recess_width = 6.0
recess_height = 8.0

# Create the base rectangular prism
result = cq.Workplane("XY").box(length, width, height)

# Add the circular cutout on the top surface
result = (
    result.faces(">Z")
    .workplane()
    .circle(circle_diameter / 2.0)
    .cutBlind(-0.1)  # Cut slightly below the surface to create a recess
)

# Add the rectangular recess on one of the sides near a corner
# Select the side face and create the recess
result = (
    result.faces("<X")
    .workplane(offset=height - recess_height)
    .rect(recess_width, recess_height, forConstruction=True)
    .vertices()
    .rect(recess_width - 2, recess_height - 2)
    .cutBlind(-height)
)

# Alternative approach to create the recess using a single cut
# result = (
#     result.faces("<X")
#     .workplane(offset=height - recess_height)
#     .rect(recess_width, recess_height)
#     .cutBlind(-height)
# )

# Alternative approach using a more precise positioning
# result = (
#     result.faces("<X")
#     .workplane(offset=0)
#     .rect(recess_width, recess_height)
#     .cutBlind(-recess_height)
# )

# The final result should have:
# 1. A rectangular prism with dimensions length x width x height
# 2. A circular recess on the top surface
# 3. A rectangular recess on the side near a corner