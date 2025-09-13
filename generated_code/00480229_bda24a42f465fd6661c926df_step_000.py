import cadquery as cq

# Define dimensions
base_length = 50.0
base_width = 30.0
base_height = 5.0

flange1_length = 20.0
flange1_width = 8.0
flange1_height = 15.0

flange2_length = 25.0
flange2_width = 10.0
flange2_height = 15.0

top_slope_length = 30.0
top_slope_width = 40.0
top_slope_height = 8.0

# Create the base
result = cq.Workplane("XY").box(base_length, base_width, base_height)

# Add the left flange
result = (
    result.faces(">Z")
    .workplane(offset=base_height)
    .rect(flange1_length, flange1_width, forConstruction=True)
    .vertices()
    .rect(flange1_length, flange1_width)
    .extrude(flange1_height)
)

# Add the right flange
result = (
    result.faces(">Z")
    .workplane(offset=base_height)
    .rect(flange2_length, flange2_width, forConstruction=True)
    .vertices()
    .rect(flange2_length, flange2_width)
    .extrude(flange2_height)
)

# Create the sloped top section
# First, get the top faces of both flanges
result = (
    result.faces(">Z")
    .workplane(offset=base_height + flange1_height)
    .rect(top_slope_length, top_slope_width, forConstruction=True)
    .vertices()
    .rect(top_slope_length, top_slope_width)
    .extrude(top_slope_height)
)

# Create a trapezoidal top surface by cutting a wedge
# This creates the sloped connection between the flanges
result = (
    result.faces(">Z")
    .workplane(offset=base_height + flange1_height + top_slope_height)
    .moveTo(-top_slope_length/2, -top_slope_width/2)
    .lineTo(top_slope_length/2, -top_slope_width/2)
    .lineTo(top_slope_length/3, top_slope_width/2)
    .lineTo(-top_slope_length/3, top_slope_width/2)
    .close()
    .extrude(2.0)
)

# Create the final top surface by cutting a trapezoid from the top
# This gives the object its trapezoidal appearance from top view
result = (
    result.faces(">Z")
    .workplane(offset=base_height + flange1_height + top_slope_height)
    .moveTo(-top_slope_length/2, -top_slope_width/2)
    .lineTo(top_slope_length/2, -top_slope_width/2)
    .lineTo(top_slope_length/3, top_slope_width/2)
    .lineTo(-top_slope_length/3, top_slope_width/2)
    .close()
    .cutBlind(-2.0)
)

# Refine edges to ensure sharp corners
result = result.edges("|Z").fillet(0.5)

# Adjust for precise geometry
result = result.faces(">Z").workplane().rect(top_slope_length, top_slope_width).extrude(2.0)

# Final refinement
result = result.edges("|Z").fillet(0.5)