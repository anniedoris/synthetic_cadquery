import cadquery as cq

# Define dimensions for the 19-inch rack mountable enclosure
rack_width = 19.0 * 25.4  # 19 inches in mm
rack_depth = 300.0        # Depth in mm (adjustable)
rack_height = 44.45       # 1U height in mm

# Create the main enclosure box
result = cq.Workplane("XY").box(rack_width, rack_depth, rack_height)

# Create front panel ventilation slots
# Vertical slots along the top edge
slot_width = 5.0
slot_height = 10.0
slot_spacing = 15.0
num_slots = int((rack_width - 20) / slot_spacing)  # Leave 10mm margin on each side

for i in range(num_slots):
    x_pos = -rack_width/2 + 10 + i * slot_spacing
    result = (
        result.faces(">Z")
        .workplane(offset=-0.1)
        .center(x_pos, rack_depth/2 - 10)
        .rect(slot_width, slot_height)
        .cutThruAll()
    )

# Create front panel circular feature (fan vent)
result = (
    result.faces(">Z")
    .workplane(offset=-0.1)
    .center(-rack_width/2 + 30, rack_depth/2 - 50)
    .circle(15.0)
    .cutThruAll()
)

# Create holes for front panel components
# Grid of holes on front panel
hole_spacing = 30.0
num_holes_x = 3
num_holes_y = 2

for i in range(num_holes_x):
    for j in range(num_holes_y):
        x_pos = -rack_width/2 + 50 + i * hole_spacing
        y_pos = rack_depth/2 - 80 - j * hole_spacing
        result = (
            result.faces(">Z")
            .workplane(offset=-0.1)
            .center(x_pos, y_pos)
            .circle(2.5)
            .cutThruAll()
        )

# Create top panel holes (grid pattern)
top_hole_spacing = 40.0
num_top_holes_x = 4
num_top_holes_y = 3

for i in range(num_top_holes_x):
    for j in range(num_top_holes_y):
        x_pos = -rack_width/2 + 30 + i * top_hole_spacing
        y_pos = -rack_depth/2 + 30 + j * top_hole_spacing
        result = (
            result.faces(">Y")
            .workplane(offset=0.1)
            .center(x_pos, y_pos)
            .circle(2.0)
            .cutThruAll()
        )

# Create rear panel mounting holes
rear_hole_spacing = 50.0
num_rear_holes_x = 2
num_rear_holes_y = 4

for i in range(num_rear_holes_x):
    for j in range(num_rear_holes_y):
        x_pos = -rack_width/2 + 30 + i * (rack_width - 60)  # Two columns
        y_pos = -rack_depth/2 + 30 + j * rear_hole_spacing
        result = (
            result.faces("<Y")
            .workplane(offset=-0.1)
            .center(x_pos, y_pos)
            .circle(3.0)
            .cutThruAll()
        )

# Create rear panel rack mounting holes (for 19-inch rack)
# Add a protrusion on the right side for mounting
result = (
    result.faces("<Y")
    .workplane(offset=-0.1)
    .center(rack_width/2 - 20, 0)
    .rect(15, 20)
    .extrude(5.0)
)

# Create side holes for ventilation
side_hole_spacing = 60.0
num_side_holes = 2

for i in range(num_side_holes):
    y_pos = -rack_depth/2 + 50 + i * side_hole_spacing
    # Left side holes
    result = (
        result.faces("<X")
        .workplane(offset=0.1)
        .center(-rack_width/2 + 10, y_pos)
        .circle(2.0)
        .cutThruAll()
    )
    # Right side holes
    result = (
        result.faces(">X")
        .workplane(offset=0.1)
        .center(rack_width/2 - 10, y_pos)
        .circle(2.0)
        .cutThruAll()
    )

# Add fillets to corners for a more aesthetically pleasing appearance
result = result.edges("|Z").fillet(2.0)

# Add a small handle feature on the rear panel
result = (
    result.faces("<Y")
    .workplane(offset=-0.1)
    .center(rack_width/2 - 20, rack_depth/2 - 30)
    .rect(10, 5)
    .extrude(3.0)
)

# Create additional mounting holes on the rear panel
# Create a series of holes along the rear panel edges for rack mounting
for i in range(3):
    result = (
        result.faces("<Y")
        .workplane(offset=-0.1)
        .center(-rack_width/2 + 30 + i * 60, -rack_depth/2 + 20)
        .circle(1.5)
        .cutThruAll()
    )