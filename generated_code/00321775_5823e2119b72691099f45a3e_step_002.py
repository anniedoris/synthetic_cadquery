import cadquery as cq
from math import pi

# Base bracket dimensions
bracket_width = 40.0
bracket_height = 20.0
bracket_thickness = 5.0
cutout_width = 20.0
cutout_height = 10.0
hole_diameter = 6.0

# Threaded rod dimensions
rod_diameter = 8.0
rod_length = 30.0

# Spring dimensions
spring_outer_diameter = 10.0
spring_inner_diameter = 6.0
spring_height = 15.0

# Top cylindrical component dimensions
top_cylinder_diameter = 12.0
top_cylinder_height = 8.0
protrusion_diameter = 4.0
protrusion_height = 3.0

# Create the base bracket
bracket = (
    cq.Workplane("XY")
    .box(bracket_width, bracket_height, bracket_thickness)
    .faces(">Z")
    .workplane()
    .rect(cutout_width, cutout_height, forConstruction=True)
    .vertices()
    .hole(4.0)
    .faces(">Z")
    .workplane()
    .circle(hole_diameter/2)
    .cutThruAll()
)

# Create the threaded rod
rod = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .circle(rod_diameter/2)
    .extrude(rod_length)
)

# Create the spring (simplified as a helix)
# We'll approximate it with a coiled cylinder
spring = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .circle(spring_inner_diameter/2)
    .extrude(spring_height)
)

# Create the top cylindrical component
top_cylinder = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .circle(top_cylinder_diameter/2)
    .extrude(top_cylinder_height)
    .faces(">Z")
    .workplane()
    .circle(protrusion_diameter/2)
    .extrude(protrusion_height)
)

# Position components
# Position the rod in the bracket
rod = rod.translate((0, 0, bracket_thickness))

# Position the spring on the rod
spring = spring.translate((0, 0, bracket_thickness))

# Position the top cylinder on the rod
top_cylinder = top_cylinder.translate((0, 0, bracket_thickness + rod_length))

# Combine all parts
result = bracket.union(rod).union(spring).union(top_cylinder)

# Add a red color to the spring for visualization
# (Note: Color is not directly supported in CadQuery, but this shows intent)