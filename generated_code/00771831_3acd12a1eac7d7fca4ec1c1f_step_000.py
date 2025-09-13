import cadquery as cq

# Define dimensions
length = 100.0
width = 60.0
thickness = 10.0
hole_diameter = 8.0
counter_sink_diameter = 12.0
counter_sink_depth = 3.0
chamfer_radius = 2.0

# Create the base plate
result = cq.Workplane("XY").box(length, width, thickness)

# Add chamfers to the edges
result = result.edges("|Z").fillet(chamfer_radius)

# Add the four corner holes with countersinks
# First, get the corner positions
corner_positions = [
    (-length/2 + chamfer_radius, -width/2 + chamfer_radius),  # Bottom-left
    (length/2 - chamfer_radius, -width/2 + chamfer_radius),   # Bottom-right
    (-length/2 + chamfer_radius, width/2 - chamfer_radius),   # Top-left
    (length/2 - chamfer_radius, width/2 - chamfer_radius)     # Top-right
]

# Add the holes with countersinks
for x, y in corner_positions:
    result = (
        result.faces(">Z")
        .workplane(centerOption="CenterOfMass")
        .center(x, y)
        .circle(counter_sink_diameter/2)
        .cutBlind(-counter_sink_depth)
        .circle(hole_diameter/2)
        .cutBlind(-thickness)
    )

# Ensure the top surface is flat and the object has consistent thickness
result = result.faces(">Z").workplane().rect(length - 2*chamfer_radius, width - 2*chamfer_radius, forConstruction=True).vertices().hole(hole_diameter)

# Final object with proper hole placement
result = (
    cq.Workplane("XY")
    .box(length, width, thickness)
    .edges("|Z")
    .fillet(chamfer_radius)
    .faces(">Z")
    .workplane()
    .pushPoints(corner_positions)
    .circle(counter_sink_diameter/2)
    .cutBlind(-counter_sink_depth)
    .circle(hole_diameter/2)
    .cutBlind(-thickness)
)