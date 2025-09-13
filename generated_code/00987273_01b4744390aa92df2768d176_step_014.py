import cadquery as cq
from math import pi, cos, sin

# Parameters for the threaded cylindrical component
diameter = 10.0
length = 30.0
thread_pitch = 1.0
thread_height = 0.3
hexagon_diameter = 6.0
hexagon_depth = 2.0
shoulder_diameter = 12.0
shoulder_length = 2.0

# Create the main cylindrical body
result = cq.Workplane("XY").circle(diameter/2).extrude(length)

# Create the hexagonal socket at one end
hexagon_radius = hexagon_diameter / 2
result = (
    result.faces("<Z")
    .workplane()
    .polygon(6, hexagon_diameter)
    .cutBlind(-hexagon_depth)
)

# Create the shoulder at the other end
result = (
    result.faces(">Z")
    .workplane()
    .circle(shoulder_diameter/2)
    .extrude(shoulder_length)
)

# Create external threads using a helix approach
# Create a thread profile
thread_profile = cq.Workplane("XY").circle(thread_height/2).extrude(thread_pitch)

# Create multiple copies of the thread profile around the cylinder
thread_count = int(length / thread_pitch)
for i in range(thread_count):
    angle = i * thread_pitch / (diameter * pi) * 360
    result = result.union(
        thread_profile.rotate((0, 0, 0), (0, 0, 1), angle)
        .translate((0, 0, i * thread_pitch))
    )

# Alternative approach using a more accurate thread generation
# Create a helical thread using a helix sweep
# For a simpler representation, we'll create a basic thread pattern
# Create thread grooves on the surface
thread_grooves = cq.Workplane("XY").circle(diameter/2 - thread_height).extrude(thread_height)
thread_grooves = thread_grooves.faces(">Z").workplane().polygon(8, 1.0).extrude(-0.1)

# Instead of complex helix generation, we'll create a simplified thread pattern
# by adding cylindrical cutouts along the length at intervals
for i in range(10):
    z_pos = i * thread_pitch
    result = (
        result.faces(">Z")
        .workplane(offset=z_pos)
        .circle(thread_height/2)
        .cutBlind(-thread_height)
    )

# Add the raised ring or lip near the hexagonal socket
result = (
    result.faces("<Z")
    .workplane(offset=-0.5)
    .circle(diameter/2 + 0.5)
    .extrude(0.5)
)

# Clean up the model by removing small features and ensuring proper geometry
result = result.faces(">Z").edges().fillet(0.1)
result = result.faces("<Z").edges().fillet(0.1)

# Create a more accurate thread representation using a helical sweep
# This is a simplified approach to represent threads
# Create a basic thread pattern that wraps around the cylinder
thread_pattern = cq.Workplane("XY").rect(0.2, 0.5).extrude(0.2)
thread_pattern = thread_pattern.rotate((0, 0, 0), (0, 0, 1), 45)

# Add a more realistic thread representation using multiple cuts
# Create the main body again for clean thread generation
result = cq.Workplane("XY").circle(diameter/2).extrude(length)

# Create thread grooves using a more precise approach
thread_radius = diameter/2 - thread_height
for i in range(20):
    angle = i * 18
    x = thread_radius * cos(angle * pi/180)
    y = thread_radius * sin(angle * pi/180)
    result = (
        result.faces(">Z")
        .workplane(offset=i * thread_pitch/20)
        .center(x, y)
        .circle(thread_height/2)
        .cutBlind(-thread_height/2)
    )

# Add the hexagonal socket
result = (
    result.faces("<Z")
    .workplane()
    .polygon(6, hexagon_diameter)
    .cutBlind(-hexagon_depth)
)

# Add the shoulder at the opposite end
result = (
    result.faces(">Z")
    .workplane()
    .circle(shoulder_diameter/2)
    .extrude(shoulder_length)
)

# Add the raised ring
result = (
    result.faces("<Z")
    .workplane(offset=-0.5)
    .circle(diameter/2 + 0.5)
    .extrude(0.5)
)

# Final cleanup to make the model look clean
result = result.edges("|Z").fillet(0.1)
result = result.faces(">Z").edges().fillet(0.1)
result = result.faces("<Z").edges().fillet(0.1)