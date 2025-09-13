import cadquery as cq

# Define dimensions
plate_length = 50.0
plate_width = 20.0
plate_thickness = 3.0

# Hole parameters
hole_diameter = 4.0
hole_spacing = 15.0
hole_offset_from_edge = 5.0

# Pin parameters
pin_diameter = 6.0
pin_length = 12.0
pin_offset_from_plate = 2.0

# End cap parameters
end_cap_diameter = 8.0
end_cap_length = 2.0

# Create the rectangular plate
result = cq.Workplane("XY").box(plate_length, plate_width, plate_thickness)

# Add holes for fastening
hole_positions = [
    (hole_offset_from_edge, 0),
    (plate_length/2, 0),
    (plate_length - hole_offset_from_edge, 0)
]

for pos in hole_positions:
    result = (
        result.faces(">Z")
        .workplane()
        .center(pos[0], pos[1])
        .hole(hole_diameter)
    )

# Add cylindrical pins
pin_positions = [
    (hole_offset_from_edge, 0),
    (plate_length/2, 0),
    (plate_length - hole_offset_from_edge, 0)
]

for pos in pin_positions:
    # Create the pin cylinder
    result = (
        result.faces(">Z")
        .workplane()
        .center(pos[0], pos[1])
        .circle(pin_diameter/2)
        .extrude(pin_length)
    )
    
    # Add the end cap
    result = (
        result.faces(">Z")
        .workplane()
        .center(pos[0], pos[1])
        .circle(end_cap_diameter/2)
        .extrude(end_cap_length)
    )

# Rotate to show the diagonal perspective as described
result = result.rotate((0, 0, 0), (1, 0, 0), 30)
result = result.rotate((0, 0, 0), (0, 1, 0), 15)