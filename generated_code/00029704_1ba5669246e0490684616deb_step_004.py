import cadquery as cq

# Parameters
plate_width = 60.0
plate_height = 40.0
segment_count = 6
hole_diameter = 4.0
bridge_thickness = 2.0

# Create the first plate
# Start with a base rectangle
plate = cq.Workplane("XY").rect(plate_width, plate_height).extrude(5.0)

# Create the segmented structure by cutting vertical slots
segment_width = plate_width / segment_count
for i in range(1, segment_count):
    cut_x = i * segment_width
    plate = plate.faces(">Z").workplane(offset=0.1).moveTo(cut_x - segment_width/2, 0).rect(segment_width/20, plate_height).cutThruAll()

# Add holes in the first three segments (near top)
hole_positions = [segment_width/2, 3*segment_width/2, 5*segment_width/2]
for pos in hole_positions:
    plate = plate.faces(">Z").workplane(offset=0.1).moveTo(pos - plate_width/2, plate_height/2 - 5).circle(hole_diameter/2).cutThruAll()

# Create the second plate as a mirror image
plate2 = plate.mirror(mirrorPlane="YZ", basePointVector=(0, 0, 0))

# Position the plates with some offset for visualization
plate = plate.translate((-plate_width/2 - 10, 0, 0))
plate2 = plate2.translate((plate_width/2 + 10, 0, 0))

# Combine both plates
result = plate.union(plate2)