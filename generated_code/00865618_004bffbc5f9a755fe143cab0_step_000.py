import cadquery as cq

# Dimensions
outer_diameter = 50.0
inner_diameter = 10.0
perimeter_hole_diameter = 4.0
num_perimeter_holes = 8
thickness = 5.0

# Create the plate
result = (
    cq.Workplane("XY")
    .circle(outer_diameter / 2.0)  # Outer circle
    .circle(inner_diameter / 2.0)   # Inner circle (central hole)
    .extrude(thickness)             # Give it thickness
)

# Add perimeter holes
result = (
    result.faces(">Z")
    .workplane()
    .rarray(outer_diameter / 2.0 - perimeter_hole_diameter, 
            outer_diameter / 2.0 - perimeter_hole_diameter, 
            num_perimeter_holes, 1, True)
    .circle(perimeter_hole_diameter / 2.0)
    .cutThruAll()
)

# Add the central hole through the entire thickness
result = (
    result.faces(">Z")
    .workplane()
    .circle(inner_diameter / 2.0)
    .cutThruAll()
)