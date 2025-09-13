import cadquery as cq

# Define dimensions
base_length = 50.0
base_width = 20.0
base_height = 5.0

# Cylindrical protrusion dimensions
cylinder_base_diameter = 12.0
cylinder_top_diameter = 8.0
cylinder_height = 10.0

# Circular cutout diameter
cutout_diameter = 11.0

# Rectangular cutout dimensions
rect_cutout_width = 8.0
rect_cutout_height = 6.0
rect_cutout_depth = 3.0

# Create the base
result = cq.Workplane("XY").box(base_length, base_width, base_height)

# Add rounded edges to the base
result = result.edges("|Z").fillet(2.0)

# Create the cylindrical protrusion on the right end
# Move to the right end of the base
result = (
    result.faces(">X")
    .workplane()
    .circle(cylinder_base_diameter/2)
    .extrude(cylinder_height)
)

# Create the tapered part of the cylinder (top part)
result = (
    result.faces(">Z")
    .workplane()
    .circle(cylinder_top_diameter/2)
    .extrude(cylinder_height/2)
)

# Create the circular cutout on the left end
result = (
    result.faces("<X")
    .workplane()
    .circle(cutout_diameter/2)
    .cutThruAll()
)

# Create the rectangular cutout on the side near the circular cutout
# Position it on the side face near the left end
result = (
    result.faces("<Y")
    .workplane(offset=-base_height/2)
    .rect(rect_cutout_width, rect_cutout_height, forConstruction=True)
    .vertices()
    .hole(rect_cutout_depth)
)

# Alternative approach for the rectangular cutout (cutting through the side)
result = (
    result.faces("<Y")
    .workplane()
    .rect(rect_cutout_width, rect_cutout_height)
    .cutBlind(-rect_cutout_depth)
)

# Let's refine this to create a proper rectangular cutout
result = (
    cq.Workplane("XY")
    .box(base_length, base_width, base_height)
    .edges("|Z").fillet(2.0)
    .faces(">X")
    .workplane()
    .circle(cylinder_base_diameter/2)
    .extrude(cylinder_height)
    .faces(">Z")
    .workplane()
    .circle(cylinder_top_diameter/2)
    .extrude(cylinder_height/2)
    .faces("<X")
    .workplane()
    .circle(cutout_diameter/2)
    .cutThruAll()
    .faces("<Y")
    .workplane()
    .rect(rect_cutout_width, rect_cutout_height)
    .cutBlind(-rect_cutout_depth)
)

# More precise approach for the rectangular cutout
result = (
    cq.Workplane("XY")
    .box(base_length, base_width, base_height)
    .edges("|Z").fillet(2.0)
    .faces(">X")
    .workplane()
    .circle(cylinder_base_diameter/2)
    .extrude(cylinder_height)
    .faces(">Z")
    .workplane()
    .circle(cylinder_top_diameter/2)
    .extrude(cylinder_height/2)
    .faces("<X")
    .workplane()
    .circle(cutout_diameter/2)
    .cutThruAll()
    .faces("<Y")
    .workplane()
    .rect(rect_cutout_width, rect_cutout_height)
    .cutBlind(-rect_cutout_depth)
)

# Final clean version
result = (
    cq.Workplane("XY")
    .box(base_length, base_width, base_height)
    .edges("|Z").fillet(2.0)
    .faces(">X")
    .workplane()
    .circle(cylinder_base_diameter/2)
    .extrude(cylinder_height)
    .faces(">Z")
    .workplane()
    .circle(cylinder_top_diameter/2)
    .extrude(cylinder_height/2)
    .faces("<X")
    .workplane()
    .circle(cutout_diameter/2)
    .cutThruAll()
    .faces("<Y")
    .workplane()
    .rect(rect_cutout_width, rect_cutout_height)
    .cutBlind(-rect_cutout_depth)
)