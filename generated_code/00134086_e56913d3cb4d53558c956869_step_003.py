import cadquery as cq

# Define dimensions for the cylindrical sleeve/bushing
outer_diameter = 20.0
inner_diameter = 12.0
length = 30.0

# Create the hollow cylinder (sleeve/bushing)
result = (
    cq.Workplane("XY")
    .circle(outer_diameter / 2.0)  # Outer circle
    .circle(inner_diameter / 2.0)   # Inner circle (creates the hollow)
    .extrude(length)                # Extrude along the Z-axis to form the cylinder
)

# The resulting object is a hollow cylinder with:
# - Outer diameter: 20.0
# - Inner diameter: 12.0
# - Length: 30.0
# The wall thickness is (20.0 - 12.0) / 2 = 4.0