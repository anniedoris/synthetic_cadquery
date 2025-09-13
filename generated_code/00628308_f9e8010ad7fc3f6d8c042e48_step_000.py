import cadquery as cq

# Define dimensions
curve_radius = 20.0      # Radius of the curved section
curve_width = 8.0        # Width of the U-shape
flat_length = 15.0       # Length of the flat ends
flat_width = 8.0         # Width of the flat ends
hole_diameter = 4.0      # Diameter of the holes
thickness = 2.0          # Thickness of the material
edge_radius = 1.0        # Radius for rounded edges

# Create the U-shaped bracket
# Start with a workplane
result = cq.Workplane("XY")

# Create the curved section (partial ring)
# We'll create a rectangle and then subtract a smaller rectangle to make the U-shape
# Create outer rectangle
outer_rect = cq.Workplane("XY").rect(2 * curve_radius + curve_width, curve_width).extrude(thickness)

# Create inner rectangle to cut out the curve
inner_rect = cq.Workplane("XY").rect(2 * curve_radius, curve_width).extrude(thickness)

# Cut the inner rectangle from the outer to create the curved section
curve_section = outer_rect.cut(inner_rect)

# Create the flat ends
# Create two flat rectangles extending from each end of the curve
# Left flat end
left_flat = cq.Workplane("XY").rect(flat_length, flat_width).extrude(thickness)
left_flat = left_flat.translate((-curve_radius - curve_width/2 - flat_length/2, 0, 0))

# Right flat end
right_flat = cq.Workplane("XY").rect(flat_length, flat_width).extrude(thickness)
right_flat = right_flat.translate((curve_radius + curve_width/2 + flat_length/2, 0, 0))

# Combine the curve and flat ends
result = curve_section.union(left_flat).union(right_flat)

# Add holes to the flat ends
# Left hole
hole_left = cq.Workplane("XY").circle(hole_diameter/2).extrude(thickness)
hole_left = hole_left.translate((-curve_radius - curve_width/2 - flat_length/2 + flat_length/2, 0, 0))

# Right hole
hole_right = cq.Workplane("XY").circle(hole_diameter/2).extrude(thickness)
hole_right = hole_right.translate((curve_radius + curve_width/2 + flat_length/2 - flat_length/2, 0, 0))

# Cut the holes
result = result.cut(hole_left).cut(hole_right)

# Apply fillets to the edges of the flat ends for rounded corners
result = result.edges("|Z").fillet(edge_radius)

# Since we're creating a U-shape with curved section, let's rebuild it more accurately:
# Create the U-shape more precisely using a profile approach

# Reset and create a better U-shaped profile
result = cq.Workplane("XY")

# Create the main U-shaped profile
# Create the outer curve
result = result.center(0, 0).rect(2 * curve_radius + curve_width, curve_width, forConstruction=True)
# Add the curved section by creating the profile in the right shape

# Better approach - create profile and extrude
# Create a 2D profile that forms a U-shape
result = (
    cq.Workplane("XY")
    .center(0, 0)
    .rect(2 * curve_radius + curve_width, curve_width)
    .center(-curve_radius - curve_width/2, 0)
    .rect(flat_length, flat_width)
    .center(curve_radius + curve_width/2, 0)
    .rect(flat_length, flat_width)
    .extrude(thickness)
)

# Let me reconsider with a cleaner approach using the correct U-shape construction
result = cq.Workplane("XY")

# Create a profile that forms the U-shape
# Start with a rectangle and remove the center to create the U
profile = cq.Workplane("XY").rect(2 * curve_radius + curve_width, curve_width).extrude(thickness)

# Create the flat ends
left_end = cq.Workplane("XY").rect(flat_length, flat_width).extrude(thickness)
left_end = left_end.translate((-curve_radius - curve_width/2 - flat_length/2, 0, 0))

right_end = cq.Workplane("XY").rect(flat_length, flat_width).extrude(thickness)
right_end = right_end.translate((curve_radius + curve_width/2 + flat_length/2, 0, 0))

# Combine the main body with flat ends
result = profile.union(left_end).union(right_end)

# Add holes
hole = cq.Workplane("XY").circle(hole_diameter/2).extrude(thickness)
hole_left = hole.translate((-curve_radius - curve_width/2 - flat_length/2 + flat_length/2, 0, 0))
hole_right = hole.translate((curve_radius + curve_width/2 + flat_length/2 - flat_length/2, 0, 0))

result = result.cut(hole_left).cut(hole_right)

# Apply fillets to edges
result = result.edges("|Z").fillet(edge_radius)

# Even better approach - create a proper 2D profile first
result = cq.Workplane("XY")

# Create a 2D profile of the U-shape
# Create the main U shape profile
# We'll use the approach of creating a profile and then extruding it
# We need to be more careful about how we construct this

# Start with a simple approach: create the 2D profile and extrude
result = (
    cq.Workplane("XY")
    .center(0, 0)
    # Create the curved section (the U part)
    .moveTo(-curve_radius - curve_width/2, 0)
    .lineTo(-curve_radius - curve_width/2, curve_width)
    .threePointArc((0, curve_width + curve_radius), (curve_radius + curve_width/2, curve_width))
    .lineTo(curve_radius + curve_width/2, 0)
    .lineTo(curve_radius + curve_width/2, -curve_width)
    .threePointArc((0, -curve_radius - curve_width), (-curve_radius - curve_width/2, -curve_width))
    .lineTo(-curve_radius - curve_width/2, 0)
    .close()
    .extrude(thickness)
)

# Add the flat ends
# Left flat end
left_end = cq.Workplane("XY").rect(flat_length, flat_width).extrude(thickness)
left_end = left_end.translate((-curve_radius - curve_width/2 - flat_length/2, 0, 0))
result = result.union(left_end)

# Right flat end
right_end = cq.Workplane("XY").rect(flat_length, flat_width).extrude(thickness)
right_end = right_end.translate((curve_radius + curve_width/2 + flat_length/2, 0, 0))
result = result.union(right_end)

# Add holes to flat ends
hole = cq.Workplane("XY").circle(hole_diameter/2).extrude(thickness)
hole_left = hole.translate((-curve_radius - curve_width/2 - flat_length/2 + flat_length/2, 0, 0))
hole_right = hole.translate((curve_radius + curve_width/2 + flat_length/2 - flat_length/2, 0, 0))
result = result.cut(hole_left).cut(hole_right)

# Apply fillets to edges
result = result.edges("|Z").fillet(edge_radius)