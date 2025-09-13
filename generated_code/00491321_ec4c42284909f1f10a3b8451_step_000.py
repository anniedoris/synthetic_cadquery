import cadquery as cq

# Define dimensions
hub_diameter = 20.0
hub_height = 5.0
arm_width = 3.0
arm_length = 15.0
plate_width = 25.0
plate_height = 8.0
plate_thickness = 2.0
hole_diameter = 2.0
hole_spacing = 5.0
small_cylinder_diameter = 4.0
small_cylinder_height = 8.0

# Create the central hub
result = cq.Workplane("XY").circle(hub_diameter/2).extrude(hub_height)

# Add concentric circles on top of the hub
result = (
    result.faces(">Z")
    .workplane()
    .circle(hub_diameter/2 - 2)
    .circle(hub_diameter/2 - 4)
    .circle(hub_diameter/2 - 6)
    .extrude(0.2)
)

# Create radial arms (3 arms positioned at 120-degree intervals)
num_arms = 3
for i in range(num_arms):
    angle = i * 360 / num_arms
    # Position the arm radially from the hub
    result = (
        result.workplane(offset=hub_height)
        .center(hub_diameter/2 * 0.8, 0)
        .transformed(rotate=cq.Vector(0, 0, angle))
        .rect(arm_width, arm_length, centered=True)
        .extrude(plate_thickness)
    )

# Create plates attached to arms
for i in range(num_arms):
    angle = i * 360 / num_arms
    # Position the plate on the end of each arm
    result = (
        result.workplane(offset=hub_height + plate_thickness)
        .center(hub_diameter/2 * 0.8, 0)
        .transformed(rotate=cq.Vector(0, 0, angle))
        .rect(plate_width, plate_height, centered=True)
        .extrude(plate_thickness)
    )

# Add holes to plates
for i in range(num_arms):
    angle = i * 360 / num_arms
    # Add holes along the edges of each plate
    result = (
        result.workplane(offset=hub_height + plate_thickness * 2)
        .center(hub_diameter/2 * 0.8, 0)
        .transformed(rotate=cq.Vector(0, 0, angle))
        .pushPoints([
            (-plate_width/2 + hole_spacing, 0),
            (plate_width/2 - hole_spacing, 0),
            (0, plate_height/2 - hole_spacing),
            (0, -plate_height/2 + hole_spacing)
        ])
        .circle(hole_diameter/2)
        .cutThruAll()
    )

# Add small cylinder component near the assembly
result = (
    result.workplane(offset=hub_height + plate_thickness * 2)
    .center(-hub_diameter/2 - 5, 0)
    .circle(small_cylinder_diameter/2)
    .extrude(small_cylinder_height)
)

result = result.translate((0, 0, -hub_height/2))