import cadquery as cq
from math import pi, sqrt

# Define dice parameters
dice_size = 20.0
corner_radius = 2.0
indentation_diameter = 2.5
indentation_depth = 1.5

# Create the first die (top die)
die1 = cq.Workplane("XY").box(dice_size, dice_size, dice_size).edges("|Z").fillet(corner_radius)

# Add indentations for faces showing 1, 5, and 4
# Face showing 1 (center)
die1 = die1.faces(">Z").workplane().center(0, 0).circle(indentation_diameter/2).cutBlind(-indentation_depth)

# Face showing 5 (center + 4 corners)
die1 = die1.faces("<Z").workplane().center(0, 0).circle(indentation_diameter/2).cutBlind(-indentation_depth)
die1 = die1.faces("<Z").workplane().pushPoints([(-5, 5), (5, 5), (-5, -5), (5, -5)]).circle(indentation_diameter/2).cutBlind(-indentation_depth)

# Face showing 4 (all 4 corners)
die1 = die1.faces(">Y").workplane().pushPoints([(-5, 5), (5, 5), (-5, -5), (5, -5)]).circle(indentation_diameter/2).cutBlind(-indentation_depth)

# Create the second die (bottom die)
die2 = cq.Workplane("XY").box(dice_size, dice_size, dice_size).edges("|Z").fillet(corner_radius)

# Add indentations for faces showing 6, 2, and 3
# Face showing 6 (all 6 corners)
die2 = die2.faces(">Z").workplane().pushPoints([(-5, 5), (5, 5), (-5, -5), (5, -5), (-5, 0), (5, 0)]).circle(indentation_diameter/2).cutBlind(-indentation_depth)

# Face showing 2 (2 corners)
die2 = die2.faces("<Z").workplane().pushPoints([(-5, 5), (5, 5)]).circle(indentation_diameter/2).cutBlind(-indentation_depth)

# Face showing 3 (3 corners)
die2 = die2.faces("<Y").workplane().pushPoints([(-5, 5), (5, 5), (0, 5)]).circle(indentation_diameter/2).cutBlind(-indentation_depth)

# Position the dice in isometric view
# Move the second die below the first one
die2 = die2.translate((0, 0, -dice_size))

# Combine the two dice
result = die1.union(die2)