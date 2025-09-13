import cadquery as cq

# Define dimensions
top_diameter = 20.0
bottom_diameter = 16.0
inner_diameter = 8.0
height = 10.0
taper_angle = 5.0  # degrees

# Create the outer cylindrical shape with taper
result = (
    cq.Workplane("XY")
    .circle(top_diameter / 2.0)  # Top face
    .workplane(offset=height * (1 - taper_angle / 90.0))  # Adjust for taper
    .circle(bottom_diameter / 2.0)  # Bottom face
    .loft(combine=True)
)

# Create the inner cylindrical passage
result = result.faces(">Z").workplane().circle(inner_diameter / 2.0).cutThruAll()

# Ensure we have a proper solid by removing any potential issues
result = result.clean()

# Final result
result = result