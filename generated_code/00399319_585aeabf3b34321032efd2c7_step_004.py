import cadquery as cq
from math import pi, cos, sin

# Parameters for the component
hex_width = 10.0          # Width of the hexagonal section
hex_height = 2.0          # Height of the hexagonal section
flange_diameter = 15.0    # Diameter of the flanges
flange_thickness = 3.0    # Thickness of the flanges
cylinder_diameter = 8.0   # Diameter of the cylindrical sections
cylinder_length = 5.0     # Length of the cylindrical sections
groove_radius = 0.5       # Radius of the grooves
groove_depth = 0.3        # Depth of the grooves
groove_count = 4          # Number of grooves per flange/cylinder

# Create the central hexagonal prism
hexagon = cq.Workplane("XY").polygon(6, hex_width).extrude(hex_height)

# Create the first flange (on the left)
flange1 = (
    cq.Workplane("XY")
    .circle(flange_diameter/2)
    .extrude(flange_thickness)
    .translate((-hex_width/2 - flange_thickness/2, 0, 0))
)

# Create the second flange (on the right)
flange2 = (
    cq.Workplane("XY")
    .circle(flange_diameter/2)
    .extrude(flange_thickness)
    .translate((hex_width/2 + flange_thickness/2, 0, 0))
)

# Add grooves to the first flange
for i in range(groove_count):
    groove_radius_offset = groove_radius * (i + 1)
    groove_circle = (
        cq.Workplane("XY", origin=(0, 0, -flange_thickness/2))
        .circle(groove_radius_offset)
        .extrude(-groove_depth)
        .translate((-hex_width/2 - flange_thickness/2, 0, 0))
    )
    flange1 = flange1.union(groove_circle)

# Add grooves to the second flange
for i in range(groove_count):
    groove_radius_offset = groove_radius * (i + 1)
    groove_circle = (
        cq.Workplane("XY", origin=(0, 0, -flange_thickness/2))
        .circle(groove_radius_offset)
        .extrude(-groove_depth)
        .translate((hex_width/2 + flange_thickness/2, 0, 0))
    )
    flange2 = flange2.union(groove_circle)

# Create the first cylinder
cylinder1 = (
    cq.Workplane("XY")
    .circle(cylinder_diameter/2)
    .extrude(cylinder_length)
    .translate((-hex_width/2 - flange_thickness - cylinder_length/2, 0, 0))
)

# Create the second cylinder
cylinder2 = (
    cq.Workplane("XY")
    .circle(cylinder_diameter/2)
    .extrude(cylinder_length)
    .translate((hex_width/2 + flange_thickness + cylinder_length/2, 0, 0))
)

# Add grooves to the first cylinder
for i in range(groove_count):
    groove_radius_offset = groove_radius * (i + 1)
    groove_circle = (
        cq.Workplane("XY", origin=(0, 0, -cylinder_length/2))
        .circle(groove_radius_offset)
        .extrude(-groove_depth)
        .translate((-hex_width/2 - flange_thickness - cylinder_length/2, 0, 0))
    )
    cylinder1 = cylinder1.union(groove_circle)

# Add grooves to the second cylinder
for i in range(groove_count):
    groove_radius_offset = groove_radius * (i + 1)
    groove_circle = (
        cq.Workplane("XY", origin=(0, 0, -cylinder_length/2))
        .circle(groove_radius_offset)
        .extrude(-groove_depth)
        .translate((hex_width/2 + flange_thickness + cylinder_length/2, 0, 0))
    )
    cylinder2 = cylinder2.union(groove_circle)

# Combine all parts
result = hexagon.union(flange1).union(flange2).union(cylinder1).union(cylinder2)