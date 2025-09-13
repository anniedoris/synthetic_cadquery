import cadquery as cq
from math import sin, cos, pi

# Parameters for the threaded ring/nut
outer_diameter = 20.0
inner_diameter = 12.0
height = 8.0
thread_pitch = 1.0
thread_height = 0.5
chamfer_distance = 1.0

# Create the outer cylinder
result = cq.Workplane("XY").circle(outer_diameter/2).extrude(height)

# Create the inner cylinder to make it hollow
result = result.faces("<Z").workplane().circle(inner_diameter/2).extrude(height)

# Create chamfer on top edge
result = result.faces(">Z").chamfer(chamfer_distance)

# Create internal threads using a helical sweep
# We'll create a thread profile and sweep it around the inner cylinder
thread_profile = cq.Workplane("XY").moveTo(inner_diameter/2, 0).lineTo(inner_diameter/2 - thread_height, 0).lineTo(inner_diameter/2 - thread_height, thread_pitch/2).lineTo(inner_diameter/2, thread_pitch/2).close()

# Create the helical thread pattern
# This is a simplified approach - in practice, you'd want a more complex thread profile
# For now, creating a basic helical groove
thread_sweep = cq.Workplane("XY").circle(inner_diameter/2 - thread_height/2).extrude(thread_pitch)

# Create multiple thread segments
thread_segments = []
for i in range(10):  # 10 thread turns
    angle = i * thread_pitch / (inner_diameter/2) * 360
    segment = thread_sweep.rotate((0, 0, 0), (0, 0, 1), angle)
    thread_segments.append(segment)

# Combine all thread segments
for segment in thread_segments:
    result = result.union(segment)

# Alternative approach using a more realistic thread creation method
# Let's build a proper thread pattern
result = cq.Workplane("XY").circle(outer_diameter/2).extrude(height)
result = result.faces("<Z").workplane().circle(inner_diameter/2).extrude(height)

# Add chamfer to top
result = result.faces(">Z").chamfer(chamfer_distance)

# Create a more accurate thread using a helical sweep approach
# Create a basic thread profile
thread_base = cq.Workplane("XY").circle(inner_diameter/2).extrude(height)

# For a better thread representation, let's use a simpler approach:
# Create a cylinder with a helical groove cut into it
# First create the basic nut shape
nut = cq.Workplane("XY").circle(outer_diameter/2).extrude(height)
nut = nut.faces("<Z").workplane().circle(inner_diameter/2).extrude(height)

# Chamfer the top
nut = nut.faces(">Z").chamfer(chamfer_distance)

# Create thread pattern using multiple cuts
# This is a simplified representation of internal threads
thread_depth = 0.3
thread_pitch = 1.0
thread_turns = int(height / thread_pitch) + 1

# Create thread grooves by cutting helical shapes
for i in range(thread_turns):
    # Create a circular cut at each thread position
    z_pos = i * thread_pitch
    if z_pos < height:
        thread_cut = cq.Workplane("XY", origin=(0, 0, z_pos)).circle(inner_diameter/2 - thread_depth).extrude(thread_pitch/2)
        # Rotate to create helical pattern
        thread_cut = thread_cut.rotate((0, 0, 0), (0, 0, 1), i * 360 / thread_turns)
        nut = nut.cut(thread_cut)

# Actually, let's use a cleaner approach with a more realistic thread pattern
result = cq.Workplane("XY").circle(outer_diameter/2).extrude(height)
result = result.faces("<Z").workplane().circle(inner_diameter/2).extrude(height)

# Chamfer the top edge
result = result.faces(">Z").chamfer(chamfer_distance)

# Create internal thread using a helical pattern
# Create a single thread profile
thread_profile = cq.Workplane("XY").moveTo(inner_diameter/2 - thread_height, 0).lineTo(inner_diameter/2, 0).lineTo(inner_diameter/2, thread_pitch/2).lineTo(inner_diameter/2 - thread_height, thread_pitch/2).close()

# Create multiple copies to form the thread
# Since CadQuery doesn't have a direct thread creation, we'll create a simplified representation
# by cutting helical grooves

# Create a rough thread representation with multiple circular cuts
# This creates a threaded appearance with the right pitch and depth
for i in range(15):
    angle = i * thread_pitch / (inner_diameter/2) * 360
    z_pos = i * thread_pitch
    if z_pos < height:
        # Create a rectangular cut to represent thread groove
        thread_cut = cq.Workplane("XY", origin=(0, 0, z_pos)).rect(thread_height*2, thread_pitch/2, centered=True).extrude(thread_pitch/4)
        thread_cut = thread_cut.rotate((0, 0, 0), (0, 0, 1), angle)
        result = result.cut(thread_cut)

# Simplified final version that better represents the requirements
result = cq.Workplane("XY").circle(outer_diameter/2).extrude(height)
result = result.faces("<Z").workplane().circle(inner_diameter/2).extrude(height)

# Add chamfer to top
result = result.faces(">Z").chamfer(chamfer_distance)

# For a more realistic thread, we'll create a single thread profile and rotate it
# This is a more accurate representation using extrusion with transformation
thread_depth = 0.3
thread_pitch = 1.0

# Create a series of helical grooves to represent threads
grooves = []
for i in range(12):  # 12 thread turns
    z_pos = i * thread_pitch
    if z_pos < height:
        # Create a circular groove at the correct depth
        groove = cq.Workplane("XY", origin=(0, 0, z_pos)).circle(inner_diameter/2 - thread_depth/2).extrude(thread_pitch/2)
        # Apply helical transformation (simplified)
        groove = groove.rotate((0, 0, 0), (0, 0, 1), i * 30)  # Rotate to create helix
        grooves.append(groove)

# Combine the grooves
for groove in grooves:
    result = result.cut(groove)

# Final simplified version that's more practical
result = cq.Workplane("XY").circle(outer_diameter/2).extrude(height)
result = result.faces("<Z").workplane().circle(inner_diameter/2).extrude(height)

# Chamfer top edge
result = result.faces(">Z").chamfer(chamfer_distance)

# Create a better thread representation by making a spiral cut
# Create the main solid
base_nut = cq.Workplane("XY").circle(outer_diameter/2).extrude(height)
base_nut = base_nut.faces("<Z").workplane().circle(inner_diameter/2).extrude(height)

# Create chamfer on top
base_nut = base_nut.faces(">Z").chamfer(chamfer_distance)

# For simplicity, create a basic threaded appearance using a helical cut
# We'll make a simple representation with a cutout pattern
result = base_nut

# Cut a spiral groove to represent threads
# This creates a simpler, more practical representation
for i in range(10):  # 10 thread turns
    z_pos = i * thread_pitch
    if z_pos < height - thread_pitch:
        # Create a spiral cut pattern
        thread_cut = cq.Workplane("XY", origin=(0, 0, z_pos)).circle(inner_diameter/2 - thread_height).extrude(thread_pitch)
        result = result.cut(thread_cut)