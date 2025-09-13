import cadquery as cq

# Define dimensions
length = 100.0
width = 20.0
height = 10.0
hole_diameter = 4.0  # One-fifth of width
indentation_diameter = 2.0
taper_width = 15.0  # Width at the tapered end

# Create the base rectangular prism with taper
result = cq.Workplane("XY").box(length, width, height)

# Apply taper to the left end (subtract a wedge)
# Create a wedge to subtract from the left end
wedge = (
    cq.Workplane("XY")
    .moveTo(-length/2, width/2)
    .lineTo(-length/2 + 10, taper_width/2)
    .lineTo(-length/2 + 10, -taper_width/2)
    .lineTo(-length/2, -width/2)
    .close()
    .extrude(height)
)

# Subtract the wedge from the left end
result = result.cut(wedge)

# Create the cylindrical hole near the right end, slightly towards the bottom
result = (
    result.faces(">X")
    .workplane(offset=-height/2 + 2)  # Slightly towards the bottom
    .center(-length/2 + 10, 0)  # Position near the right end
    .hole(hole_diameter)
)

# Create the circular indentation near the center on the top surface
result = (
    result.faces(">Z")
    .workplane()
    .center(0, 0)
    .circle(indentation_diameter/2)
    .cutBlind(-2)  # Cut shallow recess
)

# Ensure sharp edges and corners by not adding any fillets
# The object maintains its rectangular prism shape with the taper and features