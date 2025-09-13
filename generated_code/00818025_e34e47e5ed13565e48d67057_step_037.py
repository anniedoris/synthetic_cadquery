import cadquery as cq

# Define dimensions
plate_length = 100.0
plate_width = 60.0
plate_thickness = 5.0
arm_length = 30.0
arm_width = 20.0
arm_thickness = 5.0
hole_diameter = 6.0
rod_diameter = 4.0
rod_length = 40.0
lip_height = 2.0
lip_width = 5.0

# Create the main plate with curved surface
result = cq.Workplane("XY").box(plate_length, plate_width, plate_thickness)

# Add lip to the edge
result = (
    result.faces(">Y")
    .workplane(offset=plate_thickness/2)
    .rect(plate_length, lip_width, forConstruction=True)
    .vertices()
    .hole(2.0)
    .faces(">Y")
    .workplane()
    .rect(plate_length, lip_width)
    .extrude(lip_height)
)

# Add holes to the plate
hole_positions = [
    (20, 15),
    (20, 45),
    (60, 15),
    (60, 45),
    (80, 30)
]

result = result.faces(">Z").workplane()
for pos in hole_positions:
    result = result.center(pos[0] - plate_length/2, pos[1] - plate_width/2).hole(hole_diameter)

# Create the arm/bracket
result = (
    result.faces(">Y")
    .workplane(offset=plate_thickness/2)
    .rect(arm_length, arm_width)
    .extrude(arm_thickness)
)

# Chamfer the arm edge
result = (
    result.faces("<Y")
    .workplane()
    .rect(arm_length, arm_width)
    .extrude(arm_thickness)
    .faces("<Y")
    .edges("|Z")
    .chamfer(2.0)
)

# Add holes to the arm
arm_hole_positions = [
    (10, 5),
    (10, 15),
    (20, 5),
    (20, 15)
]

result = result.faces("<Y").workplane()
for pos in arm_hole_positions:
    result = result.center(pos[0] - arm_length/2, pos[1] - arm_width/2).hole(hole_diameter)

# Create the cylindrical rods
rod1 = cq.Workplane("XY").circle(rod_diameter/2).extrude(rod_length)
rod2 = cq.Workplane("XY").circle(rod_diameter/2).extrude(rod_length)

# Position the rods
rod1 = rod1.translate((plate_length/2 - 10, -plate_width/2 + 10, plate_thickness/2))
rod2 = rod2.translate((-plate_length/2 + 10, -plate_width/2 + 10, plate_thickness/2))

# Combine everything
result = result.union(rod1).union(rod2)

# Add rounded ends to rods
result = result.faces("<Z").workplane().circle(rod_diameter/2).extrude(rod_length/2)
result = result.faces(">Z").workplane().circle(rod_diameter/2).extrude(rod_length/2)

result = result