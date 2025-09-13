import cadquery as cq

# Define dimensions for the stepped platform
lower_width = 100.0
lower_depth = 80.0
lower_height = 20.0

upper_width = 60.0
upper_depth = 40.0
upper_height = 30.0

# Create the lower level
result = cq.Workplane("XY").box(lower_width, lower_depth, lower_height)

# Create the upper level, centered on the lower level
result = (
    result.faces(">Z")
    .workplane()
    .rect(upper_width, upper_depth, forConstruction=True)
    .vertices()
    .hole(5.0)  # Add holes for aesthetic/functional purposes
    .center((lower_width - upper_width) / 2, (lower_depth - upper_depth) / 2)
    .box(upper_width, upper_depth, upper_height)
)

# Add a slight fillet to the edges for a more refined look
result = result.edges("|Z").fillet(2.0)

# Ensure the final object is properly aligned
result = result.faces(">Z").workplane().rect(upper_width, upper_depth, forConstruction=True).vertices().hole(3.0)

# The final result is the stepped platform with two distinct levels