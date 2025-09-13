import cadquery as cq

# Dimensions
length = 200.0
width = 100.0
height = 50.0
drawer_front_offset = 15.0
divider_thickness = 5.0
drawer_front_thickness = 8.0

# Create the main box
result = cq.Workplane("XY").box(length, width, height)

# Create the drawer front recess
drawer_front = (
    cq.Workplane("XY")
    .box(length - drawer_front_thickness, width, height)
    .translate((drawer_front_offset, 0, 0))
)

# Subtract the drawer front from the main box
result = result.cut(drawer_front)

# Create internal dividers
# We'll create 4 dividers that divide the drawer into 5 compartments
compartment_width = (length - 4 * divider_thickness) / 5

# Create the dividers
for i in range(4):
    divider_x = (i + 1) * (compartment_width + divider_thickness) - divider_thickness/2
    divider = (
        cq.Workplane("XY")
        .box(divider_thickness, width, height)
        .translate((divider_x, 0, 0))
    )
    result = result.cut(divider)

# Create the drawer front with proper offset
drawer_front_final = (
    cq.Workplane("XY")
    .box(drawer_front_thickness, width, height)
    .translate((drawer_front_offset - drawer_front_thickness/2, 0, 0))
)

result = result.union(drawer_front_final)

# Since we want to show a partially open drawer, we'll also add a cutout
# to represent the sliding mechanism
mechanism_cutout = (
    cq.Workplane("XY")
    .box(20, width, 10)
    .translate((drawer_front_offset - 10, 0, height - 10))
)
result = result.cut(mechanism_cutout)

# Add some aesthetic details - small recesses on the sides
side_recess = (
    cq.Workplane("XY")
    .box(5, 10, 5)
    .translate((length/2 - 2.5, width/2 - 5, height - 5))
)
result = result.cut(side_recess)

side_recess2 = (
    cq.Workplane("XY")
    .box(5, 10, 5)
    .translate((-length/2 + 2.5, width/2 - 5, height - 5))
)
result = result.cut(side_recess2)