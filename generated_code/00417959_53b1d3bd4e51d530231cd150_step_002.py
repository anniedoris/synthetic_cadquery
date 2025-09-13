import cadquery as cq
from math import sin, cos, pi

# Parameters for the hex socket head cap screw
head_diameter = 6.0
head_height = 3.0
hex_socket_diameter = 4.0
hex_socket_depth = 1.5
shank_diameter = 3.0
shank_length = 20.0
thread_pitch = 0.5
thread_length = shank_length
tip_taper_length = 2.0
tip_diameter = 0.5

# Create the head with hex socket
head = cq.Workplane("XY").circle(head_diameter/2).extrude(head_height)

# Create the hex socket
hex_radius = hex_socket_diameter / 2
hex_points = []
for i in range(6):
    angle = i * pi / 3
    x = hex_radius * cos(angle)
    y = hex_radius * sin(angle)
    hex_points.append((x, y))

# Create hex socket face
hex_face = cq.Workplane("XY").polyline(hex_points).close().extrude(-hex_socket_depth)

# Combine head and hex socket
result = head.union(hex_face)

# Create the shank with threads
shank = cq.Workplane("XY").circle(shank_diameter/2).extrude(shank_length)

# Add threads to the shank
thread_points = []
for i in range(0, int(thread_length/thread_pitch)*2):
    angle = i * pi
    x = shank_diameter/2 * 0.9 * cos(angle)
    y = shank_diameter/2 * 0.9 * sin(angle)
    thread_points.append((x, y))

# Create thread profile
thread_profile = cq.Workplane("XY").polyline(thread_points).close()

# Create thread extrusion
thread_extrusion = thread_profile.extrude(thread_pitch/2)
threaded_shank = shank.union(thread_extrusion)

# Combine head and shank
result = result.union(threaded_shank)

# Create tip taper
tip_start = cq.Workplane("XY").circle(shank_diameter/2).extrude(-tip_taper_length)
tip_end = cq.Workplane("XY").circle(tip_diameter/2).extrude(-tip_taper_length)

# Create the tip
tip = tip_start.cut(tip_end)
result = result.union(tip)

# Move the result to the correct position
result = result.translate((0, 0, -shank_length - head_height - tip_taper_length))