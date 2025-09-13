import cadquery as cq

# Dimensions
length = 100.0
width = 50.0
height = 30.0
lid_thickness = 3.0
handle_width = 8.0
handle_height = 12.0
handle_depth = 5.0
vent_hole_diameter = 6.0
vent_hole_spacing = 20.0

# Create the main body of the box
box = cq.Workplane("XY").box(length, width, height)

# Create the lid
lid = cq.Workplane("XY").box(length, width, lid_thickness)

# Position the lid on top of the box
lid = lid.translate((0, 0, height))

# Create ventilation holes on the front face of the main body
front_face = box.faces(">Z").workplane(offset=-height/2)
front_face = front_face.center(-vent_hole_spacing/2, 0).circle(vent_hole_diameter/2).cutThruAll()
front_face = front_face.center(vent_hole_spacing, 0).circle(vent_hole_diameter/2).cutThruAll()

# Create a handle on the lid
handle = cq.Workplane("XY").rect(handle_width, handle_height).extrude(handle_depth)
handle = handle.translate((length/2 - handle_width/2, 0, lid_thickness - handle_depth))

# Combine the lid and handle
lid = lid.union(handle)

# Create a hinge on one side of the lid
hinge_width = 5.0
hinge_height = 3.0
hinge_depth = 2.0
hinge = cq.Workplane("XY").rect(hinge_width, hinge_height).extrude(hinge_depth)
hinge = hinge.translate((-length/2 + hinge_width/2, 0, lid_thickness - hinge_depth))

# Add the hinge to the lid
lid = lid.union(hinge)

# Position the lid to show it's open
lid = lid.rotate((0, 0, 0), (0, 1, 0), 45)

# Combine everything
result = box.union(lid)

# Ensure the lid is properly positioned and connected
# Create a simple box to represent the main body with the lid
main_body = cq.Workplane("XY").box(length, width, height)

# Create a lid that is hinged on one side
lid_body = cq.Workplane("XY").box(length, width, lid_thickness)

# Position lid above the main body
lid_body = lid_body.translate((0, 0, height))

# Create the hinge and handle features
# Create a simple box with lid and handle
result = (
    cq.Workplane("XY")
    .box(length, width, height)
    .faces(">Z")
    .workplane()
    .rect(length - 10, width - 10, forConstruction=True)
    .vertices()
    .circle(vent_hole_diameter/2)
    .cutThruAll()
    .faces(">Z")
    .workplane()
    .rect(length - 10, width - 10, forConstruction=True)
    .vertices()
    .circle(vent_hole_diameter/2)
    .cutThruAll()
    .faces(">Z")
    .workplane()
    .rect(handle_width, handle_height, forConstruction=True)
    .vertices()
    .rect(handle_width, handle_height)
    .extrude(lid_thickness)
    .translate((0, 0, height))
    .rotate((0, 0, 0), (0, 1, 0), 45)
)