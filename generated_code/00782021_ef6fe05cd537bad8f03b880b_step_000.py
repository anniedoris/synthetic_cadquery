import cadquery as cq
from math import sin, cos, pi

# Define parameters for the assembly
cylinder_radius = 10.0
cylinder_height = 20.0
cylinder_offset = 5.0
bracket_width = 8.0
bracket_thickness = 3.0
bracket_length = 15.0
gear_radius = 8.0
gear_teeth = 12
pin_radius = 2.0
pin_length = 15.0

# Create the central cylindrical structure with grooves
result = cq.Workplane("XY").circle(cylinder_radius).extrude(cylinder_height)

# Add grooves to the cylinder
for i in range(4):
    angle = i * pi / 2
    groove_x = cylinder_radius * cos(angle)
    groove_y = cylinder_radius * sin(angle)
    result = (
        result.faces(">Z")
        .workplane(offset=cylinder_height/2)
        .center(groove_x, groove_y)
        .rect(3, 2, forConstruction=True)
        .vertices()
        .hole(1.0)
    )

# Create L-shaped brackets
bracket_count = 4
for i in range(bracket_count):
    angle = i * 2 * pi / bracket_count
    bracket_x = (cylinder_radius + cylinder_offset) * cos(angle)
    bracket_y = (cylinder_radius + cylinder_offset) * sin(angle)
    
    # Create bracket
    bracket = (
        cq.Workplane("XY")
        .center(bracket_x, bracket_y)
        .rect(bracket_width, bracket_thickness)
        .extrude(bracket_length)
        .faces(">Z")
        .workplane()
        .rect(bracket_width, bracket_thickness)
        .extrude(bracket_length)
    )
    
    # Rotate bracket to correct orientation
    bracket = bracket.rotate((0, 0, 0), (0, 0, 1), angle * 180 / pi)
    
    # Position bracket properly
    result = result.union(bracket)

# Create gear-like component
gear_center_x = (cylinder_radius + cylinder_offset) * cos(pi/4)
gear_center_y = (cylinder_radius + cylinder_offset) * sin(pi/4)

# Create gear teeth using a polygon
gear = cq.Workplane("XY").center(gear_center_x, gear_center_y)

# Create gear teeth
for i in range(gear_teeth):
    angle = i * 2 * pi / gear_teeth
    tooth_x = gear_radius * cos(angle)
    tooth_y = gear_radius * sin(angle)
    # Create a simple tooth shape
    tooth = (
        cq.Workplane("XY")
        .center(tooth_x, tooth_y)
        .rect(2, 2)
        .extrude(2)
    )
    gear = gear.union(tooth)

# Add the gear to the assembly
result = result.union(gear)

# Create pins for connections
# Create a pin near the gear
pin1 = (
    cq.Workplane("XY")
    .center(gear_center_x, gear_center_y)
    .circle(pin_radius)
    .extrude(pin_length)
)
result = result.union(pin1)

# Create another pin for the assembly
pin2_x = (cylinder_radius + cylinder_offset) * cos(3*pi/4)
pin2_y = (cylinder_radius + cylinder_offset) * sin(3*pi/4)
pin2 = (
    cq.Workplane("XY")
    .center(pin2_x, pin2_y)
    .circle(pin_radius)
    .extrude(pin_length)
)
result = result.union(pin2)

# Add bearing block or support
bearing_x = (cylinder_radius + cylinder_offset) * cos(0)
bearing_y = (cylinder_radius + cylinder_offset) * sin(0)
bearing = (
    cq.Workplane("XY")
    .center(bearing_x, bearing_y)
    .rect(6, 6)
    .extrude(3)
)
result = result.union(bearing)

# Position the assembly to make it centered
result = result.translate((-cylinder_offset, 0, 0))

# Final result
result = result