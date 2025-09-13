import cadquery as cq

# Parameters for the open ring
outer_diameter = 20.0
thickness = 2.0
gap_size = 2.0
ring_angle = 340.0  # degrees (slightly less than 360 for the gap)

# Calculate radii
outer_radius = outer_diameter / 2.0
inner_radius = outer_radius - thickness

# Create the open ring by:
# 1. Creating a circular profile with the outer radius
# 2. Cutting a section out to create the gap
# 3. Extruding to create the 3D shape

# Create the base ring profile (partial circle)
ring_profile = (
    cq.Workplane("XY")
    .center(0, 0)
    .circle(outer_radius)
    .center(0, 0)
    .circle(inner_radius)
    .extrude(1.0)
)

# Create a cutting wedge to remove the gap
# The wedge should be slightly larger than the gap
wedge = (
    cq.Workplane("XY")
    .center(0, 0)
    .moveTo(outer_radius, 0)
    .lineTo(outer_radius + 1.0, 0)
    .lineTo(outer_radius + 1.0, gap_size/2)
    .lineTo(outer_radius, gap_size/2)
    .close()
    .extrude(1.0)
)

# Cut the gap from the ring
result = ring_profile.cut(wedge)

# Since we want a more realistic open ring with a gap in the circular path,
# let's use a different approach - create a full circle and then cut a small arc
# to simulate the gap in the ring

# Create the full ring with circular cross-section
full_ring = (
    cq.Workplane("XY")
    .circle(outer_radius)
    .extrude(1.0)
    .faces(">Z")
    .workplane()
    .circle(inner_radius)
    .extrude(1.0)
)

# Create a rectangular cut to simulate the gap
cut_rect = (
    cq.Workplane("XY")
    .center(outer_radius - thickness/2, 0)
    .rect(thickness, gap_size)
    .extrude(1.0)
)

# Apply the cut to create the gap
result = full_ring.cut(cut_rect)

# Make the ring truly open by creating a proper arc gap
# Create the ring with a partial circle
result = (
    cq.Workplane("XY")
    .center(0, 0)
    .circle(outer_radius)
    .center(0, 0)
    .circle(inner_radius)
    .extrude(1.0)
)

# Create the gap by cutting a section from the ring
# Create a workplane at the top face and make a rectangular cut
result = (
    result.faces(">Z")
    .workplane()
    .center(outer_radius - thickness/2, 0)
    .rect(thickness, gap_size)
    .cutThruAll()
)

# Better approach: Create a torus and cut a section out
# Create a circular arc profile and sweep it to make the ring
# But let's simplify to create a proper open ring

# Create the ring as a swept profile
# Start with a circle profile
ring_cross_section = cq.Workplane("XY").circle(outer_radius).circle(inner_radius)

# Create a path that's a partial circle
# For an open ring with gap, we'll create a path with a gap
# Use a more direct approach

# Create a solid ring with uniform thickness and a gap
# This is the most straightforward way:
result = (
    cq.Workplane("XY")
    .circle(outer_radius)
    .circle(inner_radius)
    .extrude(1.0)
    .faces(">Z")
    .workplane()
    .rect(thickness, gap_size)
    .cutThruAll()
)

# Actually, let's make a proper open ring with the gap as a section removed
# Create the outer circle and inner circle, then subtract a small section
# to create the gap

# Create a full ring
ring = cq.Workplane("XY").circle(outer_radius).circle(inner_radius).extrude(1.0)

# Create a wedge to cut out the gap
gap_wedge = (
    cq.Workplane("XY")
    .moveTo(outer_radius, 0)
    .lineTo(outer_radius, gap_size)
    .lineTo(outer_radius - gap_size, gap_size)
    .lineTo(outer_radius - gap_size, 0)
    .close()
    .extrude(1.0)
)

# Cut the gap
result = ring.cut(gap_wedge)