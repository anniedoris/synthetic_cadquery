import cadquery as cq

# Parameters for the conical segment
outer_radius = 10.0
inner_radius = 7.0
height = 15.0
thickness = 1.5
angle = 90.0  # degrees of the sector

# Create the outer conical segment
outer_cone = (
    cq.Workplane("XY")
    .circle(outer_radius)
    .workplane(offset=height)
    .circle(outer_radius * 0.5)  # taper the top
    .loft(combine=True)
)

# Create the inner conical segment
inner_cone = (
    cq.Workplane("XY")
    .circle(inner_radius)
    .workplane(offset=height - thickness)
    .circle(inner_radius * 0.5)  # taper the top
    .loft(combine=True)
)

# Create the hollow object by subtracting inner from outer
result = outer_cone.cut(inner_cone)

# Add a slight inclination to the top face by rotating the top face
# Create a workplane at the top and adjust the angle
result = (
    result.faces(">Z")
    .workplane()
    .transformed(rotate=cq.Vector(0, 5, 0))  # slight tilt
    .rect(20, 20)  # just to show the transformation
)