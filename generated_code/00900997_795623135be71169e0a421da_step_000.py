import cadquery as cq
from math import sin, cos, pi

# Parameters for the component
arm_length = 100.0
arm_width = 10.0
arm_thickness = 3.0
plate_width = 50.0
plate_height = 30.0
plate_thickness = 5.0
hole_spacing = 15.0
hole_diameter = 3.0
mounting_hole_diameter = 5.0
threaded_hole_diameter = 6.0
threaded_hole_depth = 8.0

# Create the mounting plate
plate = cq.Workplane("XY").box(plate_width, plate_height, plate_thickness)

# Add holes to the mounting plate
# Center holes for mounting
plate = (
    plate.faces(">Z")
    .workplane()
    .center(-plate_width/2 + 10, -plate_height/2 + 10)
    .circle(mounting_hole_diameter/2)
    .cutThruAll()
    .center(plate_width - 20, 0)
    .circle(mounting_hole_diameter/2)
    .cutThruAll()
    .center(-plate_width + 20, plate_height - 20)
    .circle(mounting_hole_diameter/2)
    .cutThruAll()
    .center(0, -plate_height + 20)
    .circle(mounting_hole_diameter/2)
    .cutThruAll()
)

# Add threaded hole
plate = (
    plate.faces(">Z")
    .workplane()
    .center(plate_width/2 - 15, plate_height/2 - 15)
    .circle(threaded_hole_diameter/2)
    .cutBlind(-threaded_hole_depth)
)

# Create the curved arm
# Start with a base rectangle
arm_base = cq.Workplane("XY").box(arm_length, arm_width, arm_thickness)

# Create the curved profile using a spline
# Points for the curved arm profile
points = [
    (0, 0),
    (arm_length/3, 0),
    (2*arm_length/3, arm_width/2),
    (arm_length, arm_width/2)
]

# Create the curved arm profile
arm_profile = cq.Workplane("XY").polyline(points).mirrorY()

# Extrude the arm
arm = arm_profile.extrude(arm_thickness)

# Move the arm to position it properly
arm = arm.translate((0, -arm_width/2, 0))

# Create the mounting plate with appropriate positioning
plate = plate.translate((0, 0, arm_thickness))

# Create the joint connection
# Create a bracket for reinforcement
bracket_width = 8.0
bracket_height = 15.0
bracket_thickness = 3.0

bracket = (
    cq.Workplane("XY")
    .box(bracket_width, bracket_height, bracket_thickness)
    .translate((0, -arm_width/2 - bracket_height/2, arm_thickness - bracket_thickness/2))
)

# Create holes in the arm for adjustment
num_holes = int(arm_length / hole_spacing) - 1
for i in range(num_holes):
    hole_x = (i + 1) * hole_spacing
    arm = (
        arm.faces(">Z")
        .workplane()
        .center(hole_x - arm_length/2, 0)
        .circle(hole_diameter/2)
        .cutThruAll()
    )

# Position the arm and plate properly
# Position the arm at an angle to the plate
arm = arm.rotate((0, 0, 0), (0, 0, 1), 30)

# Create the final assembly
result = plate.union(arm).union(bracket)