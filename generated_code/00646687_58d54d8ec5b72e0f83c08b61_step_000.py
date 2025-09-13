import cadquery as cq
from math import sin, cos, pi

# Define dimensions
diameter = 40.0
thickness = 3.0
edge_height = 1.0
inscription_depth = 0.3

# Create the base coin
coin = cq.Workplane("XY").circle(diameter/2).extrude(thickness)

# Create the raised design on top face
# This is a simplified representation of a human figure with some abstract elements
# In a real implementation, this would be much more complex
top_face = coin.faces(">Z").workplane()

# Create a simplified human figure design
# Head (circle)
top_face = top_face.center(0, 8).circle(3).extrude(0.8)

# Body (rectangle)
top_face = top_face.center(0, -2).rect(4, 6, centered=True).extrude(0.8)

# Arm up (rectangle)
top_face = top_face.center(0, 2).rect(1.5, 5, centered=True).extrude(0.8)

# Arm down (rectangle)
top_face = top_face.center(0, -4).rect(1.5, 4, centered=True).extrude(0.8)

# Hair/Headdress (simple arc)
top_face = top_face.center(0, 10).circle(4).extrude(0.5)

# Add some abstract elements (horse-like shape)
top_face = top_face.center(10, 0).circle(2).extrude(0.6)
top_face = top_face.center(12, 0).circle(1).extrude(0.6)

# Create the edge inscription
# We'll create a curved path for the inscription
edge_path = cq.Workplane("XY").center(0, 0).circle(diameter/2 - 1).workplane(offset=thickness/2)

# For simplicity, we'll just add a text feature along the edge
# In a real implementation, this would be more complex
edge_inscription = (
    coin.faces("<Z")
    .workplane(offset=-0.5)
    .center(0, diameter/2 - 1)
    .rect(10, 1, centered=True)
    .extrude(inscription_depth)
)

# Combine the main coin with the edge inscription
result = coin.union(edge_inscription)

# Add a raised edge to simulate the "IRELAND" inscription
# Create a circular edge profile for the inscription
edge_profile = (
    cq.Workplane("XY")
    .center(0, 0)
    .circle(diameter/2)
    .workplane(offset=thickness)
    .circle(diameter/2 - 0.5)
    .loft()
)

# This approach is simplified - in practice you'd want to create a more accurate
# text path along the edge and use it for the cut
result = result.faces(">Z").workplane().circle(diameter/2 - 1).cutBlind(-inscription_depth)