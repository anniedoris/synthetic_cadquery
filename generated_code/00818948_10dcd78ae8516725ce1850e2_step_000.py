import cadquery as cq
from math import pi, cos, sin

# Define dimensions
head_diameter = 10.0
head_height = 6.0
shaft_diameter = 6.0
shaft_length = 30.0
thread_pitch = 1.0
thread_height = 0.5
tip_diameter = 4.0
tip_length = 3.0

# Create the hexagonal head
head = cq.Workplane("XY").polygon(6, head_diameter).extrude(head_height)

# Create the threaded shaft
# We'll create a cylinder and then add helical threads
shaft = cq.Workplane("XY").circle(shaft_diameter/2).extrude(shaft_length)

# Create the unthreaded tip
tip = cq.Workplane("XY").circle(tip_diameter/2).extrude(tip_length)

# Position the tip at the end of the shaft
tip = tip.translate((0, 0, shaft_length))

# Combine the parts
bolt = head.union(shaft).union(tip)

# For the threading effect, we'll create a helical groove pattern
# This is a simplified representation - in practice, you'd want more detailed thread geometry
# Create thread grooves using a cylindrical pattern
thread_grooves = cq.Workplane("XY").circle(shaft_diameter/2 - thread_height).extrude(shaft_length)

# For a more realistic approach, we'll create a helical cut using a spline path
# This is a simplified approximation of threads
thread_cut = cq.Workplane("XY").circle(shaft_diameter/2 - thread_height).extrude(shaft_length)

# Create the actual bolt with threads (simplified approach)
# We'll create the bolt with the main shaft and then subtract thread-like features
bolt = (
    cq.Workplane("XY")
    .polygon(6, head_diameter)
    .extrude(head_height)
    .faces(">Z")
    .workplane()
    .circle(shaft_diameter/2)
    .extrude(shaft_length)
    .faces(">Z")
    .workplane()
    .circle(tip_diameter/2)
    .extrude(tip_length)
)

# For the threads, we'll create a more realistic approach using a helical sweep
# Create the hexagonal head
head = cq.Workplane("XY").polygon(6, head_diameter).extrude(head_height)

# Create the threaded shaft with a cylindrical form
shaft = cq.Workplane("XY").circle(shaft_diameter/2).extrude(shaft_length)

# Create the unthreaded tip
tip = cq.Workplane("XY").circle(tip_diameter/2).extrude(tip_length)

# Position the tip at the end of the shaft
tip = tip.translate((0, 0, shaft_length))

# Combine all parts
result = head.union(shaft).union(tip)

# Apply color to head (gray) and shaft (red) - note: color is for visualization only in CadQuery
# In a real CAD environment, you'd apply materials
result = result.faces(">Z").workplane().circle(shaft_diameter/2).extrude(0.1)