import cadquery as cq

# Define dimensions
base_length = 40.0
base_width = 25.0
base_thickness = 5.0
cylinder_diameter = 8.0
cylinder_height = 12.0
cylinder_offset = 15.0  # Distance from center to cylinder base

# Create the base plate (elliptical)
base = cq.Workplane("XY").ellipse(base_length, base_width).extrude(base_thickness)

# Create the cylindrical protrusion
cylinder = (
    cq.Workplane("XY")
    .center(cylinder_offset, 0)  # Position near the edge
    .circle(cylinder_diameter / 2.0)
    .extrude(cylinder_height)
)

# Combine the base and cylinder
result = base.union(cylinder)