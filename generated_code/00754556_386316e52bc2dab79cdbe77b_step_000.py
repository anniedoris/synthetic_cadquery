import cadquery as cq

# Define dimensions
length = 100.0
width = 60.0
thickness = 5.0

# Create first rectangle (base plate)
plate1 = cq.Workplane("XY").box(length, width, thickness)

# Create second rectangle, rotated and positioned to overlap
# Rotate 15 degrees around Z axis and offset to create overlap
plate2 = (
    cq.Workplane("XY")
    .box(length, width, thickness)
    .rotate((0, 0, 0), (0, 0, 1), 15)  # Rotate 15 degrees around Z
    .translate((20, 20, 0))  # Offset to create overlap
)

# Combine both plates
result = plate1.union(plate2)