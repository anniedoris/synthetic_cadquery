import cadquery as cq

# Define dimensions for the washer
outer_diameter = 20.0
inner_diameter = 8.0
thickness = 3.0

# Create the washer
result = (
    cq.Workplane("XY")
    .circle(outer_diameter / 2.0)  # Create outer circle
    .circle(inner_diameter / 2.0)   # Create inner circle (hole)
    .extrude(thickness)            # Extrude to create the cylindrical shape
)

# The result is a flat washer with a central hole