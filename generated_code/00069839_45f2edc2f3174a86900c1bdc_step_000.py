import cadquery as cq

# Define the dimensions
hexagon_radius = 10.0  # Distance from center to vertex of hexagon
height = 20.0          # Height of the prism
cutout_width = 8.0     # Width of the rectangular cutout
cutout_height = 12.0   # Height of the rectangular cutout

# Create the hexagonal prism
result = cq.Workplane("XY").polygon(6, hexagon_radius).extrude(height)

# Create the rectangular cutout
# Move to the center of the prism and create a rectangle
result = (
    result.faces(">Z")
    .workplane(offset=-height/2)
    .rect(cutout_width, cutout_height)
    .cutThruAll()
)

# Alternative approach using a more precise method:
# Create the hexagonal prism first
# hex_prism = cq.Workplane("XY").polygon(6, hexagon_radius).extrude(height)

# Create a rectangular solid for the cutout
# cutout = cq.Workplane("XY").rect(cutout_width, cutout_height).extrude(height + 0.1)

# Position the cutout at the center
# cutout = cutout.translate((0, 0, -0.05))  # Slightly offset to ensure full penetration

# Subtract the cutout from the hexagonal prism
# result = hex_prism.cut(cutout)