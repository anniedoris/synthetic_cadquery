import cadquery as cq

# Define dimensions
plate_length = 50.0
plate_width = 30.0
plate_thickness = 5.0
cylinder_diameter = 20.0
cylinder_inner_diameter = 12.0
cylinder_length = 25.0

# Create the base plate
result = cq.Workplane("XY").box(plate_length, plate_width, plate_thickness)

# Create the cylindrical bore
# Move to the center of the top face and create a cylinder
result = (
    result.faces(">Z")
    .workplane()
    .circle(cylinder_diameter / 2.0)
    .circle(cylinder_inner_diameter / 2.0)
    .extrude(cylinder_length)
)

# Chamfer the edges of the plate for a cleaner look
result = result.edges("|Z").chamfer(1.0)

# Add a fillet to the edges where the cylinder meets the plate
result = result.faces("<Z").edges().fillet(1.0)

# Ensure the final object is properly aligned
result = result.faces(">Z").workplane().circle(cylinder_inner_diameter / 2.0).cutThruAll()