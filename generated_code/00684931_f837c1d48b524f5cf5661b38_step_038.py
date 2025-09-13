import cadquery as cq
from math import sin, cos, pi

# Define dimensions
outer_diameter = 50.0
inner_diameter = 30.0
fin_count = 8
fin_height = 5.0
fin_width = 3.0
inner_curve_radius = 2.0
outer_curve_radius = 2.0

# Create the base ring
ring = cq.Workplane("XY").circle(outer_diameter/2).circle(inner_diameter/2).extrude(5.0)

# Create the fins
fin_angle = 360.0 / fin_count

for i in range(fin_count):
    # Position each fin around the ring
    angle = i * fin_angle
    # Create a fin shape
    fin = (
        cq.Workplane("XY")
        .center(outer_diameter/2 - fin_height/2, 0)
        .moveTo(0, -fin_width/2)
        .lineTo(fin_height, 0)
        .lineTo(0, fin_width/2)
        .close()
        .extrude(5.0)
        .rotate((0, 0, 0), (0, 0, 1), angle)
    )
    
    # Add the fin to the ring
    ring = ring.union(fin)

# Create inner curved sections
inner_curve_points = []
for i in range(fin_count):
    angle = i * fin_angle + fin_angle/2
    x = (inner_diameter/2 - inner_curve_radius) * cos(angle * pi/180)
    y = (inner_diameter/2 - inner_curve_radius) * sin(angle * pi/180)
    inner_curve_points.append((x, y))

# Create outer curved sections
outer_curve_points = []
for i in range(fin_count):
    angle = i * fin_angle + fin_angle/2
    x = (outer_diameter/2 + outer_curve_radius) * cos(angle * pi/180)
    y = (outer_diameter/2 + outer_curve_radius) * sin(angle * pi/180)
    outer_curve_points.append((x, y))

# Add inner curved sections
for i, point in enumerate(inner_curve_points):
    x, y = point
    # Create a small curved indentation
    curve = (
        cq.Workplane("XY")
        .center(x, y)
        .circle(inner_curve_radius)
        .extrude(5.0)
    )
    ring = ring.cut(curve)

# Add outer curved sections
for i, point in enumerate(outer_curve_points):
    x, y = point
    # Create a small curved indentation
    curve = (
        cq.Workplane("XY")
        .center(x, y)
        .circle(outer_curve_radius)
        .extrude(5.0)
    )
    ring = ring.cut(curve)

# Apply fillets to smooth edges
ring = ring.edges("|Z").fillet(0.5)

# Ensure we have a solid result
result = ring

# Alternative implementation with more precise fin shapes
# This version creates more organic-looking fins
result = cq.Workplane("XY").circle(outer_diameter/2).circle(inner_diameter/2).extrude(5.0)

# Create more organic fins
for i in range(fin_count):
    angle = i * fin_angle
    
    # Create a curved fin profile
    fin_profile = (
        cq.Workplane("XY")
        .moveTo(outer_diameter/2 - fin_height, -fin_width/4)
        .threePointArc((outer_diameter/2, 0), (outer_diameter/2 - fin_height, fin_width/4))
        .lineTo(outer_diameter/2 - fin_height, -fin_width/4)
        .close()
    )
    
    # Position and rotate the fin
    fin = fin_profile.extrude(5.0).rotate((0, 0, 0), (0, 0, 1), angle)
    result = result.union(fin)

# Create inner and outer curve features
# Inner curves
for i in range(fin_count):
    angle = i * fin_angle + fin_angle/2
    # Inner curve
    curve_x = (inner_diameter/2 - inner_curve_radius/2) * cos(angle * pi/180)
    curve_y = (inner_diameter/2 - inner_curve_radius/2) * sin(angle * pi/180)
    result = (
        result.faces(">Z")
        .workplane()
        .center(curve_x, curve_y)
        .circle(inner_curve_radius)
        .cutBlind(-5.0)
    )

# Outer curves
for i in range(fin_count):
    angle = i * fin_angle + fin_angle/2
    # Outer curve
    curve_x = (outer_diameter/2 + outer_curve_radius/2) * cos(angle * pi/180)
    curve_y = (outer_diameter/2 + outer_curve_radius/2) * sin(angle * pi/180)
    result = (
        result.faces(">Z")
        .workplane()
        .center(curve_x, curve_y)
        .circle(outer_curve_radius)
        .cutBlind(-5.0)
    )

# Apply final fillets
result = result.edges("|Z").fillet(0.3)