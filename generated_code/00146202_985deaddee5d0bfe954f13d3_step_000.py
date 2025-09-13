import cadquery as cq
from math import pi, cos, sin

# Dimensions
hex_socket_width = 10.0
hex_socket_depth = 3.0
cylinder_diameter = 12.0
cylinder_height = 8.0
thread_pitch = 1.5
thread_height = 0.5
thread_outer_diameter = cylinder_diameter
thread_inner_diameter = cylinder_diameter - 2 * thread_height
red_line_diameter = 2.0
red_line_height = 2.0

# Create the base workplane
result = cq.Workplane("XY")

# Create the hexagonal socket
hexagon = result.polygon(6, hex_socket_width)
hexagon = hexagon.extrude(hex_socket_depth)

# Create the cylindrical body
cylinder = hexagon.faces(">Z").workplane().circle(cylinder_diameter/2).extrude(cylinder_height)

# Create the threads
# We'll create a helical thread pattern by creating a series of cuts
thread_cut = cq.Workplane("XY").circle(thread_inner_diameter/2).extrude(thread_height)
thread_cut = thread_cut.faces(">Z").workplane().circle(thread_outer_diameter/2).cutThruAll()

# Create the thread pattern using a spiral
thread_pattern = cq.Workplane("XY").circle(thread_outer_diameter/2).extrude(thread_height)
thread_pattern = thread_pattern.faces(">Z").workplane().circle(thread_inner_diameter/2).cutThruAll()

# Create the helical thread pattern by revolving the thread cut
thread_revolve = cq.Workplane("XY").circle(thread_inner_diameter/2).extrude(thread_height)
thread_revolve = thread_revolve.faces(">Z").workplane().circle(thread_outer_diameter/2).cutThruAll()

# Instead of a complex helical pattern, let's create a simpler thread representation
# by cutting grooves around the cylinder
threads = cylinder
for i in range(8):  # 8 threads around the cylinder
    angle = i * (2 * pi / 8)
    x = (thread_outer_diameter/2 - thread_height) * cos(angle)
    y = (thread_outer_diameter/2 - thread_height) * sin(angle)
    threads = threads.faces("<Z").workplane(offset=-thread_height/2).moveTo(x, y).rect(thread_height, thread_height).cutThruAll()

# Add the red lines within the cylindrical body
red_lines = threads.faces("<Z").workplane(offset=-cylinder_height/2 + red_line_height/2).circle(red_line_diameter/2).extrude(red_line_height)

# Combine everything
result = red_lines

# Add the base hex socket
result = result.union(hexagon)

# Final result
result = result