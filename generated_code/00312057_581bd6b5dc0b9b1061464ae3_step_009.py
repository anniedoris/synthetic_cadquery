import cadquery as cq

# Create a cylinder with diameter 4 and height 2
# This gives a diameter-to-height ratio of 2:1, making it appear flat
result = cq.Workplane("XY").circle(2.0).extrude(2.0)