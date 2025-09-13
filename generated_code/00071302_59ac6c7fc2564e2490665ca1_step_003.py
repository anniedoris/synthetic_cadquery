import cadquery as cq

# Define dimensions
total_width = 50.0
total_height = 80.0
thickness = 5.0
top_width = 40.0
bottom_width = 40.0
central_width_top = 30.0
central_width_bottom = 30.0
central_width_middle = 20.0
lip_width = 8.0
lip_height = 3.0
indent_radius = 5.0
indent_depth = 3.0

# Create the base shape
result = cq.Workplane("XY")

# Create the central vertical section with hourglass shape
# Start with the bottom part
result = (
    result
    .moveTo(-central_width_bottom/2, -total_height/2)
    .lineTo(central_width_bottom/2, -total_height/2)
    .lineTo(central_width_middle/2, -total_height/2 + thickness)
    .lineTo(central_width_middle/2, total_height/2 - thickness)
    .lineTo(-central_width_middle/2, total_height/2 - thickness)
    .lineTo(-central_width_middle/2, total_height/2)
    .lineTo(-central_width_bottom/2, total_height/2)
    .close()
)

# Extrude to create the 3D shape
result = result.extrude(thickness)

# Create the top section
top_plate = (
    cq.Workplane("XY")
    .moveTo(-top_width/2, total_height/2 - thickness)
    .lineTo(top_width/2, total_height/2 - thickness)
    .lineTo(top_width/2, total_height/2)
    .lineTo(-top_width/2, total_height/2)
    .close()
    .extrude(thickness)
)

# Create the bottom section
bottom_plate = (
    cq.Workplane("XY")
    .moveTo(-bottom_width/2, -total_height/2)
    .lineTo(bottom_width/2, -total_height/2)
    .lineTo(bottom_width/2, -total_height/2 + thickness)
    .lineTo(-bottom_width/2, -total_height/2 + thickness)
    .close()
    .extrude(thickness)
)

# Add the top and bottom sections to the main shape
result = result.union(top_plate)
result = result.union(bottom_plate)

# Add the lip to the top section
top_lip = (
    cq.Workplane("XY")
    .moveTo(top_width/2 - lip_width, total_height/2 - thickness)
    .lineTo(top_width/2, total_height/2 - thickness)
    .lineTo(top_width/2, total_height/2)
    .lineTo(top_width/2 - lip_width, total_height/2)
    .close()
    .extrude(thickness)
)

# Add the lip to the bottom section
bottom_lip = (
    cq.Workplane("XY")
    .moveTo(-bottom_width/2, -total_height/2)
    .lineTo(-bottom_width/2 + lip_width, -total_height/2)
    .lineTo(-bottom_width/2 + lip_width, -total_height/2 + thickness)
    .lineTo(-bottom_width/2, -total_height/2 + thickness)
    .close()
    .extrude(thickness)
)

# Add the lips to the main shape
result = result.union(top_lip)
result = result.union(bottom_lip)

# Create and add the curved indentation on the front face of the central section
# This will be a cylindrical cutout
indent_center_y = 0
indent_center_x = 0

# Create the indentation in the central section
indent = (
    cq.Workplane("XY")
    .moveTo(indent_center_x - indent_radius, indent_center_y)
    .circle(indent_radius)
    .extrude(indent_depth)
)

# Cut the indentation from the central section
result = result.cut(indent)

# Apply fillets to smooth the transitions
result = result.edges("|Z").fillet(2.0)
result = result.edges("|X").fillet(2.0)

# Create the final result
result = result