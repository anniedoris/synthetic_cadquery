import cadquery as cq

# Define dimensions
top_diameter = 20.0
bottom_diameter = 30.0
height = 15.0
hole_diameter = 8.0

# Create the frustum of a cone with a central hole
result = (
    cq.Workplane("XY")
    .circle(bottom_diameter / 2.0)  # Bottom face
    .workplane(offset=height)        # Move to top face position
    .circle(top_diameter / 2.0)      # Top face
    .loft(combine=True)              # Create frustum by lofting between faces
    .faces(">Z")                     # Select top face
    .workplane()                     # Work on top face
    .hole(hole_diameter)             # Create central hole
)

# Alternative approach using box and cut for more control:
# result = (
#     cq.Workplane("XY")
#     .box(bottom_diameter, bottom_diameter, height, centered=False)
#     .faces(">Z")
#     .workplane()
#     .circle(top_diameter / 2.0)
#     .workplane(offset=height)
#     .circle(bottom_diameter / 2.0)
#     .loft(combine=True)
#     .faces(">Z")
#     .workplane()
#     .hole(hole_diameter)
# )