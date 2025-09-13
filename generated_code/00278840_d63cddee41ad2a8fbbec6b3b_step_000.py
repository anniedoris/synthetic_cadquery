import cadquery as cq

# Define dimensions
plate_length = 60.0
plate_width = 40.0
plate_thickness = 10.0
boss_diameter = 25.0
boss_height = 10.0
bore_diameter = 8.0
hole_diameter = 6.0
hole_spacing = 30.0
hole_offset = 15.0

# Create the rectangular plate
result = cq.Workplane("XY").box(plate_length, plate_width, plate_thickness)

# Create the cylindrical boss on one end
result = (
    result.faces(">Z")
    .workplane()
    .circle(boss_diameter / 2.0)
    .extrude(boss_height)
)

# Create the central bore in the boss
result = (
    result.faces(">Z")
    .workplane()
    .circle(bore_diameter / 2.0)
    .cutThruAll()
)

# Create mounting holes on the opposite end
result = (
    result.faces("<Z")
    .workplane()
    .center(-hole_offset, 0)
    .circle(hole_diameter / 2.0)
    .cutThruAll()
    .center(2 * hole_offset, 0)
    .circle(hole_diameter / 2.0)
    .cutThruAll()
)

# Add fillets to the edges for a smoother transition
result = result.edges("|Z").fillet(2.0)

# Ensure the final result is assigned to the variable 'result'
result = result