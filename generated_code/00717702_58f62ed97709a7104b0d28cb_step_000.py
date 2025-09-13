import cadquery as cq

# Define dimensions
spine_width = 10.0
spine_height = 50.0
spine_thickness = 5.0

base_width = 40.0
base_height = 30.0
base_thickness = 8.0

arm_width = 8.0
arm_height = 30.0
arm_thickness = 3.0

protrusion_width = 4.0
protrusion_height = 6.0
protrusion_thickness = 2.0

# Create the base plate (trapezoidal)
base = cq.Workplane("XY").rect(base_width, base_height).extrude(base_thickness)

# Create the central spine
spine = cq.Workplane("XY").translate((0, base_height/2 + spine_height/2, 0)).rect(spine_width, spine_height).extrude(spine_thickness)

# Combine base and spine
result = base.union(spine)

# Add the three arms at different heights
arm_y_positions = [-10.0, 0.0, 10.0]  # Three positions along the spine
for y_pos in arm_y_positions:
    arm = (
        cq.Workplane("XY")
        .translate((0, base_height/2 + spine_height/2 + y_pos, 0))
        .rect(arm_width, arm_height)
        .extrude(arm_thickness)
    )
    result = result.union(arm)

# Add small protrusions on the base plate
protrusion_y_positions = [-8.0, 0.0, 8.0]
for y_pos in protrusion_y_positions:
    protrusion = (
        cq.Workplane("XY")
        .translate((0, base_height/2 + y_pos, 0))
        .rect(protrusion_width, protrusion_height)
        .extrude(protrusion_thickness)
    )
    result = result.union(protrusion)

# Position the object properly
result = result.translate((0, -base_height/2, 0))