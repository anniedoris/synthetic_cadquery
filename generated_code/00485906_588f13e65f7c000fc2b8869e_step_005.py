import cadquery as cq

# Create a cuboid with dimensions that will show the 3D effect when tilted
# Using dimensions that will create a good perspective view
length = 4.0
width = 3.0
height = 2.0

# Create the base cuboid
result = cq.Workplane("XY").box(length, width, height)

# Rotate it to create the angled perspective shown in the description
# This will tilt the object to show one face prominently while revealing the 3D form
result = result.rotate((0, 0, 0), (1, 1, 0), 30)  # Rotate around diagonal axis
result = result.rotate((0, 0, 0), (0, 0, 1), 15)  # Additional rotation for better perspective

# The rotation creates the 3D effect where one face is prominent and edges recede
# The shading effect is handled by the rendering software, not the CAD code