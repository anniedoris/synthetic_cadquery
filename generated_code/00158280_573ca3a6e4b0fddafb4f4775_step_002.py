import cadquery as cq

# Dimensions
arc_radius = 50.0
arc_width = 20.0
thickness = 5.0
tab_height = 8.0
tab_width = 10.0
cutout_height = 12.0
cutout_width = 6.0
cutout_spacing = 15.0
foot_height = 4.0
foot_width = 8.0
foot_depth = 6.0

# Create the arc-shaped base
# Start with a rectangle and then create the curved shape
base = cq.Workplane("XY").rect(arc_width, arc_radius * 2).extrude(thickness)

# Create the arc profile by cutting out a quarter circle
arc_profile = cq.Workplane("XY").circle(arc_radius).extrude(thickness)

# Create the main curved shape by subtracting the arc from the base
# First create a workplane on the top face to add features
result = base

# Add the top surface (flat)
result = result.faces(">Z").workplane().rect(arc_width, arc_radius * 2).extrude(0.1)

# Add rectangular tabs at ends and midpoint
# Left tab
result = (
    result.faces(">Z")
    .workplane()
    .moveTo(-arc_width/2 - tab_width/2, 0)
    .rect(tab_width, tab_height)
    .extrude(thickness)
)

# Right tab
result = (
    result.faces(">Z")
    .workplane()
    .moveTo(arc_width/2 + tab_width/2, 0)
    .rect(tab_width, tab_height)
    .extrude(thickness)
)

# Midpoint tab
result = (
    result.faces(">Z")
    .workplane()
    .moveTo(0, 0)
    .rect(tab_width, tab_height)
    .extrude(thickness)
)

# Add cutouts along the sides
# Create a workplane on the front face to add cutouts
result = result.faces(">X").workplane(offset=thickness/2)

# Add cutouts evenly spaced
for i in range(3):
    y_pos = -arc_radius + i * cutout_spacing
    result = (
        result.moveTo(0, y_pos)
        .rect(cutout_width, cutout_height)
        .cutBlind(-thickness)
    )

# Add feet at the bottom
result = result.faces("<Z").workplane()

# Add feet at bottom
result = (
    result.moveTo(-arc_width/2 + foot_width/2, -arc_radius + foot_height/2)
    .rect(foot_width, foot_height)
    .extrude(-foot_depth)
)

result = (
    result.moveTo(arc_width/2 - foot_width/2, -arc_radius + foot_height/2)
    .rect(foot_width, foot_height)
    .extrude(-foot_depth)
)

# Create a proper arc-shaped object with the correct geometry
# Start over with a cleaner approach

# Create the main arc shape
result = cq.Workplane("XY").box(arc_width, arc_radius * 2, thickness)

# Create a workplane on the top face to add tabs
result = result.faces(">Z").workplane()

# Add tabs at ends and center
# Left tab
result = (
    result.moveTo(-arc_width/2 - tab_width/2, 0)
    .rect(tab_width, tab_height)
    .extrude(thickness)
)

# Right tab
result = (
    result.moveTo(arc_width/2 + tab_width/2, 0)
    .rect(tab_width, tab_height)
    .extrude(thickness)
)

# Center tab
result = (
    result.moveTo(0, 0)
    .rect(tab_width, tab_height)
    .extrude(thickness)
)

# Create a more precise arc shape by using a curved profile
# Start with a rectangle and then create a proper arc
result = cq.Workplane("XY").box(arc_width, arc_radius * 2, thickness)

# Add the curved shape features
# Add rectangular cutouts along the curved surface
cutout_positions = [-arc_radius + 10, -arc_radius + 25, -arc_radius + 40]

# Add cutouts
for pos in cutout_positions:
    result = (
        result.faces(">X")
        .workplane(offset=thickness/2)
        .moveTo(0, pos)
        .rect(cutout_width, cutout_height)
        .cutBlind(-thickness)
    )

