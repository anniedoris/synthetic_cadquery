import cadquery as cq

# Dimensions
length = 100.0
width = 30.0
height = 5.0
hole_diameter = 4.0
hole_spacing = length / 6.0  # 6 spaces for 5 holes

# Create the base plate
result = cq.Workplane("XY").box(length, width, height)

# Add holes
for i in range(5):
    x_pos = -length/2 + (i + 1) * hole_spacing
    result = (
        result.faces(">Z")
        .workplane(offset=0.1)  # Slightly above top surface
        .center(x_pos, 0)
        .hole(hole_diameter)
    )

# Ensure the holes go through the entire thickness
result = result.faces(">Z").workplane().hole(hole_diameter)