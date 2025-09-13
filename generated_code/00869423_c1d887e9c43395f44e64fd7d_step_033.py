import cadquery as cq

# Define dimensions
flange_width = 40.0
flange_thickness = 5.0
port_diameter = 20.0
port_length = 30.0
shaft_diameter = 12.0
hole_diameter = 4.0
corner_offset = 15.0
fillet_radius = 3.0

# Create the base flange
base_flange = (
    cq.Workplane("XY")
    .rect(flange_width, flange_width)
    .extrude(flange_thickness)
    .faces("<Z")
    .workplane()
    .circle(shaft_diameter/2)
    .extrude(flange_thickness)
    .faces("<Z")
    .workplane()
    .rect(flange_width, flange_width, forConstruction=True)
    .vertices()
    .circle(hole_diameter/2)
    .cutThruAll()
    .edges("|Z")
    .fillet(fillet_radius)
)

# Create the top flange
top_flange = (
    cq.Workplane("XY")
    .rect(flange_width, flange_width)
    .extrude(flange_thickness)
    .faces(">Z")
    .workplane()
    .circle(shaft_diameter/2)
    .extrude(flange_thickness)
    .faces(">Z")
    .workplane()
    .rect(flange_width, flange_width, forConstruction=True)
    .vertices()
    .circle(hole_diameter/2)
    .cutThruAll()
    .edges("|Z")
    .fillet(fillet_radius)
)

# Create the cylindrical port
port = (
    cq.Workplane("YZ")
    .circle(port_diameter/2)
    .extrude(port_length)
    .faces("<X")
    .workplane()
    .circle(port_diameter/2 - 2)
    .extrude(port_length)
)

# Position the port on the left side
port = port.translate((-port_length/2, 0, 0))

# Create the shaft connecting the flanges
shaft = (
    cq.Workplane("XY")
    .circle(shaft_diameter/2)
    .extrude(flange_thickness * 2)
    .faces("<Z")
    .workplane()
    .circle(shaft_diameter/2)
    .extrude(flange_thickness)
    .faces(">Z")
    .workplane()
    .circle(shaft_diameter/2)
    .extrude(flange_thickness)
)

# Position the shaft in the center
shaft = shaft.translate((0, 0, flange_thickness))

# Combine all parts
result = base_flange.union(top_flange).union(port).union(shaft)