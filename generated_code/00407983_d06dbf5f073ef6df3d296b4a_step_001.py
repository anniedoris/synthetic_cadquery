import cadquery as cq
from math import pi, cos, sin

# Base plate dimensions
base_width = 50.0
base_thickness = 5.0
corner_radius = 5.0

# Gear dimensions
gear_diameter = 30.0
gear_thickness = 3.0
gear_teeth = 12
tooth_width = 2.0
tooth_height = 1.5

# Leg dimensions
leg_count = 3
leg_radius = 3.0
leg_length = 20.0

# Create base plate with rounded corners
base = cq.Workplane("XY").box(base_width, base_width, base_thickness)
base = base.edges("|Z").fillet(corner_radius)

# Add mounting holes at each corner
hole_diameter = 4.0
corner_offset = base_width/2 - 5.0
base = (
    base.faces(">Z")
    .workplane()
    .pushPoints([
        (corner_offset, corner_offset),
        (-corner_offset, corner_offset),
        (-corner_offset, -corner_offset),
        (corner_offset, -corner_offset)
    ])
    .hole(hole_diameter)
)

# Create gear
gear = cq.Workplane("XY").circle(gear_diameter/2).extrude(gear_thickness)

# Create gear teeth
tooth_angle = 2 * pi / gear_teeth
for i in range(gear_teeth):
    angle = i * tooth_angle
    # Create a triangular tooth
    tooth_points = [
        (gear_diameter/2 * cos(angle), gear_diameter/2 * sin(angle)),
        (gear_diameter/2 * cos(angle + tooth_angle/2), gear_diameter/2 * sin(angle + tooth_angle/2)),
        (gear_diameter/2 * cos(angle + tooth_angle), gear_diameter/2 * sin(angle + tooth_angle))
    ]
    # Create a tooth profile
    tooth = cq.Workplane("XY").polyline(tooth_points).close().extrude(tooth_height)
    tooth = tooth.rotate((0, 0, 0), (0, 0, 1), i * tooth_angle)
    gear = gear.union(tooth)

# Position gear on base
gear = gear.translate((0, 0, base_thickness))

# Create legs
legs = cq.Workplane("XY")
for i in range(leg_count):
    angle = i * 2 * pi / leg_count
    # Create a leg as a cylinder
    leg = cq.Workplane("XY").circle(leg_radius).extrude(leg_length)
    # Position the leg
    leg = leg.translate((
        (base_width/2 - 10) * cos(angle),
        (base_width/2 - 10) * sin(angle),
        base_thickness
    ))
    legs = legs.union(leg)

# Combine all parts
result = base.union(legs).union(gear)