import cadquery as cq

# Define dimensions
prism_width = 40.0
prism_length = 60.0
prism_height = 20.0

cylinder_diameter = 15.0
cylinder_height = 8.0

# Create the main rectangular prism body
result = cq.Workplane("XY").box(prism_width, prism_length, prism_height)

# Create the cylindrical protrusion
cylinder = cq.Workplane("XY").circle(cylinder_diameter/2).extrude(cylinder_height)

# Position the cylinder on the side of the prism
# Place it centered on the front face of the prism
cylinder = cylinder.translate((0, prism_length/2 + cylinder_diameter/2, 0))

# Combine the prism and cylinder
result = result.union(cylinder)