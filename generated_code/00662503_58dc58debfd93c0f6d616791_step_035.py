import cadquery as cq

# Dimensions for the taller hexagonal prism (bolt/nut)
height_taller = 20.0
hex_width_taller = 10.0
hole_diameter_taller = 6.0

# Dimensions for the shorter hexagonal prism (bolt/nut)
height_shorter = 12.0
hex_width_shorter = 8.0
hole_diameter_shorter = 5.0

# Create the taller hexagonal prism with central hole
taller_prism = (
    cq.Workplane("XY")
    .polygon(6, hex_width_taller)
    .extrude(height_taller)
    .faces(">Z")
    .workplane()
    .hole(hole_diameter_taller)
    .faces("<Z")
    .workplane()
    .hole(hole_diameter_taller)
)

# Create the shorter hexagonal prism with central hole and angle
shorter_prism = (
    cq.Workplane("XY")
    .polygon(6, hex_width_shorter)
    .extrude(height_shorter)
    .faces(">Z")
    .workplane()
    .hole(hole_diameter_shorter)
    .faces("<Z")
    .workplane()
    .hole(hole_diameter_shorter)
    .rotate((0, 0, 0), (0, 1, 0), 30)  # Rotate to show angled perspective
)

# Combine both objects
result = taller_prism.union(shorter_prism.translate((20, 0, 0)))