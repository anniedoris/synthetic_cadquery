import cadquery as cq

# Base dimensions
base_length = 100.0
base_width = 50.0
base_height = 10.0

# Protrusion dimensions
protrusion_diameter = 8.0
protrusion_height = 5.0

# Plate dimensions
plate_length = 40.0
plate_width = 30.0
plate_height = 3.0

# Shaft dimensions
shaft_diameter = 10.0
shaft_length = 20.0
shaft_flat_length = 5.0

# Create base
base = cq.Workplane("XY").box(base_length, base_width, base_height)

# Add protrusions
base = (
    base.faces(">Z")
    .workplane()
    .center(-base_length/2 + 10, 0)
    .circle(protrusion_diameter/2)
    .extrude(protrusion_height)
    .faces(">Z")
    .workplane()
    .center(base_length/2 - 10, 0)
    .circle(protrusion_diameter/2)
    .extrude(protrusion_height)
)

# Add holes to base
base = (
    base.faces(">Z")
    .workplane()
    .pushPoints([(-base_length/2 + 20, -base_width/2 + 10),
                 (-base_length/2 + 20, base_width/2 - 10),
                 (base_length/2 - 20, -base_width/2 + 10),
                 (base_length/2 - 20, base_width/2 - 10)])
    .circle(2.0)
    .cutThruAll()
)

# Create plate
plate = cq.Workplane("XY").box(plate_length, plate_width, plate_height)

# Add holes to plate
plate = (
    plate.faces(">Z")
    .workplane()
    .circle(shaft_diameter/2)
    .cutThruAll()
    .faces(">Z")
    .workplane()
    .pushPoints([(-plate_length/2 + 8, -plate_width/2 + 8),
                 (-plate_length/2 + 8, plate_width/2 - 8),
                 (plate_length/2 - 8, -plate_width/2 + 8),
                 (plate_length/2 - 8, plate_width/2 - 8)])
    .circle(1.5)
    .cutThruAll()
)

# Create shaft
shaft = cq.Workplane("XY").circle(shaft_diameter/2).extrude(shaft_length)

# Add flat end to shaft
shaft = (
    shaft.faces(">Z")
    .workplane()
    .center(0, 0)
    .rect(shaft_flat_length, shaft_diameter, forConstruction=True)
    .vertices()
    .hole(1.0)
)

# Position components
# Place plate on base
plate = plate.translate((0, 0, base_height))

# Position shaft through plate
shaft = shaft.translate((0, 0, base_height + plate_height))

# Combine all components
result = base.union(plate).union(shaft)