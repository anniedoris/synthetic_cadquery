import cadquery as cq

# Define dimensions
outer_diameter = 20.0
inner_diameter = 10.0
height = 5.0

# Create the cylindrical part with a hollow center
result = (
    cq.Workplane("XY")
    .circle(outer_diameter / 2.0)  # Create outer cylinder
    .extrude(height)               # Extrude to given height
    .faces(">Z")                   # Select top face
    .workplane()                   # Create workplane on top face
    .circle(inner_diameter / 2.0)  # Create inner hole
    .cutThruAll()                  # Cut through entire height
)