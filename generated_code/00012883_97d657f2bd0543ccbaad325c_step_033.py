import cadquery as cq

# Create a rectangular prism that is elongated (length >> width and height)
# This represents a straight rod or beam with consistent cross-section
result = cq.Workplane("front").box(2.0, 2.0, 20.0)