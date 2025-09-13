import cadquery as cq

# Define dimensions
length = 10.0
width = 10.0
height = 10.0
thickness = 1.0

# Create the base box
result = cq.Workplane("XY").box(length, width, height)

# Remove the front face to create an open box
# We'll cut a box that represents the front opening
front_cut = (
    cq.Workplane("XY")
    .box(length, thickness, height)
    .translate((0, -width/2 + thickness/2, 0))
)

# Subtract the front opening from the main box
result = result.cut(front_cut)

# Add some thickness to make it a proper hollow box
# Create the outer box
outer_box = cq.Workplane("XY").box(length, width, height)

# Create the inner box (hollow part)
inner_box = cq.Workplane("XY").box(length - 2*thickness, width - 2*thickness, height - thickness)

# Position the inner box to be centered
inner_box = inner_box.translate((0, 0, thickness/2))

# Create the hollow box by subtracting inner from outer
result = outer_box.cut(inner_box)

# Remove the front face to create the open container
# Create a box that represents the front opening
front_opening = (
    cq.Workplane("XY")
    .box(length, thickness, height)
    .translate((0, -width/2 + thickness/2, 0))
)

# Subtract the front opening
result = result.cut(front_opening)

# Alternative approach: simpler way to make an open box
# Create a solid rectangular prism
result = cq.Workplane("XY").box(length, width, height)

# Remove the front face by cutting a box in that position
front_face_cut = (
    cq.Workplane("XY")
    .box(length, thickness, height)
    .translate((0, -width/2 + thickness/2, 0))
)
result = result.cut(front_face_cut)

# Better approach - create a hollow box with one face missing
# Start with a solid box
base_box = cq.Workplane("XY").box(length, width, height)

# Create a hollow box by subtracting an inner box
inner_box = cq.Workplane("XY").box(length - 2*thickness, width - 2*thickness, height - thickness)
inner_box = inner_box.translate((0, 0, thickness/2))

# Make the box hollow
hollow_box = base_box.cut(inner_box)

# Remove the front face to make it open
front_face = (
    cq.Workplane("XY")
    .box(length, thickness, height)
    .translate((0, -width/2 + thickness/2, 0))
)

result = hollow_box.cut(front_face)