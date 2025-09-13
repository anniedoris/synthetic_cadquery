import cadquery as cq

# Left Component
# Base structure
base_length = 40.0
base_width = 20.0
base_height = 10.0
base = cq.Workplane("XY").box(base_length, base_width, base_height)

# Top plate
top_plate_length = base_length + 4.0
top_plate_width = base_width + 4.0
top_plate_height = 2.0
top_plate = cq.Workplane("XY").box(top_plate_length, top_plate_width, top_plate_height)
top_plate = top_plate.translate((0, 0, base_height))

# Cutout in top plate
cutout_length = 8.0
cutout_width = 6.0
cutout = cq.Workplane("XY").rect(cutout_length, cutout_width).extrude(top_plate_height + 0.1)
cutout = cutout.translate(((top_plate_length - cutout_length) / 2, 
                          (top_plate_width - cutout_width) / 2, 
                          base_height - 0.05))

# Rear support
support_width = 6.0
support_height = 8.0
support_depth = 4.0
support = cq.Workplane("XY").box(support_width, support_depth, support_height)
support = support.translate((base_length / 2 - support_width / 2, 
                            -base_width / 2 + support_depth / 2, 
                            base_height))

# Combine left component
left_component = base.union(top_plate).union(support).cut(cutout)

# Right Component
# Main U-shaped body
u_length = 30.0
u_width = 20.0
u_height = 15.0
u_radius = 5.0

# Create the U-shape with rounded top
u_shape = cq.Workplane("XY")
u_shape = u_shape.moveTo(-u_length/2, -u_width/2)
u_shape = u_shape.lineTo(u_length/2, -u_width/2)
u_shape = u_shape.lineTo(u_length/2, u_width/2 - u_radius)
u_shape = u_shape.threePointArc((u_length/2 - u_radius, u_width/2), (0, u_width/2))
u_shape = u_shape.lineTo(-u_length/2 + u_radius, u_width/2)
u_shape = u_shape.threePointArc((-u_length/2, u_width/2 - u_radius), (-u_length/2, -u_width/2))
u_shape = u_shape.close()

# Extrude the U-shape
main_body = u_shape.extrude(u_height)

# Add cylindrical sections
cylinder_radius = 3.0
cylinder_height = 5.0
cylinder1 = cq.Workplane("XY").circle(cylinder_radius).extrude(cylinder_height)
cylinder1 = cylinder1.translate((0, 0, u_height - cylinder_height))

cylinder2 = cq.Workplane("XY").circle(cylinder_radius).extrude(cylinder_height)
cylinder2 = cylinder2.translate((0, 0, u_height - cylinder_height))

# Add end caps
cap_width = 12.0
cap_height = 3.0
cap_depth = 8.0
cap1 = cq.Workplane("XY").rect(cap_width, cap_depth).extrude(cap_height)
cap1 = cap1.translate((u_length/2 - cap_width/2, 0, u_height - cap_height))

cap2 = cq.Workplane("XY").rect(cap_width, cap_depth).extrude(cap_height)
cap2 = cap2.translate((-u_length/2 + cap_width/2, 0, u_height - cap_height))

# Combine right component
right_component = main_body.union(cylinder1).union(cylinder2).union(cap1).union(cap2)

# Position both components
result = left_component.translate((-60, 0, 0)).union(right_component.translate((60, 0, 0)))