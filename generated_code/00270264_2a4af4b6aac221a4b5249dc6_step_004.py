import cadquery as cq

# Dimensions
length = 600.0
width = 400.0
height = 20.0
leg_height = 20.0
leg_diameter = 15.0
burner_size = 80.0
burner_border = 10.0
control_diameter = 12.0

# Create the main cooktop body
cooktop = cq.Workplane("XY").box(length, width, height)

# Add raised perimeter edge
cooktop = cooktop.faces(">Z").workplane().rect(length - 10, width - 10).extrude(2)

# Add chamfered sides (slightly sloped inward)
# We'll create a chamfer on the vertical edges
cooktop = cooktop.edges("|Z").chamfer(2)

# Add front and back lip
front_back_lip_height = 3.0
cooktop = (
    cooktop.faces(">Y")
    .workplane(offset=-front_back_lip_height)
    .rect(length - 20, front_back_lip_height * 2)
    .extrude(front_back_lip_height)
    .faces("<Y")
    .workplane(offset=-front_back_lip_height)
    .rect(length - 20, front_back_lip_height * 2)
    .extrude(front_back_lip_height)
)

# Create the cooking zones (2x2 grid)
burner_spacing_x = (length - 2 * burner_size) / 3
burner_spacing_y = (width - 2 * burner_size) / 3

# Create burner zones
for i in range(2):
    for j in range(2):
        x_pos = -length/2 + burner_spacing_x + i * (burner_size + burner_spacing_x)
        y_pos = -width/2 + burner_spacing_y + j * (burner_size + burner_spacing_y)
        # Create the burner indentation
        cooktop = (
            cooktop.faces(">Z")
            .workplane()
            .center(x_pos, y_pos)
            .rect(burner_size, burner_size)
            .extrude(-10)
        )
        # Add the raised border around each burner
        cooktop = (
            cooktop.faces(">Z")
            .workplane()
            .center(x_pos, y_pos)
            .rect(burner_size + burner_border, burner_size + burner_border)
            .extrude(2)
        )

# Add the legs at each corner
leg_positions = [
    (-length/2 + 20, -width/2 + 20),
    (length/2 - 20, -width/2 + 20),
    (-length/2 + 20, width/2 - 20),
    (length/2 - 20, width/2 - 20)
]

for x, y in leg_positions:
    cooktop = (
        cooktop.faces("<Z")
        .workplane()
        .center(x, y)
        .circle(leg_diameter/2)
        .extrude(leg_height)
    )

# Add control knobs
control_positions = [
    (-length/4, -width/2 + 30),
    (length/4, -width/2 + 30)
]

for x, y in control_positions:
    cooktop = (
        cooktop.faces("<Y")
        .workplane()
        .center(x, y)
        .circle(control_diameter/2)
        .extrude(-5)
    )

result = cooktop