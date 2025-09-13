import cadquery as cq

# Component 1: Curved cylindrical segment with flat side
# Define dimensions
length1 = 40.0
height1 = 20.0
thickness1 = 5.0
radius1 = 25.0

# Create the first component
component1 = (
    cq.Workplane("XY")
    .moveTo(-length1/2, 0)
    .lineTo(length1/2, 0)
    .threePointArc((0, radius1), (-length1/2, 0))
    .close()
    .extrude(thickness1)
    .edges("|Z").fillet(2.0)
)

# Component 2: Partial U-shape with flat side
# Define dimensions
length2 = 40.0
height2 = 20.0
thickness2 = 5.0
radius2 = 30.0

# Create the second component
component2 = (
    cq.Workplane("XY")
    .moveTo(-length2/2, 0)
    .lineTo(length2/2, 0)
    .threePointArc((0, -radius2), (-length2/2, 0))
    .close()
    .extrude(thickness2)
    .edges("|Z").fillet(2.0)
)

# Position components for interlocking
# Component 1 is positioned at the origin
# Component 2 is rotated and positioned to interlock with component 1
component2 = component2.rotate((0, 0, 0), (0, 0, 1), 180).translate((0, 0, thickness1))

# Combine components for final result
result = component1.union(component2)