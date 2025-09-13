import cadquery as cq
from math import cos, sin, pi

# Define parameters
central_radius = 20.0
arm_count = 8
arm_width_base = 8.0
arm_width_tip = 3.0
arm_length = 30.0
arm_height = 5.0
arm_taper = 0.3
additional_width = 6.0
additional_height = 4.0
triangular_size = 4.0

# Create the central body
result = cq.Workplane("XY").circle(central_radius).extrude(2.0)

# Create arms
for i in range(arm_count):
    angle = 2 * pi * i / arm_count
    
    # Create a trapezoidal arm profile
    arm_points = [
        (0, 0),
        (arm_width_base/2, 0),
        (arm_width_tip/2, arm_length),
        (-arm_width_tip/2, arm_length),
        (-arm_width_base/2, 0)
    ]
    
    # Create the arm
    arm = (
        cq.Workplane("XY")
        .polyline(arm_points)
        .close()
        .extrude(arm_height)
        .rotate((0, 0, 0), (0, 0, 1), angle * 180 / pi)
        .translate((central_radius * cos(angle), central_radius * sin(angle), 0))
    )
    
    # Add taper to the arm
    arm = arm.faces(">Z").workplane().rect(arm_width_base, arm_length).extrude(-arm_taper * arm_length)
    
    result = result.union(arm)

# Add additional rectangular elements
for i in range(arm_count):
    angle = 2 * pi * i / arm_count
    
    # Add rectangular element near the central body
    rect = (
        cq.Workplane("XY")
        .rect(additional_width, additional_height)
        .extrude(1.5)
        .rotate((0, 0, 0), (0, 0, 1), angle * 180 / pi)
        .translate((central_radius * 0.7 * cos(angle), central_radius * 0.7 * sin(angle), 0))
    )
    
    result = result.union(rect)

# Add triangular elements near the central body
for i in range(arm_count):
    angle = 2 * pi * i / arm_count
    
    # Create triangular support
    triangle_points = [
        (0, 0),
        (triangular_size/2, triangular_size),
        (-triangular_size/2, triangular_size),
        (0, 0)
    ]
    
    triangle = (
        cq.Workplane("XY")
        .polyline(triangle_points)
        .close()
        .extrude(1.5)
        .rotate((0, 0, 0), (0, 0, 1), angle * 180 / pi)
        .translate((central_radius * 0.5 * cos(angle), central_radius * 0.5 * sin(angle), 0))
    )
    
    result = result.union(triangle)

# Add a slight fillet to the edges for smoother appearance
result = result.edges("|Z").fillet(1.0)

# Add a small central hole
result = result.faces(">Z").workplane().hole(4.0)

# Add a chamfer to the top edges
result = result.faces(">Z").edges().chamfer(0.5)

# Add a chamfer to the bottom edges
result = result.faces("<Z").edges().chamfer(0.5)

# Ensure all elements are properly aligned and connected
result = result.clean()