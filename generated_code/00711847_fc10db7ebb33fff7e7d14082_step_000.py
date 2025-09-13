import cadquery as cq
from math import pi, cos, sin

# Main body dimensions
main_length = 80.0
main_width = 8.0
main_height = 4.0
main_curve_radius = 15.0

# Hinged part dimensions
hinge_length = 20.0
hinge_width = 12.0
hinge_height = 6.0

# Create the main body - a curved elongated shape
main_body = (
    cq.Workplane("XY")
    .moveTo(-main_length/2, 0)
    .lineTo(main_length/2, 0)
    .threePointArc((main_length/2 + main_curve_radius, main_curve_radius), (main_length/2, main_curve_radius*2))
    .lineTo(-main_length/2, main_curve_radius*2)
    .threePointArc((-main_length/2 - main_curve_radius, main_curve_radius), (-main_length/2, 0))
    .close()
    .extrude(main_height)
)

# Create the hinged part
hinge_part = (
    cq.Workplane("XY")
    .moveTo(-hinge_length/2, -hinge_width/2)
    .lineTo(hinge_length/2, -hinge_width/2)
    .lineTo(hinge_length/2, hinge_width/2)
    .lineTo(-hinge_length/2, hinge_width/2)
    .close()
    .extrude(hinge_height)
    .translate((main_length/2 - hinge_length/2, 0, main_height/2))
)

# Create a cylindrical hinge connection point
hinge_connection = (
    cq.Workplane("XY")
    .moveTo(main_length/2 - 5, 0)
    .circle(3.0)
    .extrude(2.0)
    .translate((0, 0, main_height/2))
)

# Combine the main body with the hinged part and hinge connection
result = main_body.union(hinge_part).union(hinge_connection)

# Add fillets to make the connections smoother
result = result.edges("|Z").fillet(1.0)