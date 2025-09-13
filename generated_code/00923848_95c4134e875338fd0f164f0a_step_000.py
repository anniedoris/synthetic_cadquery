import cadquery as cq

# Define dimensions
length = 10.0
width = 8.0
height = 6.0

# Create the open-top rectangular prism
result = (
    cq.Workplane("XY")
    .box(length, width, height)
    .faces(">Z")  # Select the top face
    .shell(-0.1)  # Remove the top face by shelling with small negative thickness
)

# Alternative approach - more explicit removal of top face
# result = cq.Workplane("XY").box(length, width, height)
# result = result.faces(">Z").workplane().rect(length, width).cutThruAll()