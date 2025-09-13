import cadquery as cq

# Define dimensions
base_length = 50.0
base_width = 30.0
base_height = 10.0
cylinder_diameter = 8.0
cylinder_height = 15.0
pin_diameter = 3.0
pin_height = 3.0

# Create the base with tapered sides
# Start with a box and then create the tapered effect by using a workplane
# at an offset to create the angled sides
result = cq.Workplane("XY").box(base_length, base_width, base_height)

# Create the cylindrical component on top
# Position it near the center of the top surface
result = (
    result.faces(">Z")
    .workplane()
    .center(0, 0)  # Center on the top surface
    .circle(cylinder_diameter / 2.0)
    .extrude(cylinder_height)
)

# Add the smaller pin/connector on top of the cylinder
result = (
    result.faces(">Z")
    .workplane()
    .center(0, 0)
    .circle(pin_diameter / 2.0)
    .extrude(pin_height)
)

# Alternative approach to create a more realistic tapered base:
# Create a rectangular prism and then add the cylinder on top
result = cq.Workplane("XY").box(base_length, base_width, base_height)

# Add the cylinder
result = (
    result.faces(">Z")
    .workplane()
    .center(0, 0)
    .circle(cylinder_diameter / 2.0)
    .extrude(cylinder_height)
)

# Add the pin
result = (
    result.faces(">Z")
    .workplane()
    .center(0, 0)
    .circle(pin_diameter / 2.0)
    .extrude(pin_height)
)