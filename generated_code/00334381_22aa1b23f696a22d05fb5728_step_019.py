import cadquery as cq

# Define dimensions
cylinder_diameter = 10.0
cylinder_length = 50.0
semicircle_radius = cylinder_diameter / 2.0

# Create the cylindrical body
result = cq.Workplane("XY").circle(cylinder_diameter / 2.0).extrude(cylinder_length)

# Create the semicircular end cap
# Move to the end of the cylinder and create a semicircle
result = (
    result.faces(">Z")
    .workplane()
    .circle(semicircle_radius)
    .extrude(semicircle_radius)
    .faces(">Z")
    .workplane()
    .circle(semicircle_radius)
    .extrude(-semicircle_radius)
)

# Create a more realistic semicircular end by cutting a half cylinder
result = (
    result.faces(">Z")
    .workplane()
    .circle(semicircle_radius)
    .extrude(semicircle_radius)
    .faces(">Z")
    .workplane()
    .circle(semicircle_radius)
    .extrude(-semicircle_radius)
    .faces(">Z")
    .workplane()
    .circle(semicircle_radius)
    .extrude(-semicircle_radius)
)

# Better approach - create a proper semicircular cap
# Create a half-cylinder for the rounded end
cap = cq.Workplane("XY").circle(semicircle_radius).extrude(semicircle_radius).rotate((0,0,0), (0,1,0), 90)

# Position the cap at the end of the cylinder and union it
result = result.union(cap.translate((0, 0, cylinder_length)))

# Alternative approach - create the semicircular end by using a proper half-circle
# Create a half cylinder for the rounded end
result = (
    cq.Workplane("XY")
    .circle(cylinder_diameter / 2.0)
    .extrude(cylinder_length)
    .faces(">Z")
    .workplane()
    .circle(cylinder_diameter / 2.0)
    .extrude(cylinder_diameter / 2.0)
    .faces(">Z")
    .workplane()
    .circle(cylinder_diameter / 2.0)
    .extrude(-cylinder_diameter / 2.0)
)

# Even simpler and more correct approach:
# Create the main cylinder
result = cq.Workplane("XY").circle(cylinder_diameter / 2.0).extrude(cylinder_length)

# Create the semicircular cap at the end
cap = cq.Workplane("XY").circle(cylinder_diameter / 2.0).extrude(cylinder_diameter / 2.0)
result = result.union(cap.translate((0, 0, cylinder_length)))