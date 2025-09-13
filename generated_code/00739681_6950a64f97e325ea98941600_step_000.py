import cadquery as cq

# Parameters for the plate assembly
plate_width = 100.0
plate_height = 20.0
plate_thickness = 5.0
num_plates = 5
slot_width = 8.0
slot_height = 12.0
slot_spacing = 15.0
offset_distance = 2.0

# Create a single plate with slots
plate = cq.Workplane("XY").box(plate_width, plate_height, plate_thickness)

# Add slots to the plate
# Create a workplane for the top face
top_face = plate.faces(">Z").workplane()

# Add slots along the length of the plate
for i in range(4):  # 4 slots per plate
    x_pos = -plate_width/2 + (i * slot_spacing) + slot_spacing/2
    top_face = top_face.center(x_pos, 0).rect(slot_width, slot_height, forConstruction=True).vertices().hole(2.0)

# Create the stacked plates
result = plate

# Create additional plates with offset
for i in range(1, num_plates):
    # Create a new plate with offset
    new_plate = plate.translate((0, i * offset_distance, 0))
    # Rotate each plate slightly to create the angled perspective
    new_plate = new_plate.rotate((0, 0, 0), (0, 0, 1), i * 5)  # 5 degree rotation per plate
    result = result.union(new_plate)

# Ensure the final result is properly constructed
result = result.val().translate((0, 0, 0))