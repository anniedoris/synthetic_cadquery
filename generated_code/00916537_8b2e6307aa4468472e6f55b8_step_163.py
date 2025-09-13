import cadquery as cq

# Define dimensions
outer_diameter = 20.0
inner_diameter = 12.0
length = 15.0
thickness = (outer_diameter - inner_diameter) / 2

# Create the hollow cylinder
result = (
    cq.Workplane("XY")
    .circle(outer_diameter / 2)
    .circle(inner_diameter / 2)
    .extrude(length)
    .faces(">Z")
    .fillet(1.0)  # Round top edge
    .faces("<Z")
    .fillet(1.0)  # Round bottom edge
    .transformed(rotate=cq.Vector(15, 0, 0))  # Tilt the cylinder
)

# Alternative approach using shell for more precise control
# result = (
#     cq.Workplane("XY")
#     .circle(outer_diameter / 2)
#     .extrude(length)
#     .faces(">Z")
#     .workplane()
#     .circle(inner_diameter / 2)
#     .cutBlind(-length)
#     .faces(">Z")
#     .fillet(1.0)
#     .faces("<Z")
#     .fillet(1.0)
#     .transformed(rotate=cq.Vector(15, 0, 0))
# )