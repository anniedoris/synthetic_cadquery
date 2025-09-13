import cadquery as cq
from math import pi, cos, sin

# Dimensions
length = 100.0
width = 20.0
height = 15.0
curve_radius = 5.0
end_cap_radius = 8.0
screw_hole_dia = 2.0
circle_cutouts = [
    (20.0, 8.0, 4.0),
    (40.0, 12.0, 3.0),
    (60.0, 6.0, 5.0),
    (80.0, 10.0, 3.5)
]
rect_cutouts = [
    (30.0, 5.0, 10.0, 4.0),
    (50.0, 8.0, 12.0, 3.0),
    (70.0, 6.0, 8.0, 5.0)
]
slot_positions = [
    (15.0, 2.0, 6.0, 1.5),
    (25.0, 12.0, 8.0, 1.0),
    (35.0, 4.0, 10.0, 2.0)
]

# Create the base rectangular shape with curved edges
result = cq.Workplane("XY").box(length, width, height)

# Apply fillets to edges for smooth ergonomic feel
result = result.edges("|Z").fillet(2.0)
result = result.edges("|X").fillet(1.5)

# Create the curved profile by adding a slight arch to the top surface
# We'll create a curved surface along the length
# First create a workplane on the top face
result = result.faces(">Z").workplane()
# Add a series of points to create a curved profile
pts = []
num_points = 20
for i in range(num_points + 1):
    x = i * length / num_points
    # Create a smooth curve
    y = width/2 - curve_radius * cos(pi * i / num_points)
    pts.append((x, y))
    
# Create a spline to define the curved top edge
# This is a simplified approach - in practice you might want to use more complex
# surface modeling for a smooth curved surface
result = result.moveTo(0, width/2).lineTo(length, width/2)

# Create end cap with screw hole
# Create a circular cap at one end
end_cap = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .circle(end_cap_radius)
    .extrude(height)
    .faces(">Z")
    .workplane()
    .circle(screw_hole_dia/2)
    .cutThruAll()
)

# Position the end cap
result = result.union(end_cap.translate((0, 0, 0)))

# Create circular cutouts
for x, y, dia in circle_cutouts:
    result = (
        result.faces(">Z")
        .workplane(offset=0.1)
        .moveTo(x, y)
        .circle(dia/2)
        .cutBlind(-height + 0.2)
    )

# Create rectangular cutouts
for x, y, w, h in rect_cutouts:
    result = (
        result.faces(">Z")
        .workplane(offset=0.1)
        .moveTo(x, y)
        .rect(w, h, centered=True)
        .cutBlind(-height + 0.2)
    )

# Create slots
for x, y, w, h in slot_positions:
    result = (
        result.faces(">Z")
        .workplane(offset=0.1)
        .moveTo(x, y)
        .rect(w, h, centered=True)
        .cutBlind(-height + 0.2)
    )

# Create internal structure with walls and bosses
# Add some internal walls to create partitions
internal_walls = (
    cq.Workplane("XY")
    .box(length - 4, width - 4, height - 2)
    .translate((2, 2, 1))
)

# Add mounting bosses
boss_positions = [(10, 5), (30, 15), (50, 5), (70, 15)]
for x, y in boss_positions:
    result = (
        result.faces(">Z")
        .workplane(offset=0.1)
        .moveTo(x, y)
        .circle(2.0)
        .extrude(1.0)
    )

# Add internal partitions
result = result.union(internal_walls)

# Ensure we have a proper solid result
result = result.clean()

# This is a simplified version - a full implementation would require more complex
# geometry to accurately model the curved surface and internal structure
# The approach above creates a basic version with the specified features