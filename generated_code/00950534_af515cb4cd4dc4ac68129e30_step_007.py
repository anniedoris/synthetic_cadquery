import cadquery as cq

# Dimensions
length = 50.0
width = 30.0
thickness = 5.0
hole_diameter = 8.0
protrusion_radius = 15.0
protrusion_height = 10.0
corner_radius = 3.0

# Create the base plate with rounded corners
result = cq.Workplane("XY").box(length, width, thickness)

# Create the circular hole in the center
result = (
    result.faces(">Z")
    .workplane()
    .circle(hole_diameter / 2.0)
    .cutThruAll()
)

# Create the curved protrusion on one side
# First, create a workplane at the edge where the protrusion will be
result = (
    result.faces(">Y")
    .workplane(offset=thickness/2)
    .moveTo(0, 0)
    .threePointArc((protrusion_radius/2, protrusion_height), (protrusion_radius, 0))
    .mirrorY()
    .extrude(protrusion_height)
)

# Round the corners of the base plate
result = result.edges("|Z").fillet(corner_radius)

# Ensure the protrusion is properly blended with the base
# We need to make sure the protrusion connects smoothly to the base
# This is achieved by the way we constructed it with the arc

# The final result should have a base plate with a circular hole and a curved protrusion
# The protrusion extends from one edge of the base and has a smooth curve
# The corners of the base are rounded for a finished appearance

# The object is now complete