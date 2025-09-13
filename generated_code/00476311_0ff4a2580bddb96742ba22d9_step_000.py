import cadquery as cq

# Define dimensions
length = 50.0   # width
width = 30.0    # height  
thickness = 10.0 # depth

# Define circular feature
hole_diameter = 12.0
hole_depth = 6.0

# Create the base block
result = cq.Workplane("XY").box(length, width, thickness)

# Add the circular recess on the top face
result = (
    result.faces(">Z")
    .workplane()
    .circle(hole_diameter / 2.0)
    .cutBlind(hole_depth)
)