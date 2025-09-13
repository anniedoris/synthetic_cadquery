import cadquery as cq

# Create a cylinder with radius 2 and height 8
result = cq.Workplane("XY").circle(2).extrude(8)

# Rotate the cylinder to give it a diagonal appearance
# Rotate 45 degrees around the X-axis and 30 degrees around the Y-axis
result = result.rotate((0, 0, 0), (1, 0, 0), 45)
result = result.rotate((0, 0, 0), (0, 1, 0), 30)