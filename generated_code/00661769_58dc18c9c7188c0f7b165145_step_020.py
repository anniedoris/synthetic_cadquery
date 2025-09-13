import cadquery as cq

# Define dimensions
cylinder_diameter = 10.0
cylinder_length = 20.0
box_length = 40.0
box_width = 30.0
box_height = 15.0
mounting_hole_diameter = 3.0
mounting_hole_spacing = 22.0
protrusion1_length = 8.0
protrusion1_width = 4.0
protrusion1_height = 3.0
protrusion2_length = 12.0
protrusion2_width = 6.0
protrusion2_height = 4.0
side_hole_diameter = 2.0
side_hole_offset = 5.0

# Create the main rectangular box
result = cq.Workplane("XY").box(box_length, box_width, box_height)

# Create the cylindrical section
cylinder = cq.Workplane("XY").circle(cylinder_diameter/2).extrude(cylinder_length)

# Position the cylinder at the front left of the box
cylinder = cylinder.translate((-box_length/2 + cylinder_length/2, 0, 0))

# Combine the cylinder with the box
result = result.union(cylinder)

# Add mounting holes on the bottom face
result = (
    result.faces("<Z")
    .workplane()
    .rect(mounting_hole_spacing, mounting_hole_spacing, forConstruction=True)
    .vertices()
    .hole(mounting_hole_diameter)
)

# Add protrusions on one side face
# First protrusion (small rectangular block)
result = (
    result.faces(">Y")
    .workplane(offset=box_height/2 - protrusion1_height/2)
    .center(-box_length/2 + protrusion1_length/2, -box_width/2 + protrusion1_width/2)
    .box(protrusion1_length, protrusion1_width, protrusion1_height, centered=True)
)

# Second protrusion (larger complex shape)
result = (
    result.faces(">Y")
    .workplane(offset=box_height/2 - protrusion2_height/2)
    .center(-box_length/2 + protrusion2_length/2, box_width/2 - protrusion2_width/2)
    .box(protrusion2_length, protrusion2_width, protrusion2_height, centered=True)
)

# Add small circular hole near the top edge on the side face
result = (
    result.faces(">Y")
    .workplane(offset=box_height/2 - side_hole_offset)
    .center(-box_length/2 + side_hole_diameter/2, 0)
    .hole(side_hole_diameter)
)

# Add the front end cap with hole and concentric ring
result = (
    result.faces("<X")
    .workplane()
    .circle(cylinder_diameter/2)
    .circle(cylinder_diameter/4)
    .extrude(-2)
)

# Add center hole in the front cap
result = (
    result.faces("<X")
    .workplane()
    .center(0, 0)
    .circle(cylinder_diameter/8)
    .cutThruAll()
)

# Add texture to the front face (simplified as concentric circles)
result = (
    result.faces("<X")
    .workplane()
    .circle(cylinder_diameter/3)
    .circle(cylinder_diameter/5)
    .circle(cylinder_diameter/7)
    .extrude(-0.5)
)

# Ensure proper orientation and connection
result = result.rotate((0, 0, 0), (0, 1, 0), 90)

# Move to origin
result = result.translate((0, 0, box_height/2))