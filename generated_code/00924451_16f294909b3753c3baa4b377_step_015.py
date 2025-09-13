import cadquery as cq

# Define dimensions
rod_diameter = 10.0
rod_length = 100.0
nut_height = 8.0
nut_width = 16.0  # Across flats

# Create the cylindrical rod
rod = cq.Workplane("XY").circle(rod_diameter/2).extrude(rod_length)

# Create a hexagonal nut
hex_nut = cq.Workplane("XY").polygon(6, nut_width).extrude(nut_height)

# Position the first nut at the start of the rod
nut1 = hex_nut.translate((0, 0, -nut_height/2))

# Position the second nut at the end of the rod
nut2 = hex_nut.translate((0, 0, rod_length + nut_height/2))

# Combine the rod and nuts
result = rod.union(nut1).union(nut2)