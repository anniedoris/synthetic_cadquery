import cadquery as cq

# Define dimensions
plate_width = 50.0
plate_length = 100.0
thickness = 5.0
slot_width = 10.0
slot_length = 80.0
hole_diameter = 6.0
hole_offset = 15.0
fillet_radius = 2.0

# Create the L-shaped plate
result = (
    cq.Workplane("XY")
    # Create the vertical plate
    .box(plate_width, plate_length, thickness)
    # Create the horizontal plate
    .faces(">Y")
    .workplane()
    .box(plate_length, plate_width, thickness)
    # Remove the overlapping region to create the L-shape
    .faces("<Y")
    .workplane()
    .box(plate_length, plate_width, thickness)
    # Create the central slot
    .faces(">Z")
    .workplane()
    .rect(slot_length, slot_width, forConstruction=True)
    .vertices()
    .hole(hole_diameter)
    # Add holes to the vertical plate
    .faces("<Y")
    .workplane()
    .rect(plate_width, plate_length, forConstruction=True)
    .vertices()
    .hole(hole_diameter)
    # Add holes to the horizontal plate
    .faces(">X")
    .workplane()
    .rect(plate_length, plate_width, forConstruction=True)
    .vertices()
    .hole(hole_diameter)
    # Round the edges
    .edges("|Z")
    .fillet(fillet_radius)
)

# Correct approach: Create proper L-shape with proper boolean operations
result = (
    cq.Workplane("XY")
    # Create the base plate
    .box(plate_width, plate_length, thickness)
    # Create the vertical extension
    .faces(">Y")
    .workplane()
    .box(plate_length, plate_width, thickness)
    # Create the central slot
    .faces(">Z")
    .workplane()
    .rect(slot_length, slot_width)
    .cutThruAll()
    # Add holes to the base plate
    .faces("<Y")
    .workplane()
    .rect(plate_width, plate_length, forConstruction=True)
    .vertices()
    .hole(hole_diameter)
    # Add holes to the vertical plate
    .faces(">X")
    .workplane()
    .rect(plate_length, plate_width, forConstruction=True)
    .vertices()
    .hole(hole_diameter)
    # Round edges
    .edges("|Z")
    .fillet(fillet_radius)
)

# Even better approach: start with one plate, then add the other
result = (
    cq.Workplane("XY")
    # Create base plate
    .box(plate_width, plate_length, thickness)
    # Add the L-shaped extension
    .faces(">Y")
    .workplane()
    .box(plate_length, plate_width, thickness)
    # Create central slot in the intersection
    .faces(">Z")
    .workplane()
    .rect(slot_length, slot_width)
    .cutThruAll()
    # Add holes to the base plate
    .faces("<Y")
    .workplane()
    .rect(plate_width, plate_length, forConstruction=True)
    .vertices()
    .hole(hole_diameter)
    # Add holes to the extension plate
    .faces(">X")
    .workplane()
    .rect(plate_length, plate_width, forConstruction=True)
    .vertices()
    .hole(hole_diameter)
    # Fillet edges
    .edges("|Z")
    .fillet(fillet_radius)
)