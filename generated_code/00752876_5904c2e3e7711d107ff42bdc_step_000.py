import cadquery as cq

# Define dimensions
outer_diameter = 50.0
inner_diameter = 30.0
ring_thickness = 5.0
rect_width = 5.0
rect_height = 15.0
fillet_radius = 1.0
chamfer_distance = 1.0

# Create the circular ring
ring = cq.Workplane("XY").circle(outer_diameter/2).circle(inner_diameter/2).extrude(ring_thickness)

# Add chamfer to the top edge of the ring
ring = ring.faces(">Z").chamfer(chamfer_distance)

# Create the rectangular extension
rect = cq.Workplane("XY").rect(rect_width, rect_height).extrude(ring_thickness)

# Position the rectangle perpendicular to the ring
# The rectangle is placed so that one edge aligns with the outer edge of the ring
rect = rect.translate((outer_diameter/2 + rect_width/2, 0, 0))

# Combine the ring and rectangle
result = ring.union(rect)

# Add fillets at the junction where rectangle meets the ring
# Select the edges where the rectangle connects to the ring
result = result.edges("|X and >Y").fillet(fillet_radius)
result = result.edges("|X and <Y").fillet(fillet_radius)