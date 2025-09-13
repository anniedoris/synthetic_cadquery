import cadquery as cq
from math import sin, cos, pi

# Parameters for the screw
head_diameter = 6.0
head_height = 2.0
shaft_diameter = 3.0
shaft_length = 20.0
thread_length = 12.0
point_diameter = 1.0
point_length = 3.0

# Create the head (dome shape)
head = cq.Workplane("XY").circle(head_diameter/2).extrude(head_height)

# Create the cylindrical shaft
shaft = (
    cq.Workplane("XY", origin=(0, 0, head_height))
    .circle(shaft_diameter/2)
    .extrude(shaft_length)
)

# Combine head and shaft
screw = head.union(shaft)

# Create the threaded section using a helical profile
# Define thread parameters
thread_pitch = 0.5
thread_height = 0.2
thread_width = 0.3

# Create thread profile
def create_thread_profile():
    # Create a V-shaped thread profile
    thread_profile = (
        cq.Workplane("XY")
        .moveTo(-thread_width/2, 0)
        .lineTo(0, thread_height)
        .lineTo(thread_width/2, 0)
        .close()
    )
    return thread_profile

# Create the threaded section with helical extrusion
threaded_section = (
    cq.Workplane("XY", origin=(0, 0, head_height + shaft_length - thread_length))
    .circle(shaft_diameter/2)
    .extrude(thread_length, both=True)
)

# For a more realistic thread, we'll create a helical groove
# Create a simple helical thread pattern using a swept profile
thread_profile = (
    cq.Workplane("XY")
    .moveTo(-thread_width/2, 0)
    .lineTo(0, thread_height)
    .lineTo(thread_width/2, 0)
    .close()
)

# Create a helical path for the thread
# For simplicity, we'll make a rough thread representation
# by creating a series of filleted rectangles along a helical path

# Instead, let's use a more practical approach with a cylinder with grooves
# Create the main shaft with a thread-like appearance using fillets
threaded_screw = screw

# Create the point at the end
point = (
    cq.Workplane("XY", origin=(0, 0, head_height + shaft_length))
    .circle(point_diameter/2)
    .extrude(point_length)
    .faces(">Z")
    .workplane()
    .circle(point_diameter/2 * 0.5)
    .extrude(point_length/2)
    .faces(">Z")
    .workplane()
    .circle(point_diameter/2 * 0.2)
    .extrude(point_length/4)
)

# Final assembly
result = threaded_screw.union(point)

# Add thread-like features by creating grooves
# Create thread grooves around the shaft
thread_grooves = (
    cq.Workplane("XY", origin=(0, 0, head_height))
    .circle(shaft_diameter/2 - 0.1)
    .extrude(thread_length)
    .faces(">Z")
    .workplane()
    .circle(shaft_diameter/2 - 0.3)
    .extrude(thread_length)
)

# Simplified approach - create the basic structure
# Create the full screw with head, shaft, threaded section, and point
result = (
    cq.Workplane("XY")
    .circle(head_diameter/2)
    .extrude(head_height)
    .faces(">Z")
    .workplane()
    .circle(shaft_diameter/2)
    .extrude(shaft_length)
    .faces(">Z")
    .workplane()
    .circle(shaft_diameter/2)
    .extrude(thread_length)
    .faces(">Z")
    .workplane()
    .circle(point_diameter/2)
    .extrude(point_length)
    .faces(">Z")
    .workplane()
    .circle(point_diameter/2 * 0.5)
    .extrude(point_length/2)
    .faces(">Z")
    .workplane()
    .circle(point_diameter/2 * 0.2)
    .extrude(point_length/4)
)