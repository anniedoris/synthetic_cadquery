import cadquery as cq
from math import sin, cos, pi

# Create the U-shaped cross-section profile
# This creates a U-shape with rounded top and straight sides
u_profile = (
    cq.Workplane("XY")
    .moveTo(-10, 0)  # Start at left side of bottom
    .lineTo(-10, -5)  # Vertical line down
    .lineTo(-5, -5)   # Horizontal line to bottom of U
    .threePointArc((-2, -3), (0, -5))  # Rounded top of U
    .lineTo(5, -5)    # Horizontal line to right side of bottom
    .lineTo(10, -5)   # Vertical line up
    .lineTo(10, 0)    # Horizontal line to right end
    .close()
)

# Create a smooth curved path for the extrusion
# This creates a path that goes down, curves around, then up
path_points = []
# Generate points for a smooth curve
for i in range(21):
    t = i / 20.0
    # Create a path that moves in a U-shape with some asymmetry
    x = 50 * sin(t * pi)  # X follows sine wave
    y = 20 * t - 10       # Y moves linearly
    z = 10 * sin(t * 2 * pi)  # Z creates some curvature
    
    # Add some asymmetry to make it not perfectly symmetrical
    if t > 0.5:
        z += 5 * (t - 0.5)
    
    path_points.append((x, y, z))

# Create the path curve
path = cq.Workplane("XY").polyline(path_points)

# Create the 3D object by sweeping the U-profile along the path
result = u_profile.sweep(path, multisection=True)

# Add flared entry and exit points for better guidance
# Create a larger opening at the start
result = (
    result.faces("<Y")
    .workplane()
    .rect(15, 10, forConstruction=True)
    .vertices()
    .hole(3)
)

# Create a larger opening at the end
result = (
    result.faces(">Y")
    .workplane()
    .rect(15, 10, forConstruction=True)
    .vertices()
    .hole(3)
)