# Add feet at bottom
result = result.faces("<Z").workplane()

# Add feet at the bottom
result = (
    result.moveTo(-arc_width/2 + foot_width/2, -arc_radius + foot_height/2)
    .rect(foot_width, foot_height)
    .extrude(-foot_depth)
)

result = (
    result.moveTo(arc_width/2 - foot_width/2, -arc_radius + foot_height/2)
    .rect(foot_width, foot_height)
    .extrude(-foot_depth)
)

# Create a more accurate curved shape using the proper approach
result = cq.Workplane("XY").box(arc_width, arc_radius * 2, thickness)

# Add the features on the top surface
result = result.faces(">Z").workplane()

# Add tabs at ends and center
# Left tab
result = (
    result.moveTo(-arc_width/2 - tab_width/2, 0)
    .rect(tab_width, tab_height)
    .extrude(thickness)
)

# Right tab
result = (
    result.moveTo(arc_width/2 + tab_width/2, 0)
    .rect(tab_width, tab_height)
    .extrude(thickness)
)

# Center tab
result = (
    result.moveTo(0, 0)
    .rect(tab_width, tab_height)
    .extrude(thickness)
)

# Add cutouts
cutout_positions = [-arc_radius + 10, -arc_radius + 25, -arc_radius + 40]

for pos in cutout_positions:
    result = (
        result.faces(">X")
        .workplane(offset=thickness/2)
        .moveTo(0, pos)
        .rect(cutout_width, cutout_height)
        .cutBlind(-thickness)
    )

# Add feet at bottom
result = result.faces("<Z").workplane()

# Add feet
result = (
    result.moveTo(-arc_width/2 + foot_width/2, -arc_radius + foot_height/2)
    .rect(foot_width, foot_height)
    .extrude(-foot_depth)
)

result = (
    result.moveTo(arc_width/2 - foot_width/2, -arc_radius + foot_height/2)
    .rect(foot_width, foot_height)
    .extrude(-foot_depth)
)

# Create a cleaner version that focuses on the core requirements
result = cq.Workplane("XY").box(arc_width, arc_radius * 2, thickness)

# Add tabs on top
result = result.faces(">Z").workplane()

# Left tab
result = (
    result.moveTo(-arc_width/2 - tab_width/2, 0)
    .rect(tab_width, tab_height)
    .extrude(thickness)
)

# Right tab
result = (
    result.moveTo(arc_width/2 + tab_width/2, 0)
    .rect(tab_width, tab_height)
    .extrude(thickness)
)

# Center tab
result = (
    result.moveTo(0, 0)
    .rect(tab_width, tab_height)
    .extrude(thickness)
)

# Add cutouts along the sides
cutout_positions = [-arc_radius + 10, -arc_radius + 25, -arc_radius + 40]

for pos in cutout_positions:
    result = (
        result.faces(">X")
        .workplane(offset=thickness/2)
        .moveTo(0, pos)
        .rect(cutout_width, cutout_height)
        .cutBlind(-thickness)
    )

# Add feet at bottom
result = result.faces("<Z").workplane()

# Add feet
result = (
    result.moveTo(-arc_width/2 + foot_width/2, -arc_radius + foot_height/2)
    .rect(foot_width, foot_height)
    .extrude(-foot_depth)
)

result = (
    result.moveTo(arc_width/2 - foot_width/2, -arc_radius + foot_height/2)
    .rect(foot_width, foot_height)
    .extrude(-foot_depth)
)

# Final clean version
result = cq.Workplane("XY").box(arc_width, arc_radius * 2, thickness)

# Add tabs on top
result = result.faces(">Z").workplane()

# Left tab
result = (
    result.moveTo(-arc_width/2 - tab_width/2, 0)
    .rect(tab_width, tab_height)
    .extrude(thickness)
)

# Right tab
result = (
    result.moveTo(arc_width/2 + tab_width/2, 0)
    .rect(tab_width, tab_height)
    .extrude(thickness)
)

