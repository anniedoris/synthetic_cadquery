import cadquery as cq

# Dimensions
base_diameter = 50.0
base_thickness = 5.0
shaft_diameter = 10.0
shaft_height = 15.0
indenture_diameter = 3.0
ridge_height = 1.0
ridge_width = 3.0

# Create the base plate
result = cq.Workplane("XY").circle(base_diameter/2).extrude(base_thickness)

# Add the annular ridge/chamfer around the perimeter
result = (
    result.faces(">Z")
    .workplane()
    .circle(base_diameter/2 - ridge_width)
    .circle(base_diameter/2)
    .extrude(ridge_height)
)

# Create the central shaft
result = (
    result.faces(">Z")
    .workplane()
    .circle(shaft_diameter/2)
    .extrude(shaft_height)
)

# Create the indentation on the top of the shaft
result = (
    result.faces(">Z")
    .workplane()
    .circle(indenture_diameter/2)
    .cutBlind(-1.0)
)

result = result.translate((0, 0, base_thickness/2))