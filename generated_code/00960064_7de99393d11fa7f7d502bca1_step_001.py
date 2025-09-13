import cadquery as cq

# Define dimensions
width = 10.0      # Width of the cross-section
height = 20.0     # Height of the cross-section (2x width)
length = 100.0    # Length of the prism
cap_offset = 2.0  # Offset for the end caps
cap_thickness = 5.0  # Thickness of the end caps

# Create the main prism
result = cq.Workplane("XY").box(length, width, height)

# Create left end cap
left_cap = (
    cq.Workplane("XY")
    .box(cap_thickness, width, height)
    .translate((-length/2 - cap_thickness/2, 0, 0))
)

# Create right end cap
right_cap = (
    cq.Workplane("XY")
    .box(cap_thickness, width, height)
    .translate((length/2 + cap_thickness/2, 0, 0))
)

# Combine the main prism with the end caps
result = result.union(left_cap).union(right_cap)

# Add holes to left end cap
result = (
    result.faces("<X")
    .workplane()
    .circle(2.0)
    .cutThruAll()
)

# Add holes to right end cap
result = (
    result.faces(">X")
    .workplane()
    .circle(2.0)
    .cutThruAll()
)