import cadquery as cq

# Define dimensions
horizontal_length = 50.0
horizontal_width = 20.0
horizontal_thickness = 5.0
vertical_length = 30.0
vertical_width = 20.0
vertical_thickness = 5.0
cylinder_diameter = 8.0
cylinder_height = 10.0
cutout_length = 15.0
cutout_width = 8.0
hole_diameter = 3.0
standoff_diameter = 4.0
standoff_height = 3.0

# Create the base L-shaped object
result = cq.Workplane("XY").box(horizontal_length, horizontal_width, horizontal_thickness)

# Add the vertical section
result = result.faces(">Z").workplane().box(vertical_length, vertical_width, vertical_thickness)

# Create the cylindrical protrusion at the end of horizontal section
result = (
    result.faces(">X")
    .workplane(offset=horizontal_thickness)
    .circle(cylinder_diameter/2)
    .extrude(cylinder_height)
)

# Create the hollow cylinder (cut out the center)
result = (
    result.faces(">Z")
    .workplane(offset=cylinder_height)
    .circle(cylinder_diameter/2 - 1)
    .extrude(1)
)

# Create the rectangular cutout near the cylindrical end
result = (
    result.faces(">X")
    .workplane(offset=horizontal_thickness)
    .rect(cutout_length, cutout_width, forConstruction=True)
    .vertices()
    .hole(1.0)
)

# Create circular holes on the vertical section
result = (
    result.faces(">Z")
    .workplane(offset=vertical_thickness)
    .rect(vertical_length - 10, vertical_width - 10, forConstruction=True)
    .vertices()
    .hole(hole_diameter)
)

# Create the small cylindrical protrusion (standoff)
result = (
    result.faces(">Z")
    .workplane(offset=vertical_thickness)
    .moveTo(-vertical_length/2 + 5, 0)
    .circle(standoff_diameter/2)
    .extrude(standoff_height)
)

# Ensure proper alignment and clean up any potential issues
result = result.faces(">Z").workplane().tag("top_surface")

# Final result
result = result