import cadquery as cq

# Dimensions
rail_length = 200.0
rail_width = 20.0
rail_height = 10.0
carriage_length = 60.0
carriage_width = 20.0
carriage_height = 10.0
end_cap_width = 25.0
end_cap_length = 10.0
end_cap_height = 10.0
hole_diameter = 3.0
hole_spacing = 20.0
hole_offset = 5.0

# Create the main rail
rail = cq.Workplane("XY").box(rail_length, rail_width, rail_height)

# Add holes to the top surface of the rail
rail = (
    rail.faces(">Z")
    .workplane()
    .rarray(hole_spacing, 0, int(rail_length/hole_spacing), 1, center=True)
    .circle(hole_diameter/2)
    .cutThruAll()
)

# Create the carriage
carriage = cq.Workplane("XY").box(carriage_length, carriage_width, carriage_height)

# Create the U-shaped opening in the bottom of the carriage
carriage = (
    carriage.faces("<Z")
    .workplane()
    .rect(carriage_length - 2, carriage_width - 2, forConstruction=True)
    .vertices()
    .circle(2.0)
    .extrude(-2.0)
)

# Create end caps
end_cap = cq.Workplane("XY").box(end_cap_length, end_cap_width, end_cap_height)

# Position end caps at each end of the rail
end_cap_left = end_cap.translate((-rail_length/2 + end_cap_length/2, 0, 0))
end_cap_right = end_cap.translate((rail_length/2 - end_cap_length/2, 0, 0))

# Combine all parts
result = rail.union(end_cap_left).union(end_cap_right)

# Add carriage to the rail (positioned at the center for visualization)
carriage = carriage.translate((0, 0, rail_height/2 + carriage_height/2))
result = result.union(carriage)