# Center tab
result = (
    result.moveTo(0, 0)
    .rect(tab_width, tab_height)
    .extrude(thickness)
)

# Add cutouts along the sides
cutout_positions = [-arc_radius + 10, -arc_radius + 25, -arc_radius + 40]

for pos in cutout_positions:
    result = (
        result.faces(">X")
        .workplane(offset=thickness/2)
        .moveTo(0, pos)
        .rect(cutout_width, cutout_height)
        .cutBlind(-thickness)
    )

# Add feet at bottom
result = result.faces("<Z").workplane()

# Add feet
result = (
    result.moveTo(-arc_width/2 + foot_width/2, -arc_radius + foot_height/2)
    .rect(foot_width, foot_height)
    .extrude(-foot_depth)
)

result = (
    result.moveTo(arc_width/2 - foot_width/2, -arc_radius + foot_height/2)
    .rect(foot_width, foot_height)
    .extrude(-foot_depth)
)

# Simplified final version
result = cq.Workplane("XY").box(arc_width, arc_radius * 2, thickness)

# Add tabs on top
result = result.faces(">Z").workplane()

# Add tabs at ends and center
result = (
    result.moveTo(-arc_width/2 - tab_width/2, 0)
    .rect(tab_width, tab_height)
    .extrude(thickness)
)

result = (
    result.moveTo(arc_width/2 + tab_width/2, 0)
    .rect(tab_width, tab_height)
    .extrude(thickness)
)

result = (
    result.moveTo(0, 0)
    .rect(tab_width, tab_height)
    .extrude(thickness)
)

# Add cutouts along the sides
cutout_positions = [-arc_radius + 10, -arc_radius + 25, -arc_radius + 40]

for pos in cutout_positions:
    result = (
        result.faces(">X")
        .workplane(offset=thickness/2)
        .moveTo(0, pos)
        .rect(cutout_width, cutout_height)
        .cutBlind(-thickness)
    )

# Add feet at bottom
result = result.faces("<Z").workplane()

# Add feet
result = (
    result.moveTo(-arc_width/2 + foot_width/2, -arc_radius + foot_height/2)
    .rect(foot_width, foot_height)
    .extrude(-foot_depth)
)

result = (
    result.moveTo(arc_width/2 - foot_width/2, -arc_radius + foot_height/2)
    .rect(foot_width, foot_height)
    .extrude(-foot_depth)
)

# Final version with better structure
result = cq.Workplane("XY").box(arc_width, arc_radius * 2, thickness)

# Add tabs on top surface
result = result.faces(">Z").workplane()

# Left tab
result = (
    result.moveTo(-arc_width/2 - tab_width/2, 0)
    .rect(tab_width, tab_height)
    .extrude(thickness)
)

# Right tab
result = (
    result.moveTo(arc_width/2 + tab_width/2, 0)
    .rect(tab_width, tab_height)
    .extrude(thickness)
)

# Center tab
result = (
    result.moveTo(0, 0)
    .rect(tab_width, tab_height)
    .extrude(thickness)
)

# Add cutouts on the side faces
cutout_positions = [-arc_radius + 10, -arc_radius + 25, -arc_radius + 40]

for pos in cutout_positions:
    result = (
        result.faces(">X")
        .workplane(offset=thickness/2)
        .moveTo(0, pos)
        .rect(cutout_width, cutout_height)
        .cutBlind(-thickness)
    )

# Add feet at bottom
result = result.faces("<Z").workplane()

# Add feet
result = (
    result.moveTo(-arc_width/2 + foot_width/2, -arc_radius + foot_height/2)
    .rect(foot_width, foot_height)
    .extrude(-foot_depth)
)

result = (
    result.moveTo(arc_width/2 - foot_width/2, -arc_radius + foot_height/2)
    .rect(foot_width, foot_height)
    .extrude(-foot_depth)
)