import cadquery as cq

# Main body dimensions
main_length = 100.0
main_width = 60.0
main_height = 40.0

# Cylindrical component dimensions
cylinder_diameter = 30.0
cylinder_height = 20.0

# Box component dimensions
box_length = 40.0
box_width = 30.0
box_height = 15.0

# Create main body
main_body = cq.Workplane("XY").box(main_length, main_width, main_height)

# Add flanges (front and back)
flange_thickness = 5.0
main_body = main_body.faces(">Z").workplane(offset=flange_thickness).rect(main_length, main_width, forConstruction=True).vertices().hole(6.0)
main_body = main_body.faces("<Z").workplane(offset=-flange_thickness).rect(main_length, main_width, forConstruction=True).vertices().hole(6.0)

# Add side cutouts
side_cutout_width = 20.0
side_cutout_height = 15.0
main_body = main_body.faces(">Y").workplane(offset=main_height/2 - side_cutout_height/2).rect(side_cutout_width, side_cutout_height).cutThruAll()
main_body = main_body.faces("<Y").workplane(offset=main_height/2 - side_cutout_height/2).rect(side_cutout_width, side_cutout_height).cutThruAll()

# Add bolt holes on top
main_body = main_body.faces(">Z").workplane().rect(main_length - 10, main_width - 10, forConstruction=True).vertices().hole(4.0)

# Add cylindrical component
cylinder = cq.Workplane("XY").circle(cylinder_diameter/2).extrude(cylinder_height)
cylinder = cylinder.translate((0, main_width/2 - flange_thickness/2, main_height/2))

# Add box component
box = cq.Workplane("XY").box(box_length, box_width, box_height)
box = box.translate((0, 0, main_height + box_height/2))

# Combine all components
result = main_body.union(cylinder).union(box)

# Add wires/connections
wire_diameter = 3.0
wire_length = 20.0
wire = cq.Workplane("XY").circle(wire_diameter/2).extrude(wire_length)
wire = wire.translate((main_length/2 + wire_length/2, 0, main_height/2))
result = result.union(wire)