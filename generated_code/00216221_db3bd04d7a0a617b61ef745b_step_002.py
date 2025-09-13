import cadquery as cq

# Define dimensions
length = 100.0  # longer side
width = 60.0    # shorter side
thickness = 5.0 # uniform thickness
tilt_angle = 12.0 # tilt angle in degrees

# Create the base rectangle
panel = cq.Workplane("XY").rect(length, width)

# Rotate the rectangle to create the tilt
panel = panel.rotate((0, 0, 0), (0, 0, 1), tilt_angle)

# Extrude to create the 3D panel
panel = panel.extrude(thickness)

# Add the two circular holes
# Hole 1: near bottom left corner
# Position it at (-length/2 + 15, -width/2 + 15) 
panel = (
    panel.faces(">Z")
    .workplane()
    .center(-length/2 + 15, -width/2 + 15)
    .circle(3.0)
    .cutThruAll()
)

# Hole 2: at center of panel
panel = (
    panel.faces(">Z")
    .workplane()
    .center(0, 0)
    .circle(3.0)
    .cutThruAll()
)

result = panel