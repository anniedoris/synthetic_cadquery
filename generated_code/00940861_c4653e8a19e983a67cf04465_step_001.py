import cadquery as cq

# Dimensions
length = 100.0
width = 60.0
height = 40.0
thickness = 3.0
cutout_diameter = 8.0
hole_diameter = 2.5
support_width = 10.0
support_height = 5.0

# Create the base box with open bottom
result = cq.Workplane("XY").box(length, width, height)

# Remove the bottom face to create an open structure
result = result.faces("<Z").shell(-thickness)

# Add top plate
top_plate = cq.Workplane("XY").box(length, width, thickness)

# Add cutouts to top plate
# Front cutout
top_plate = (
    top_plate.faces(">Z")
    .workplane()
    .center(-length/4, 0)
    .circle(cutout_diameter/2)
    .cutThruAll()
)

# Back cutout
top_plate = (
    top_plate.faces(">Z")
    .workplane()
    .center(length/4, 0)
    .circle(cutout_diameter/2)
    .cutThruAll()
)

# Add side panel cutouts
# Left side
result = (
    result.faces("<X")
    .workplane()
    .center(0, 0)
    .circle(cutout_diameter/2)
    .cutThruAll()
)

# Right side
result = (
    result.faces(">X")
    .workplane()
    .center(0, 0)
    .circle(cutout_diameter/2)
    .cutThruAll()
)

# Add mounting holes to top plate
top_plate = (
    top_plate.faces(">Z")
    .workplane()
    .rect(length - 10, width - 10, forConstruction=True)
    .vertices()
    .cboreHole(hole_diameter, hole_diameter * 1.5, hole_diameter * 0.5)
)

# Add base supports
# Front support
result = (
    result.faces("<Z")
    .workplane()
    .center(-length/2 + support_width/2, 0)
    .rect(support_width, support_height)
    .extrude(-thickness)
)

# Back support
result = (
    result.faces("<Z")
    .workplane()
    .center(length/2 - support_width/2, 0)
    .rect(support_width, support_height)
    .extrude(-thickness)
)

# Combine top plate with main structure
result = result.union(top_plate)

# Add holes to side panels
# Left side holes
result = (
    result.faces("<X")
    .workplane()
    .rect(width - 10, height - 10, forConstruction=True)
    .vertices()
    .cboreHole(hole_diameter, hole_diameter * 1.5, hole_diameter * 0.5)
)

# Right side holes
result = (
    result.faces(">X")
    .workplane()
    .rect(width - 10, height - 10, forConstruction=True)
    .vertices()
    .cboreHole(hole_diameter, hole_diameter * 1.5, hole_diameter * 0.5)
)

# Add holes to front and back panels
# Front panel holes
result = (
    result.faces("<Y")
    .workplane()
    .rect(length - 10, height - 10, forConstruction=True)
    .vertices()
    .cboreHole(hole_diameter, hole_diameter * 1.5, hole_diameter * 0.5)
)

# Back panel holes
result = (
    result.faces(">Y")
    .workplane()
    .rect(length - 10, height - 10, forConstruction=True)
    .vertices()
    .cboreHole(hole_diameter, hole_diameter * 1.5, hole_diameter * 0.5)
)