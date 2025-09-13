import cadquery as cq

# Dimensions
base_length = 40.0
base_width = 20.0
base_thickness = 5.0

cylinder_diameter = 12.0
cylinder_length = 25.0
cylinder_offset = 5.0

arm_curvature_radius = 15.0
arm_thickness = 5.0

second_plate_length = 30.0
second_plate_width = 20.0
second_plate_thickness = 5.0

# Base plate
result = cq.Workplane("XY").box(base_length, base_width, base_thickness)

# Countersunk holes in triangular pattern
hole_positions = [
    (-10, 5),   # Top left
    (10, 5),    # Top right
    (0, -5)     # Bottom center
]

for pos in hole_positions:
    result = (
        result.faces(">Z")
        .workplane()
        .center(pos[0], pos[1])
        .cskHole(3.0, 6.0, 90.0)  # countersunk hole
    )

# Cylindrical component
result = (
    result.faces(">Z")
    .workplane(offset=cylinder_offset)
    .center(0, 0)
    .circle(cylinder_diameter/2)
    .extrude(cylinder_length)
    .faces(">Z")
    .workplane()
    .circle(cylinder_diameter/2 - 2)
    .cutBlind(-cylinder_length)
)

# Connecting arm (curved)
# Create a curved arm by making a solid and then cutting it
arm_start = cq.Workplane("XY").box(arm_thickness, 10, arm_thickness)
arm_end = cq.Workplane("XY").box(arm_thickness, 10, arm_thickness).translate((0, cylinder_length, 0))

# We'll create a smooth curved transition using a spline
arm_points = [
    (0, 0, 0),
    (0, cylinder_length/2, arm_curvature_radius),
    (0, cylinder_length, 0)
]

# Create the curved arm by making a profile and revolving it
arm_profile = cq.Workplane("XY").moveTo(0, 0).lineTo(arm_thickness, 0).lineTo(arm_thickness, 10).lineTo(0, 10).close()
arm_solid = arm_profile.extrude(cylinder_length)

# Connect arm to cylinder
result = result.union(arm_solid.translate((0, cylinder_length/2, base_thickness)))

# Second plate
result = (
    result.faces(">Z")
    .workplane(offset=arm_curvature_radius)
    .center(0, cylinder_length)
    .box(second_plate_length, second_plate_width, second_plate_thickness)
)

result = result.translate((0, 0, -base_thickness))