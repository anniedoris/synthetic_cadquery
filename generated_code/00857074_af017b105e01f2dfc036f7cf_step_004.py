import cadquery as cq

# Main plate dimensions
plate_width = 80.0
plate_height = 120.0
plate_thickness = 3.0

# Mounting hole parameters
mounting_hole_diameter = 3.0
mounting_hole_spacing = 15.0
mounting_hole_offset = 5.0

# Recessed slot parameters
slot_width = 10.0
slot_height = 5.0
slot_offset_from_top = 10.0

# Protrusions parameters
protrusion_width = 12.0
protrusion_height = 8.0
protrusion_offset_from_bottom = 15.0

# Additional cutouts
cutout_width = 6.0
cutout_height = 4.0
cutout_offset_from_bottom = 25.0

# Smaller part dimensions
small_part_width = 40.0
small_part_height = 60.0
small_part_thickness = 3.0

# Protruding tab parameters
tab_width = 8.0
tab_height = 10.0
tab_offset_from_top = 10.0

# Cylindrical feature parameters
cylinder_diameter = 4.0
cylinder_offset_from_bottom = 10.0

# Create the main plate
result = cq.Workplane("XY").box(plate_width, plate_height, plate_thickness)

# Add mounting holes
for i in range(4):
    if i < 2:
        # Top mounting holes
        result = (
            result.faces(">Z")
            .workplane()
            .center(-plate_width/2 + mounting_hole_offset + i * mounting_hole_spacing, 
                   plate_height/2 - mounting_hole_offset)
            .hole(mounting_hole_diameter)
        )
    else:
        # Bottom mounting holes
        result = (
            result.faces(">Z")
            .workplane()
            .center(-plate_width/2 + mounting_hole_offset + (i-2) * mounting_hole_spacing, 
                   -plate_height/2 + mounting_hole_offset)
            .hole(mounting_hole_diameter)
        )

# Add recessed slot
result = (
    result.faces(">Z")
    .workplane()
    .center(0, plate_height/2 - slot_offset_from_top - slot_height/2)
    .rect(slot_width, slot_height)
    .cutThruAll()
)

# Add protrusions near bottom edge
result = (
    result.faces(">Z")
    .workplane()
    .center(-protrusion_width/2 - 5, -plate_height/2 + protrusion_offset_from_bottom + protrusion_height/2)
    .rect(protrusion_width, protrusion_height)
    .cutThruAll()
)
result = (
    result.faces(">Z")
    .workplane()
    .center(protrusion_width/2 + 5, -plate_height/2 + protrusion_offset_from_bottom + protrusion_height/2)
    .rect(protrusion_width, protrusion_height)
    .cutThruAll()
)

# Add additional cutouts near bottom edge
result = (
    result.faces(">Z")
    .workplane()
    .center(-cutout_width/2 - 5, -plate_height/2 + cutout_offset_from_bottom + cutout_height/2)
    .rect(cutout_width, cutout_height)
    .cutThruAll()
)
result = (
    result.faces(">Z")
    .workplane()
    .center(cutout_width/2 + 5, -plate_height/2 + cutout_offset_from_bottom + cutout_height/2)
    .rect(cutout_width, cutout_height)
    .cutThruAll()
)

# Create the smaller part
small_part = cq.Workplane("XY").box(small_part_width, small_part_height, small_part_thickness)

# Add protruding tab on smaller part
small_part = (
    small_part.faces(">Z")
    .workplane()
    .center(0, small_part_height/2 - tab_offset_from_top - tab_height/2)
    .rect(tab_width, tab_height)
    .cutThruAll()
)

# Add holes and cutouts to smaller part
small_part = (
    small_part.faces(">Z")
    .workplane()
    .center(-10, 10)
    .circle(1.5)
    .cutThruAll()
)
small_part = (
    small_part.faces(">Z")
    .workplane()
    .center(10, 10)
    .circle(1.5)
    .cutThruAll()
)

# Add rectangular cutout near top edge
small_part = (
    small_part.faces(">Z")
    .workplane()
    .center(0, small_part_height/2 - 15)
    .rect(10, 5)
    .cutThruAll()
)

# Add cylindrical feature (bolt/pin)
small_part = (
    small_part.faces(">Z")
    .workplane()
    .center(0, -small_part_height/2 + cylinder_offset_from_bottom)
    .circle(cylinder_diameter/2)
    .extrude(small_part_thickness)
)

# Position the smaller part relative to the main plate
# Translate the small part to position it above the main plate
small_part = small_part.translate((0, 0, plate_thickness))

# Combine the main plate and small part
result = result.union(small_part)

# Add a small clearance between the parts to ensure they don't intersect
# We'll add a small offset to the small part's position to simulate clearance
small_part = small_part.translate((0, 0, 0.1))
result = result.union(small_part)