import cadquery as cq

# Dimensions
width = 200.0
height = 300.0
thickness = 8.0
screen_width = 180.0
screen_height = 260.0
bezel_width = (width - screen_width) / 2
bezel_height = (height - screen_height) / 2
corner_radius = 10.0
edge_chamfer = 2.0
button_width = 40.0
button_height = 6.0
button_depth = 2.0
home_button_diameter = 20.0
home_button_depth = 3.0
microphone_diameter = 4.0
microphone_depth = 1.5
port_width = 12.0
port_height = 4.0
port_depth = 2.0

# Create the base rectangular prism
result = cq.Workplane("XY").box(width, height, thickness)

# Round the edges and corners
result = result.edges("|Z").fillet(corner_radius)
result = result.edges("|X or |Y").chamfer(edge_chamfer)

# Create the screen recess
result = (
    result.faces(">Z")
    .workplane(offset=-0.1)
    .rect(screen_width, screen_height)
    .cutBlind(-0.1)
)

# Create the home button on the bottom face
result = (
    result.faces("<Z")
    .workplane(offset=-0.1)
    .center(0, -height/2 + home_button_diameter/2 + 5)
    .circle(home_button_diameter/2)
    .cutBlind(-home_button_depth)
)

# Create the microphone cutout on one side face
result = (
    result.faces("<X")
    .workplane(offset=thickness/2 - microphone_depth/2)
    .center(0, 0)
    .circle(microphone_diameter/2)
    .cutBlind(-microphone_depth)
)

# Create the port cutout on the other side face
result = (
    result.faces(">X")
    .workplane(offset=thickness/2 - port_depth/2)
    .center(0, -height/2 + port_height/2 + 10)
    .rect(port_width, port_height)
    .cutBlind(-port_depth)
)

# Create the button cutout on one side face
result = (
    result.faces("<X")
    .workplane(offset=thickness/2 - button_depth/2)
    .center(0, height/2 - button_height/2 - 10)
    .rect(button_width, button_height)
    .cutBlind(-button_depth)
)