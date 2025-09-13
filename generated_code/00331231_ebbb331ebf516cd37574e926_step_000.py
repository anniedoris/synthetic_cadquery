import cadquery as cq
from math import sin, cos, pi

# Create the main cylinder with tilted orientation
# Base cylinder parameters
radius = 10.0
height = 30.0

# Create a cylinder and tilt it by rotating around X-axis
result = cq.Workplane("XY").circle(radius).extrude(height)

# Rotate the cylinder to create the tilted effect
result = result.rotate((0, 0, 0), (1, 0, 0), 30)

# Add concentric grooves/ridges
# Create several concentric circles at different radii to represent the ridges
groove_count = 6
groove_spacing = 3.0

# Create the grooves by cutting slots at different radii
for i in range(groove_count):
    groove_radius = radius - (i * groove_spacing)
    if groove_radius > 2:  # Make sure we don't go too small
        # Create a slot that wraps around the cylinder
        # We'll create a rectangular slot at each groove position
        slot_width = 1.0
        slot_height = 0.5
        
        # Create workplane at the appropriate position along the cylinder
        result = (
            result.faces(">Z")
            .workplane(offset=-height/2 + i * groove_spacing)
            .circle(groove_radius)
            .rect(slot_width, slot_height, forConstruction=True)
            .vertices()
            .hole(slot_width/2)
        )

# Alternative approach: Create a more realistic helical groove pattern
# Create a helical pattern of ridges around the cylinder
# This approach uses a more complex method to create grooves that follow the surface

# Create a basic cylinder with some ridges using a more direct approach
cylinder = cq.Workplane("XY").circle(radius).extrude(height)
cylinder = cylinder.rotate((0, 0, 0), (1, 0, 0), 30)

# Add multiple circular cuts to simulate grooves
groove_radius = radius - 1.0
for i in range(8):
    offset = (i * 3.0) - 10.0  # Position the grooves along the length
    cylinder = (
        cylinder.faces(">Z")
        .workplane(offset=offset)
        .circle(groove_radius)
        .cutThruAll()
    )

# Add more subtle ridges for a better texture effect
for i in range(5):
    offset = (i * 6.0) - 12.0  # Position the grooves along the length
    cylinder = (
        cylinder.faces(">Z")
        .workplane(offset=offset)
        .circle(radius - 2.0)
        .cutThruAll()
    )

# For a more realistic approach, let's create a cylinder with helical ridges
# Create the base cylinder
base_cylinder = cq.Workplane("XY").circle(radius).extrude(height)

# Rotate to get the tilted effect
result = base_cylinder.rotate((0, 0, 0), (1, 0, 0), 30)

# Add some concentric ridges as described in the requirements
# We'll create multiple circles with increasing radii
for i in range(5):
    ridge_radius = radius - 1.5 - (i * 1.0)
    if ridge_radius > 1:
        result = (
            result.faces(">Z")
            .workplane(offset=-height/2 + (i * 6))
            .circle(ridge_radius)
            .cutThruAll()
        )

# Create a cleaner version with the main requirements
# Create a tilted cylinder
cylinder = cq.Workplane("XY").circle(radius).extrude(height)
cylinder = cylinder.rotate((0, 0, 0), (1, 0, 0), 30)

# Add the concentric grooves/ridges
# These are essentially circular cuts at various heights
groove_positions = [-12, -6, 0, 6, 12]  # Positions along the cylinder length
for pos in groove_positions:
    cylinder = (
        cylinder.faces(">Z")
        .workplane(offset=pos)
        .circle(radius - 2.0)
        .cutThruAll()
    )

# Add some additional detail with parallel lines
# Create a cylinder with cylindrical grooves
result = cq.Workplane("XY").circle(radius).extrude(height)
result = result.rotate((0, 0, 0), (1, 0, 0), 30)

# Add concentric circular grooves
for i in range(5):
    groove_radius = radius - 1.5 - i * 1.0
    if groove_radius > 0.5:
        result = (
            result.faces(">Z")
            .workplane(offset=-height/2 + i * 6)
            .circle(groove_radius)
            .cutThruAll()
        )

# Final version with clearer concentric ridges
result = cq.Workplane("XY").circle(radius).extrude(height)
result = result.rotate((0, 0, 0), (1, 0, 0), 30)

# Add 5 evenly spaced concentric ridges that follow the cylindrical surface
num_ridges = 5
ridge_spacing = height / (num_ridges + 1)

for i in range(num_ridges):
    # Position each ridge along the height of the cylinder
    z_offset = -height/2 + (i + 1) * ridge_spacing
    # Create a circular cut at each position
    result = (
        result.faces(">Z")
        .workplane(offset=z_offset)
        .circle(radius - 2.0)
        .cutThruAll()
    )

# Add a few more detail ridges for better visual representation
for i in range(3):
    z_offset = -height/2 + 3 + i * 10
    result = (
        result.faces(">Z")
        .workplane(offset=z_offset)
        .circle(radius - 3.0)
        .cutThruAll()
    )