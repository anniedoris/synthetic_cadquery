import cadquery as cq
from math import pi, cos, sin

# Bolt and Nut Parameters
bolt_diameter = 8.0
head_diameter = 12.0
head_height = 5.0
thread_diameter = 6.0
thread_pitch = 1.25
thread_length = 20.0
nut_diameter = 14.0
nut_height = 8.0
hex_width = 10.0  # Across flats of hex nut

# Create the bolt head
bolt = cq.Workplane("XY").circle(head_diameter/2).extrude(head_height)

# Create the threaded portion
threaded_part = (
    cq.Workplane("XY")
    .circle(thread_diameter/2)
    .extrude(thread_length)
)

# Create the shank (smooth portion between head and threads)
shank = (
    cq.Workplane("XY")
    .circle(bolt_diameter/2)
    .extrude(2)
)

# Combine the bolt components
bolt = bolt.union(shank).union(threaded_part)

# Create the hexagonal nut
# Create a hexagon
hex_points = []
for i in range(6):
    angle = pi/3 * i
    x = hex_width/2 * cos(angle)
    y = hex_width/2 * sin(angle)
    hex_points.append((x, y))

# Create the hexagonal profile
nut_profile = (
    cq.Workplane("XY")
    .polyline(hex_points)
    .close()
    .extrude(nut_height)
)

# Create internal threads in the nut
# Create a cylinder to subtract for the threaded hole
nut_hole = (
    cq.Workplane("XY")
    .circle(thread_diameter/2)
    .extrude(nut_height + 1)
)

# Subtract the hole from the nut
nut = nut_profile.cut(nut_hole)

# Position the nut above the bolt
bolt = bolt.translate((0, 0, head_height + 2))

# Combine bolt and nut
result = bolt.union(nut)