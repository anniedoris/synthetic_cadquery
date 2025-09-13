import cadquery as cq

# Define dimensions
diameter = 10.0
length = 50.0
radius = diameter / 2.0

# Create the main cylindrical body
cylinder = cq.Workplane("XY").circle(radius).extrude(length)

# Create hemispherical caps
# First cap at one end
cap1 = cq.Workplane("XY").circle(radius).extrude(radius).translate((0, 0, -radius))

# Second cap at the other end  
cap2 = cq.Workplane("XY").circle(radius).extrude(radius).translate((0, 0, length))

# Combine the parts
result = cylinder.union(cap1).union(cap2)

# Rotate to achieve diagonal orientation
# Rotate 45 degrees around Y axis, then 30 degrees around X axis
result = result.rotate((0, 0, 0), (0, 1, 0), 45)
result = result.rotate((0, 0, 0), (1, 0, 0), 30)