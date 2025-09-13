import cadquery as cq
from math import pi, sin, cos

# Bottle dimensions
bottle_height = 200.0
body_height = 160.0
neck_height = 30.0
neck_diameter = 12.0
body_diameter = 60.0
cork_height = 8.0
cork_diameter = 10.0
thread_depth = 2.0
thread_pitch = 4.0
thread_count = 6

# Create the main body of the bottle
# Start with a workplane at the bottom
body = cq.Workplane("XY").circle(body_diameter/2).extrude(body_height)

# Create the neck
neck = cq.Workplane("XY", origin=(0, 0, body_height)).circle(neck_diameter/2).extrude(neck_height)

# Combine body and neck
bottle = body.union(neck)

# Create the cork area
cork_base = cq.Workplane("XY", origin=(0, 0, body_height + neck_height)).circle(cork_diameter/2).extrude(cork_height)

# Create threading on the cork
threading = cq.Workplane("XY", origin=(0, 0, body_height + neck_height + cork_height)).circle(cork_diameter/2).extrude(thread_depth)

# Create the actual threads
for i in range(thread_count):
    angle = (i * 2 * pi) / thread_count
    x = (cork_diameter/2 - thread_depth/2) * cos(angle)
    y = (cork_diameter/2 - thread_depth/2) * sin(angle)
    thread = cq.Workplane("XY", origin=(x, y, body_height + neck_height + cork_height)).circle(thread_pitch/4).extrude(thread_depth)
    threading = threading.union(thread)

# Combine all parts
bottle = bottle.union(cork_base).union(threading)

# Create a smooth, rounded shape for the bottle body using a blend
# Create a more realistic bottle shape with a smooth curve
bottle_shape = cq.Workplane("XY").center(0, 0).rect(body_diameter, body_diameter, forConstruction=True).vertices().circle(body_diameter/2).extrude(body_height)

# Add the neck and cork
result = bottle_shape.union(neck).union(cork_base)

# Create a more realistic bottle shape using a spline
# Create a workplane for the bottle body
bottle_body = cq.Workplane("XY")

# Define points for the bottle body shape
points = [
    (-body_diameter/2, 0),
    (-body_diameter/4, 10),
    (-body_diameter/6, 40),
    (-body_diameter/8, 100),
    (0, 160),
    (body_diameter/8, 100),
    (body_diameter/6, 40),
    (body_diameter/4, 10),
    (body_diameter/2, 0)
]

# Create the body with a spline
bottle_body = bottle_body.lineTo(points[0][0], points[0][1])
for i in range(1, len(points)):
    bottle_body = bottle_body.lineTo(points[i][0], points[i][1])

# Close the profile and extrude
bottle_body = bottle_body.close().extrude(body_height)

# Create the neck
neck_profile = cq.Workplane("XY", origin=(0, 0, body_height)).circle(neck_diameter/2).extrude(neck_height)

# Create the cork area
cork_profile = cq.Workplane("XY", origin=(0, 0, body_height + neck_height)).circle(cork_diameter/2).extrude(cork_height)

# Combine everything
result = bottle_body.union(neck_profile).union(cork_profile)

# Add the threading to the cork
# Create a series of concentric circles to represent the threading
for i in range(thread_count):
    angle = (i * 2 * pi) / thread_count
    x = (cork_diameter/2 - thread_depth/2) * cos(angle)
    y = (cork_diameter/2 - thread_depth/2) * sin(angle)
    threading_circle = cq.Workplane("XY", origin=(x, y, body_height + neck_height + cork_height)).circle(thread_pitch/4).extrude(thread_depth)
    result = result.union(threading_circle)