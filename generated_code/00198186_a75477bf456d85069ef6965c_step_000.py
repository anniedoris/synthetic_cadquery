import cadquery as cq

# Define dimensions
ring_outer_diameter = 20.0
ring_thickness = 4.0
shaft_diameter = 6.0
shaft_length = ring_outer_diameter

# Create the ring (torus-like shape)
# First, create a circle for the ring cross-section
ring_circle = cq.Workplane("XY").circle(ring_outer_diameter/2 - ring_thickness/2)

# Then revolve it around the Z axis to create the torus
ring = ring_circle.revolve(360, (0, 0, 0), (0, 0, 1))

# Create the shaft
# Start with a workplane on the top face of the ring
shaft_workplane = (
    cq.Workplane("XY")
    .box(ring_outer_diameter, ring_outer_diameter, ring_thickness)
    .faces(">Z")
    .workplane()
)

# Create the shaft cylinder
shaft = shaft_workplane.circle(shaft_diameter/2).extrude(shaft_length)

# Position the shaft to connect with the ring
# Move the shaft to the center of the ring and extend it outward
shaft = shaft.translate((0, 0, ring_thickness/2 + shaft_length/2))

# Combine the ring and shaft
result = ring.union(shaft)