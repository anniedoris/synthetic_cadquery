import cadquery as cq

# Define dimensions
base_length = 50.0
base_width = 30.0
base_height = 10.0
base_bottom_width = 35.0

circular_inner_diameter = 20.0
circular_outer_diameter = 25.0
circular_height = 5.0

clamp_length = 25.0
clamp_width = 15.0
clamp_height = 8.0
clamp_hole_diameter = 6.0

# Create the mounting base with trapezoidal side profile
# Start with a rectangular prism and offset the bottom
base = cq.Workplane("XY").box(base_length, base_width, base_height)

# Create the trapezoidal side profile by cutting a wedge from the bottom
# This creates the wider bottom
base = base.faces("<Y").workplane(offset=-base_height/2).rect(base_bottom_width, base_height, forConstruction=True).vertices().hole(base_height)

# Create the circular component (ring)
circular_component = (
    cq.Workplane("XY")
    .circle(circular_outer_diameter/2)
    .circle(circular_inner_diameter/2)
    .extrude(circular_height)
    .translate((0, 0, base_height))
)

# Create the clamp with through-hole
clamp = (
    cq.Workplane("XY")
    .rect(clamp_length, clamp_width)
    .extrude(clamp_height)
    .faces(">Z")
    .workplane()
    .circle(clamp_hole_diameter/2)
    .cutThruAll()
    .translate((0, 0, base_height + circular_height))
)

# Combine all parts
result = base.union(circular_component).union(clamp)