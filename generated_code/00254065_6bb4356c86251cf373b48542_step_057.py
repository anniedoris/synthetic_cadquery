import cadquery as cq

# Define dimensions
plate_width = 50.0
plate_length = 50.0
thickness = 5.0
center_hole_dia = 10.0
small_hole_dia = 3.0
small_hole_spacing = 15.0
small_hole_offset = 20.0

# Create the base plate
result = cq.Workplane("XY").box(plate_width, plate_length, thickness)

# Create the L-shaped bracket by cutting a corner
# First, create a workplane on the top face
result = result.faces(">Z").workplane().box(plate_width, plate_length, thickness)

# Create the corner cutout to form L-shape
# We'll create a rectangular cutout on one side
result = (
    result.faces(">Z")
    .workplane()
    .rect(plate_width, plate_length, forConstruction=True)
    .vertices()
    .circle(plate_width/2)
    .cutBlind(-thickness)
)

# Actually, let's create a proper L-bracket
result = cq.Workplane("XY").box(plate_width, plate_length, thickness)

# Create the first plate (horizontal)
plate1 = cq.Workplane("XY").box(plate_width, plate_length, thickness)

# Create the second plate (vertical) perpendicular to the first
plate2 = (
    cq.Workplane("XY")
    .box(plate_width, plate_length, thickness)
    .rotate((0, 0, 0), (0, 0, 1), 90)
    .translate((0, plate_length/2, 0))
)

# Combine the plates
result = plate1.union(plate2)

# Create central hole on both plates
result = (
    result.faces(">Z")
    .workplane()
    .circle(center_hole_dia/2)
    .cutThruAll()
)

# Create small holes around the central hole
result = (
    result.faces(">Z")
    .workplane()
    .rect(small_hole_offset*2, small_hole_offset*2, forConstruction=True)
    .vertices()
    .circle(small_hole_dia/2)
    .cutThruAll()
)

# Adjust to properly form the L-bracket
result = cq.Workplane("XY").box(plate_width, plate_length, thickness)
# Create the vertical plate
vertical_plate = cq.Workplane("XY").box(thickness, plate_length, thickness).translate((plate_width/2 - thickness/2, 0, 0))
# Create the horizontal plate  
horizontal_plate = cq.Workplane("XY").box(plate_width, thickness, thickness).translate((0, plate_length/2 - thickness/2, 0))

# Combine the plates
result = vertical_plate.union(horizontal_plate)

# Add the central hole in the corner
result = (
    result.faces(">Z")
    .workplane()
    .center(plate_width/2 - thickness/2, plate_length/2 - thickness/2)
    .circle(center_hole_dia/2)
    .cutThruAll()
)

# Add the surrounding holes
result = (
    result.faces(">Z")
    .workplane()
    .center(plate_width/2 - thickness/2, plate_length/2 - thickness/2)
    .rect(small_hole_offset*2, small_hole_offset*2, forConstruction=True)
    .vertices()
    .circle(small_hole_dia/2)
    .cutThruAll()
)

# Simplified and corrected approach
result = cq.Workplane("XY").box(plate_width, plate_length, thickness)

# Create L-bracket shape by cutting a corner
result = (
    result.faces(">Z")
    .workplane()
    .rect(plate_width, plate_length, forConstruction=True)
    .vertices()
    .circle(plate_width/2)
    .cutBlind(-thickness)
)

# Better approach - create two plates that intersect at right angle
# Create the base plate (horizontal)
base_plate = cq.Workplane("XY").box(plate_width, thickness, thickness)

# Create the vertical plate  
vertical_plate = cq.Workplane("XY").box(thickness, plate_length, thickness)

# Position the vertical plate to meet the base at right angle
vertical_plate = vertical_plate.translate((plate_width - thickness, 0, 0))

# Combine them
result = base_plate.union(vertical_plate)

# Add the central hole in the corner
result = (
    result.faces(">Z")
    .workplane()
    .center(plate_width - thickness/2, thickness/2)
    .circle(center_hole_dia/2)
    .cutThruAll()
)

# Add surrounding small holes
result = (
    result.faces(">Z")
    .workplane()
    .center(plate_width - thickness/2, thickness/2)
    .rect(small_hole_spacing*2, small_hole_spacing*2, forConstruction=True)
    .vertices()
    .circle(small_hole_dia/2)
    .cutThruAll()
)

# Let's rework this properly - create a clean L-bracket
result = cq.Workplane("XY").box(plate_width, plate_length, thickness)

# Create the L-shape by making a cut
result = (
    result.faces(">Z")
    .workplane()
    .rect(plate_width, plate_length)
    .rect(plate_width - thickness, plate_length - thickness)
    .cutBlind(-thickness)
)

# Actually, let's create a proper L-bracket
result = cq.Workplane("XY").box(plate_width, plate_length, thickness)

# Create the horizontal part
horizontal_part = cq.Workplane("XY").box(plate_width, thickness, thickness)

# Create the vertical part
vertical_part = cq.Workplane("XY").box(thickness, plate_length, thickness)

# Position the vertical part to meet the horizontal part at right angle
vertical_part = vertical_part.translate((plate_width - thickness, 0, 0))

# Combine both parts
result = horizontal_part.union(vertical_part)

# Add the central hole in the corner
result = (
    result.faces(">Z")
    .workplane()
    .center(plate_width - thickness/2, thickness/2)
    .circle(center_hole_dia/2)
    .cutThruAll()
)

# Add surrounding small holes
result = (
    result.faces(">Z")
    .workplane()
    .center(plate_width - thickness/2, thickness/2)
    .rect(small_hole_spacing*2, small_hole_spacing*2, forConstruction=True)
    .vertices()
    .circle(small_hole_dia/2)
    .cutThruAll()
)

# Let's create the L-bracket from scratch properly
result = cq.Workplane("XY")

# Create horizontal plate
result = result.rect(plate_width, thickness).extrude(thickness)

# Create vertical plate
vertical_plate = cq.Workplane("XY").rect(thickness, plate_length).extrude(thickness)

# Position the vertical plate to meet horizontal at right angle
vertical_plate = vertical_plate.translate((plate_width - thickness, 0, 0))

# Combine the plates
result = result.union(vertical_plate)

# Add central hole
result = (
    result.faces(">Z")
    .workplane()
    .center(plate_width - thickness/2, thickness/2)
    .circle(center_hole_dia/2)
    .cutThruAll()
)

# Add surrounding holes
result = (
    result.faces(">Z")
    .workplane()
    .center(plate_width - thickness/2, thickness/2)
    .rect(small_hole_spacing*2, small_hole_spacing*2, forConstruction=True)
    .vertices()
    .circle(small_hole_dia/2)
    .cutThruAll()
)