import cadquery as cq
from math import pi, sin, cos

# Bolt parameters
head_diameter = 6.0
head_height = 3.0
shaft_diameter = 4.0
shaft_length = 10.0
thread_diameter = 4.0
thread_length = 8.0
thread_pitch = 0.8
thread_height = 0.4

# Create the bolt head
bolt = cq.Workplane("XY").circle(head_diameter/2).extrude(head_height)

# Create the shaft
bolt = bolt.faces(">Z").workplane().circle(shaft_diameter/2).extrude(shaft_length)

# Create the threaded portion
threaded_section = cq.Workplane("XY").circle(thread_diameter/2).extrude(thread_length)

# Create threads using a helix approach
# We'll create a series of cylinders to simulate the threads
thread_cylinders = cq.Workplane("XY").circle(thread_diameter/2 - thread_height).extrude(thread_length)

# Create a helical thread pattern
# This is a simplified representation - in reality, threads would be more complex
# We'll create a series of grooves to represent the thread profile
for i in range(int(thread_length/thread_pitch)):
    angle = i * thread_pitch / thread_diameter * 2 * pi
    thread_cut = (
        cq.Workplane("XY")
        .moveTo(thread_diameter/2 - thread_height, 0)
        .lineTo(thread_diameter/2 - thread_height, thread_height)
        .lineTo(thread_diameter/2 - thread_height/2, thread_height)
        .lineTo(thread_diameter/2 - thread_height/2, 0)
        .close()
        .extrude(thread_length)
        .rotate((0, 0, 0), (0, 0, 1), angle)
    )
    bolt = bolt.cut(thread_cut)

# Position the threaded section at the end of the shaft
bolt = bolt.faces(">Z").workplane(offset=shaft_length).union(threaded_section)

# Create a more realistic bolt with a hexagonal head
# Create the bolt head with hexagonal profile
hex_head = cq.Workplane("XY").polygon(6, head_diameter/2).extrude(head_height)

# Add a cylindrical shaft to the hex head
hex_shaft = cq.Workplane("XY").circle(shaft_diameter/2).extrude(shaft_length)

# Add threaded portion
threaded_shaft = cq.Workplane("XY").circle(thread_diameter/2).extrude(thread_length)

# Combine all parts
result = hex_head.union(hex_shaft).union(threaded_shaft)

# Center the bolt
result = result.translate((0, 0, -head_height - shaft_length - thread_length/2))