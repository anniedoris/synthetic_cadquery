import cadquery as cq
from math import pi, cos, sin

# Bolt dimensions
head_diameter = 10.0
head_height = 6.0
shaft_diameter = 6.0
shaft_length = 20.0
thread_pitch = 1.0
taper_length = 3.0
hex_height = 1.5

# Create the hexagonal head
head = cq.Workplane("XY").polygon(6, head_diameter).extrude(head_height)

# Create the cylindrical shaft with threads
shaft = cq.Workplane("XY").circle(shaft_diameter/2).extrude(shaft_length)

# Create threads using a helix
# We'll create a series of circles along the shaft to represent threads
thread_circles = []
for i in range(int(shaft_length / thread_pitch)):
    z_pos = i * thread_pitch
    thread_circles.append(
        cq.Workplane("XY", origin=(0, 0, z_pos))
        .circle(shaft_diameter/2 - 0.3)
        .extrude(0.2)
    )

# Combine threads with shaft
for circle in thread_circles:
    shaft = shaft.union(circle)

# Create the tapered end
taper_start = shaft_length - taper_length
taper_end = shaft_length
taper_radius = shaft_diameter/2 * 0.5

taper = (
    cq.Workplane("XY", origin=(0, 0, taper_start))
    .circle(shaft_diameter/2)
    .workplane(offset=taper_length)
    .circle(taper_radius)
    .loft(combine=True)
)

# Combine all parts
bolt = head.union(shaft).union(taper)

# Add chamfers to the hexagon edges
bolt = bolt.faces(">Z").edges().fillet(0.5)

# Create a slightly angled perspective (optional for visualization)
# This can be done by rotating the entire object
result = bolt.rotate((0, 0, 0), (1, 0, 0), 15)