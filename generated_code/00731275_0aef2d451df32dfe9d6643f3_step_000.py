import cadquery as cq
from math import pi, cos, sin

# Parameters for the assembly
ring_radius = 50.0
ring_thickness = 5.0
hub_radius = 15.0
hub_thickness = 10.0
support_width = 3.0
support_height = 20.0
support_thickness = 2.0
num_supports = 8
arm_length = 30.0
arm_radius = 5.0
detachable_radius = 3.0
detachable_length = 8.0

# Create the semi-circular ring
ring = cq.Workplane("XY").circle(ring_radius).extrude(ring_thickness)

# Create the inner cutout for the ring
inner_cutout = cq.Workplane("XY").circle(ring_radius - ring_thickness).extrude(ring_thickness + 0.1)

# Subtract the inner cutout from the ring
ring = ring.cut(inner_cutout)

# Create the central hub
hub = cq.Workplane("XY").circle(hub_radius).extrude(hub_thickness)

# Create the hollow center of the hub
hub_hole = cq.Workplane("XY").circle(hub_radius * 0.4).extrude(hub_thickness + 0.1)
hub = hub.cut(hub_hole)

# Create radial supports
supports = cq.Workplane("XY")
for i in range(num_supports):
    angle = 2 * pi * i / num_supports
    x = hub_radius * cos(angle)
    y = hub_radius * sin(angle)
    
    # Create support
    support = cq.Workplane("XY", origin=(x, y, 0)).rect(support_width, support_height).extrude(support_thickness)
    
    # Rotate support to align with radial direction
    support = support.rotate((0, 0, 0), (0, 0, 1), angle * 180 / pi)
    
    # Position support at the right location
    support = support.translate((0, 0, hub_thickness/2 - support_thickness/2))
    
    supports = supports.union(support)

# Combine ring and hub with supports
assembly = ring.union(hub).union(supports)

# Create extending arms
arms = cq.Workplane("XY")
for i in range(2):
    # Position arms on the left side
    arm_offset = -ring_radius + 10 if i == 0 else -ring_radius + 10 + 15
    arm = cq.Workplane("XY", origin=(arm_offset, 0, 0)).circle(arm_radius).extrude(arm_length)
    arm = arm.rotate((0, 0, 0), (0, 1, 0), 90)
    arms = arms.union(arm)

# Add the arms to the assembly
assembly = assembly.union(arms)

# Create detachable component
detachable = cq.Workplane("XY", origin=(-ring_radius + 15, -10, 0)).circle(detachable_radius).extrude(detachable_length)
assembly = assembly.union(detachable)

# Position the assembly in the right orientation
result = assembly.rotate((0, 0, 0), (0, 0, 1), 90)

# Add mounting points to the ring
for i in range(8):
    angle = 2 * pi * i / 8
    x = ring_radius * cos(angle)
    y = ring_radius * sin(angle)
    
    # Add mounting holes to the ring
    mounting_hole = cq.Workplane("XY", origin=(x, y, 0)).circle(1.5).extrude(ring_thickness + 0.1)
    result = result.cut(mounting_hole)

# Add mounting points to the hub
for i in range(6):
    angle = 2 * pi * i / 6
    x = hub_radius * cos(angle)
    y = hub_radius * sin(angle)
    
    # Add mounting holes to the hub
    mounting_hole = cq.Workplane("XY", origin=(x, y, 0)).circle(1.0).extrude(hub_thickness + 0.1)
    result = result.cut(mounting_hole)