import cadquery as cq

# Create the main housing body
# Overall dimensions
length = 100.0
width = 60.0
height = 40.0

# Create the basic housing shape with curved top and bottom
housing = cq.Workplane("XY").box(length, width, height)

# Create curved top surface by removing material from the top
top_curve = (
    cq.Workplane("XY")
    .box(length, width, height)
    .faces(">Z")
    .workplane()
    .circle(30)
    .extrude(2)
)

# Create curved bottom surface
bottom_curve = (
    cq.Workplane("XY")
    .box(length, width, height)
    .faces("<Z")
    .workplane()
    .circle(25)
    .extrude(2)
)

# Combine the housing with the curved features
housing = housing.union(top_curve).union(bottom_curve)

# Create the internal compartments
# Left compartment - rectangular with flat base
left_compartment = (
    cq.Workplane("XY")
    .box(length, width, height)
    .faces("<X")
    .workplane()
    .rect(40, 40)
    .extrude(30)
)

# Right compartment - more complex with curved base
right_compartment = (
    cq.Workplane("XY")
    .box(length, width, height)
    .faces(">X")
    .workplane()
    .circle(20)
    .extrude(25)
)

# Combine compartments with housing
housing = housing.cut(left_compartment).cut(right_compartment)

# Add vertical supports
vertical_supports = cq.Workplane("XY").box(length, width, height)
for i in range(5):
    x_pos = -length/2 + (i * length/4)
    support = (
        cq.Workplane("XY")
        .box(length, width, height)
        .faces("<X")
        .workplane(offset=x_pos)
        .rect(2, 30)
        .extrude(35)
    )
    vertical_supports = vertical_supports.union(support)

# Add horizontal supports
horizontal_supports = cq.Workplane("XY").box(length, width, height)
for i in range(3):
    y_pos = -width/2 + (i * width/2)
    support = (
        cq.Workplane("XY")
        .box(length, width, height)
        .faces("<Y")
        .workplane(offset=y_pos)
        .rect(80, 2)
        .extrude(35)
    )
    horizontal_supports = horizontal_supports.union(support)

# Combine all supports with housing
housing = housing.union(vertical_supports).union(horizontal_supports)

# Create the curved base for the right compartment
right_curve_base = (
    cq.Workplane("XY")
    .box(length, width, height)
    .faces(">X")
    .workplane()
    .circle(18)
    .extrude(5)
)

housing = housing.union(right_curve_base)

# Add internal dividers for better compartmentalization
divider = (
    cq.Workplane("XY")
    .box(length, width, height)
    .faces("<X")
    .workplane(offset=-20)
    .rect(2, 30)
    .extrude(30)
)
housing = housing.union(divider)

# Create a lid/cover for the housing
lid = (
    cq.Workplane("XY")
    .box(length, width, 5)
    .faces(">Z")
    .workplane()
    .circle(25)
    .extrude(2)
)

# Final result
result = housing.union(lid)