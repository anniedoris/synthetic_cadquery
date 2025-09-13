import cadquery as cq

# Define dimensions
outer_diameter = 50.0
inner_diameter = 10.0
hole_diameter = 3.0
thickness = 5.0
edge_height = 1.0

# Create the octagonal plate with central hole
result = (
    cq.Workplane("XY")
    .polygon(8, outer_diameter/2)
    .circle(inner_diameter/2)
    .extrude(thickness)
)

# Add raised edges around the perimeter
result = (
    result.faces(">Z")
    .workplane()
    .polygon(8, outer_diameter/2)
    .extrude(edge_height)
)

# Add the 8 perimeter holes
result = (
    result.faces(">Z")
    .workplane()
    .rarray(outer_diameter/2 * 0.707, outer_diameter/2 * 0.707, 8, 1, center=True)
    .circle(hole_diameter/2)
    .cutThruAll()
)

# Add the central hole
result = (
    result.faces(">Z")
    .workplane()
    .circle(inner_diameter/2)
    .cutThruAll()
)