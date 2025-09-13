import cadquery as cq

# Define dimensions
hub_width = 40.0
hub_height = 20.0
hub_length = 10.0
hub_radius = 5.0

cylinder_diameter = 20.0
cylinder_radius = cylinder_diameter / 2.0
cylinder_length = 30.0

fin_width = 2.0
fin_height = 5.0
fin_thickness = 1.0
fin_count = 8

# Create the central hub
hub = cq.Workplane("XY").box(hub_width, hub_height, hub_length)
hub = hub.faces(">Z").workplane().circle(hub_radius).cutThruAll()
hub = hub.edges("|Z").fillet(2.0)

# Create one cylindrical component with fins
cylinder = cq.Workplane("XY").circle(cylinder_radius).extrude(cylinder_length/2)
cylinder = cylinder.faces(">Z").workplane().circle(cylinder_radius).cutThruAll()

# Create fins around the cylinder
fin_angle = 360.0 / fin_count
for i in range(fin_count):
    angle = i * fin_angle
    fin = (
        cq.Workplane("XY")
        .moveTo(cylinder_radius, 0)
        .lineTo(cylinder_radius + fin_width, 0)
        .lineTo(cylinder_radius + fin_width, fin_height)
        .lineTo(cylinder_radius, fin_height)
        .close()
        .extrude(fin_thickness)
        .rotateAboutCenter((0, 0, 1), angle)
    )
    cylinder = cylinder.union(fin)

# Position the cylinders on both sides of the hub
cylinder1 = cylinder.translate((-(hub_width/2 + cylinder_length/2), 0, 0))
cylinder2 = cylinder.translate((+(hub_width/2 + cylinder_length/2), 0, 0))

# Combine everything
result = hub.union(cylinder1).union(cylinder2)