import cadquery as cq

# Define dimensions
length = 80.0
width = 60.0
height = 40.0
cylinder_diameter = 20.0
cylinder_depth = 30.0
flange_width = 8.0
hole_diameter = 4.0
hex_size = 6.0
edge_radius = 3.0

# Create base rectangular box
result = cq.Workplane("XY").box(length, width, height)

# Create the angled top surface (trapezoidal profile)
# We'll create a cutout on the front face to form the trapezoid
result = (
    result.faces(">Z")
    .workplane()
    .rect(length - 10, width - 10, forConstruction=True)
    .vertices()
    .hole(2)  # Small holes to define the trapezoidal shape
)

# Create the main cylindrical cutout on the front face
result = (
    result.faces(">Y")
    .workplane()
    .circle(cylinder_diameter / 2)
    .cutBlind(-cylinder_depth)
)

# Create the flange-like structure around the cylindrical cutout
result = (
    result.faces(">Y")
    .workplane()
    .circle(cylinder_diameter / 2 + flange_width)
    .circle(cylinder_diameter / 2)
    .extrude(flange_width)
)

# Add holes around the cylindrical cutout
holes_positions = [
    (-10, 0),
    (0, 10),
    (10, 0),
    (0, -10),
    (-5, 5),
    (5, -5)
]

result = result.faces(">Y").workplane().pushPoints(holes_positions).circle(hole_diameter / 2).cutBlind(-cylinder_depth)

# Add holes on the top surface
top_holes_positions = [
    (20, 15),
    (20, -15),
    (-20, 15),
    (-20, -15)
]

result = (
    result.faces(">Z")
    .workplane()
    .pushPoints(top_holes_positions)
    .circle(hole_diameter / 2)
    .cutBlind(-10)
)

# Add hexagonal cutouts on the side opposite to the cylindrical cutout
result = (
    result.faces("<Y")
    .workplane()
    .center(-20, 0)
    .polygon(6, hex_size)
    .cutBlind(-15)
)

result = (
    result.faces("<Y")
    .workplane()
    .center(20, 0)
    .polygon(6, hex_size)
    .cutBlind(-15)
)

# Round the edges
result = result.edges("|Z").fillet(edge_radius)

# Ensure the cylindrical cutout is properly aligned
result = result.faces(">Y").workplane().circle(cylinder_diameter / 2).cutBlind(-cylinder_depth)

# Add a small chamfer to the top edges for finishing
result = result.edges(">Z and |Y").chamfer(1.0)

# Final result
result = result