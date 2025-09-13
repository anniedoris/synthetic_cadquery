import cadquery as cq

# Define ellipse parameters
major_axis = 4.0
minor_axis = 2.0

# Create an ellipse
result = cq.Workplane("XY").ellipse(major_axis, minor_axis)