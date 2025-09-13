import cadquery as cq

# Define cone parameters
base_radius = 2.0
height = 4.0

# Create a cone with circular base and tapering sides to apex
result = cq.Workplane("XY").circle(base_radius).extrude(height)