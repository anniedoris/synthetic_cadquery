import cadquery as cq

# Brick dimensions
length = 32.0  # 4 bumps * 8mm pitch
width = 8.0    # 1 bump * 8mm pitch  
height = 9.6   # Standard LEGO height

# Protrusion parameters
bump_diameter = 4.8
bump_height = 1.8
spacing = 8.0  # Pitch between centers

# Create the base brick
result = cq.Workplane("XY").box(length, width, height)

# Add the bumps on top
# Create a grid of 4x4 bumps
for i in range(4):
    for j in range(4):
        x = (i - 1.5) * spacing
        y = (j - 1.5) * spacing
        result = result.faces(">Z").workplane(offset=height).moveTo(x, y).circle(bump_diameter/2).extrude(bump_height)

# The bottom surface should have corresponding recesses for interlocking
# This is a simplified version - in a real LEGO brick, there would be tubes
# but for this basic representation, we'll just have the flat bottom