import cadquery as cq

# Base dimensions
base_length = 50.0
base_width = 30.0
base_thickness = 5.0

# Main body dimensions
body_length = 40.0
body_width = 20.0
body_thickness = 8.0

# Cylindrical section dimensions
cylinder_diameter = 10.0
cylinder_length = 15.0

# Create the base plate
result = cq.Workplane("XY").box(base_length, base_width, base_thickness)

# Add the curved section with parallel cutouts
# Create a workplane on the top face of the base
result = result.faces(">Z").workplane()

# Add the two circular cutouts near the center
result = result.center(-10, 0).circle(4.0).cutThruAll()
result = result.center(10, 0).circle(4.0).cutThruAll()

# Add a small lip or flange on one edge
result = result.faces("<Y").workplane(offset=2.0).rect(5, 5, forConstruction=True).vertices().hole(2.0)

# Create the curved main body section
# Move to the top of the base and create a curved profile
result = result.faces(">Z").workplane().center(0, -base_width/2 + body_width/2)

# Create a curved profile using a spline
points = [
    (0, 0),
    (10, 5),
    (20, 10),
    (30, 15),
    (40, 20),
    (40, 10),
    (30, 5),
    (20, 0),
    (10, -5),
    (0, -10)
]

# Create the curved section
result = result.polyline(points).close().extrude(body_length)

# Add parallel semi-circular cutouts along the main body
cutout_radius = 3.0
cutout_spacing = 5.0
num_cutouts = int(body_length / cutout_spacing) - 1

for i in range(num_cutouts):
    offset = (i + 1) * cutout_spacing
    result = result.faces(">Z").workplane(offset=offset).circle(cutout_radius).cutThruAll()

# Create the tapering section
# Add a taper to the body
result = result.faces(">Z").workplane(offset=body_length).center(0, 0).rect(10, 10).extrude(10)

# Create the cylindrical section
result = result.faces(">Z").workplane(offset=10).center(0, 0).circle(cylinder_diameter/2).extrude(cylinder_length)

# Round the edges for better appearance and safety
result = result.edges("|Z").fillet(1.0)

# Create a final workplane to add any additional features
result = result.faces(">Z").workplane().center(0, 0).circle(2.0).cutThruAll()

# Create a hole for fastening if needed
result = result.faces("<Z").workplane().center(0, 0).circle(3.0).cutThruAll()

# Ensure the result is properly defined
result = result