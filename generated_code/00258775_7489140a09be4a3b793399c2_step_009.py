import cadquery as cq
from math import pi, cos, sin

# Parameters
main_diameter = 10.0
main_length = 100.0
pin_diameter = 3.0
pin_length = 15.0
pin_spacing = 20.0
num_pins = 5

# Create the main cylinder
result = cq.Workplane("XY").circle(main_diameter/2).extrude(main_length)

# Add rounded end cap
result = result.faces(">Z").workplane().circle(main_diameter/2).extrude(2)

# Add pins
for i in range(num_pins):
    # Calculate position along the cylinder
    z_pos = i * pin_spacing
    
    # Create two pins on opposite sides
    angle1 = 0
    angle2 = pi
    
    # First pin
    pin1 = (
        cq.Workplane("XY")
        .center(0, 0)
        .workplane(offset=z_pos)
        .center(main_diameter/2 * cos(angle1), main_diameter/2 * sin(angle1))
        .circle(pin_diameter/2)
        .extrude(pin_length)
    )
    
    # Second pin
    pin2 = (
        cq.Workplane("XY")
        .center(0, 0)
        .workplane(offset=z_pos)
        .center(main_diameter/2 * cos(angle2), main_diameter/2 * sin(angle2))
        .circle(pin_diameter/2)
        .extrude(pin_length)
    )
    
    # Add pins to the main cylinder
    result = result.union(pin1)
    result = result.union(pin2)

# Rotate the assembly to achieve diagonal orientation
result = result.rotate((0, 0, 0), (1, 1, 0), 45)

# Ensure the result is properly oriented
result = result.translate((-main_length/2, -main_length/2, 0))