import cadquery as cq
from math import pi, cos, sin

# Bolt dimensions
bolt_diameter = 8.0
flange_diameter = 16.0
flange_height = 2.0
base_diameter = 12.0
base_height = 1.0
shaft_length = 20.0
thread_pitch = 1.25
thread_height = 0.625
hex_width = 10.0
hex_height = 8.0

# Create the shaft with threads
shaft = cq.Workplane("XY").circle(bolt_diameter/2).extrude(shaft_length)

# Create the hex flange
flange = cq.Workplane("XY").circle(flange_diameter/2).extrude(flange_height)

# Create the circular base
base = cq.Workplane("XY").circle(base_diameter/2).extrude(base_height)

# Position the flange on top of the shaft
flange = flange.translate((0, 0, shaft_length))

# Position the base below the shaft
base = base.translate((0, 0, -base_height))

# Combine the parts
result = shaft.union(flange).union(base)

# Create threads on the shaft
# We'll create a helical thread pattern using a revolved profile
thread_profile = cq.Workplane("XZ").lineTo(thread_height, 0).lineTo(0, thread_height/2).lineTo(-thread_height, 0).close().revolve(360, (-thread_height, 0), (thread_height, 0))

# Position and add thread to the shaft
thread = thread_profile.translate((0, 0, 0))
for i in range(int(shaft_length/thread_pitch)):
    thread = thread.union(thread_profile.translate((0, 0, i*thread_pitch)))

# Subtract the thread from the shaft
result = result.cut(thread)

# Create hexagonal flange using a polygon
hex_flange = cq.Workplane("XY").polygon(6, hex_width).extrude(flange_height)
hex_flange = hex_flange.translate((0, 0, shaft_length))

# Replace the circular flange with hexagonal flange
result = result.cut(flange)
result = result.union(hex_flange)

# Add a small fillet between base and shaft for smooth transition
result = result.edges("|Z").fillet(0.5)

# Make sure the final result is properly constructed
result = result.val()

# Create the final bolt assembly
result = cq.Workplane("XY").box(10, 10, 10).cut(result)