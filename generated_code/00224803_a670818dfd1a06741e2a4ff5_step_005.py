import cadquery as cq

# Define dimensions
base_length = 50.0
base_width = 30.0
base_height = 10.0
cylinder_diameter = 12.0
cylinder_height = base_height
protrusion_length = 20.0
protrusion_width = 15.0
protrusion_height = 12.0
hollow_depth = 15.0
notch_width = 5.0
notch_height = 3.0
notch_depth = 8.0

# Create the base rectangular prism
result = cq.Workplane("XY").box(base_length, base_width, base_height)

# Add the cylindrical extension on the right side
result = (
    result.faces(">Y")
    .workplane()
    .circle(cylinder_diameter / 2.0)
    .extrude(cylinder_height)
)

# Add the rectangular protrusion on top
result = (
    result.faces(">Z")
    .workplane()
    .center(base_length / 2.0 - protrusion_length / 2.0, 0)
    .rect(protrusion_length, protrusion_width)
    .extrude(protrusion_height)
)

# Create the curved hollow section on the right side
# First, create a workplane on the right face of the base
result = (
    result.faces(">Y")
    .workplane()
    .center(0, -base_width / 2.0 + hollow_depth / 2.0)
    .rect(hollow_depth, base_height)
    .cutBlind(-hollow_depth / 2.0)
)

# Create the curved U-shape hollow section
# Create a circular arc and then cut it out
result = (
    result.faces(">Y")
    .workplane()
    .center(0, -base_width / 2.0 + hollow_depth / 2.0)
    .moveTo(hollow_depth / 2.0, 0)
    .threePointArc((0, hollow_depth / 2.0), (-hollow_depth / 2.0, 0))
    .close()
    .cutBlind(-hollow_depth / 2.0)
)

# Add the small notches on the sides
# Notch on the top edge near the cylinder
result = (
    result.faces(">Z")
    .workplane()
    .center(base_length / 2.0 - notch_depth / 2.0, base_width / 2.0 - notch_width / 2.0)
    .rect(notch_depth, notch_width)
    .cutBlind(-notch_height)
)

# Notch on the bottom edge near the cylinder
result = (
    result.faces("<Z")
    .workplane()
    .center(base_length / 2.0 - notch_depth / 2.0, base_width / 2.0 - notch_width / 2.0)
    .rect(notch_depth, notch_width)
    .cutBlind(-notch_height)
)

# Notch on the top edge near the protrusion
result = (
    result.faces(">Z")
    .workplane()
    .center(-base_length / 2.0 + notch_depth / 2.0, base_width / 2.0 - notch_width / 2.0)
    .rect(notch_depth, notch_width)
    .cutBlind(-notch_height)
)

# Notch on the bottom edge near the protrusion
result = (
    result.faces("<Z")
    .workplane()
    .center(-base_length / 2.0 + notch_depth / 2.0, base_width / 2.0 - notch_width / 2.0)
    .rect(notch_depth, notch_width)
    .cutBlind(-notch_height)
)

# Ensure we have the final result
result = result