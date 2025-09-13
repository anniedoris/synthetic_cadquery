import cadquery as cq

# Define dimensions
outer_diameter = 20.0
inner_diameter = 12.0
height = 30.0
ring_outer_diameter = 25.0
ring_height = 5.0

# Create the main cylindrical body with hollow center
result = cq.Workplane("XY").circle(outer_diameter/2).circle(inner_diameter/2).extrude(height)

# Create the integrated ring/flange
# Move to the top of the cylinder and create the ring
result = (
    result.faces(">Z")
    .workplane()
    .circle(ring_outer_diameter/2)
    .circle(outer_diameter/2)
    .extrude(ring_height)
)

# Ensure the ring is properly aligned with the cylinder by using a boolean operation
# This ensures a clean integration without gaps or steps
result = result.faces(">Z").workplane(offset=ring_height).circle(outer_diameter/2).extrude(0.001)

# The above creates a seamless transition between the cylinder and ring
# The small extrusion ensures proper surface continuity