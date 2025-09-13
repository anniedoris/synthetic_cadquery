import cadquery as cq

# Create a rhombus shape with perspective effect
# Using a polygon with 4 sides, but offsetting points to create perspective
result = (
    cq.Workplane("front")
    .polygon(4, 2.0)  # Create a square (rhombus) with side length 2.0
    .transformed(offset=cq.Vector(0, 0, 0), rotate=cq.Vector(15, 10, 0))  # Add perspective rotation
    .extrude(0.1)  # Add minimal thickness to make it visible
)