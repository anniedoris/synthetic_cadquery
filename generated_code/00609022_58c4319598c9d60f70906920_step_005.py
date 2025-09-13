import cadquery as cq

# Create the main body with dome and cylindrical transition
# Start with a workplane at the base
result = cq.Workplane("XY")

# Create the dome shape - flattened sphere at the top
# We'll create a series of cross-sections and loft them together
# Base circle for the dome
dome_radius = 10.0
cylinder_radius = 8.0
cylinder_length = 12.0
protrusion_radius = 4.0
protrusion_length = 6.0

# Create the main body by lofting cross-sections
# Base circle
base_circle = cq.Workplane("XY").circle(dome_radius).val()

# Mid circle (transition to cylinder)
mid_circle = cq.Workplane("XY").circle(cylinder_radius).val()

# Top circle (flattened dome)
top_circle = cq.Workplane("XY").circle(dome_radius * 0.8).val()

# Create a lofted surface from these sections
# We'll create a more detailed loft with intermediate sections
main_body = (
    cq.Workplane("XY")
    .circle(dome_radius)
    .workplane(offset=2)
    .circle(cylinder_radius * 0.9)
    .workplane(offset=4)
    .circle(cylinder_radius * 0.8)
    .workplane(offset=6)
    .circle(cylinder_radius)
    .workplane(offset=8)
    .circle(cylinder_radius)
    .workplane(offset=10)
    .circle(cylinder_radius * 0.9)
    .workplane(offset=12)
    .circle(dome_radius * 0.8)
    .loft(combine=True)
)

# Create the protrusion
protrusion = (
    cq.Workplane("XY")
    .moveTo(12, 0)
    .circle(protrusion_radius)
    .workplane(offset=1)
    .circle(protrusion_radius * 0.8)
    .workplane(offset=2)
    .circle(protrusion_radius * 0.6)
    .workplane(offset=3)
    .circle(protrusion_radius * 0.4)
    .workplane(offset=4)
    .circle(protrusion_radius * 0.2)
    .workplane(offset=5)
    .circle(0.1)
    .loft(combine=True)
)

# Combine the main body and protrusion
result = main_body.union(protrusion)

# Add a smooth transition fillet between the main body and protrusion
# This would be more complex in practice but we'll keep it simple for this example

# Let's simplify and create a cleaner version with better control
result = (
    cq.Workplane("XY")
    .circle(10)  # Base of main body
    .workplane(offset=2)
    .circle(8.5)  # Mid section
    .workplane(offset=4)
    .circle(8)  # Cylindrical section
    .workplane(offset=10)
    .circle(8)  # Continue cylinder
    .workplane(offset=12)
    .circle(8.5)  # Back to larger radius
    .workplane(offset=14)
    .circle(10)  # Top of dome
    .loft(combine=True)
    .faces(">Z")
    .workplane()
    .circle(4)
    .workplane(offset=1)
    .circle(3)
    .workplane(offset=2)
    .circle(2)
    .workplane(offset=3)
    .circle(1)
    .loft(combine=True)
    .translate((0, 0, 0))
)