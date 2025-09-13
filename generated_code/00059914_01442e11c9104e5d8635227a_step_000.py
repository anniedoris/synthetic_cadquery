import cadquery as cq

# Define dimensions for the hexagonal nut
hex_width = 10.0  # Width across flats of the hexagon
hole_diameter = 6.0  # Diameter of the central hole
thickness = 5.0  # Thickness of the nut

# Create the hexagonal nut
result = (
    cq.Workplane("XY")
    .polygon(6, hex_width)  # Create a regular hexagon
    .extrude(thickness)  # Extrude to create the 3D nut
    .faces(">Z")  # Select the top face
    .workplane()  # Create a workplane on the top face
    .circle(hole_diameter / 2)  # Draw the central hole
    .cutThruAll()  # Cut through the entire nut
)

# Optional: Add fillets to the edges for a more realistic appearance
# result = result.edges("|Z").fillet(0.5)