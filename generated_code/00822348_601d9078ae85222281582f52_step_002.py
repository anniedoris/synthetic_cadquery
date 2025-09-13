import cadquery as cq
from math import sin, cos, pi

# Parameters for the threaded shaft with lobes
shaft_diameter = 20.0
shaft_length = 100.0
lobe_count = 3
lobe_radius = 4.0
lobe_height = 3.0
helix_pitch = 15.0
end_cap_diameter = 25.0
end_cap_thickness = 5.0
center_hole_diameter = 8.0

# Create the base shaft
result = cq.Workplane("XY").circle(shaft_diameter/2).extrude(shaft_length)

# Create a single lobe profile
lobe = (
    cq.Workplane("XY")
    .circle(lobe_radius)
    .workplane(offset=lobe_height)
    .circle(lobe_radius*0.7)
    .loft(combine=True)
)

# Create helical pattern of lobes
# First, we'll create a helix path for the lobes
helix_points = []
for i in range(100):
    angle = i * 2 * pi / 100
    z = i * helix_pitch / 100
    x = (shaft_diameter/2 + lobe_radius) * cos(angle)
    y = (shaft_diameter/2 + lobe_radius) * sin(angle)
    helix_points.append((x, y, z))

# Create a workplane for the lobes
lobe_workplane = cq.Workplane("XY").center(0, 0).workplane(offset=0)

# Create multiple lobes around the shaft
for i in range(lobe_count):
    angle = 2 * pi * i / lobe_count
    lobe_copy = lobe.translate((0, 0, 0))
    lobe_copy = lobe_copy.rotate((0, 0, 0), (0, 0, 1), angle * 180 / pi)
    result = result.union(lobe_copy)

# Add end caps
# Create the first end cap
end_cap1 = cq.Workplane("XY").circle(end_cap_diameter/2).extrude(end_cap_thickness)
result = result.union(end_cap1.translate((0, 0, shaft_length/2 + end_cap_thickness/2)))

# Create the second end cap with a central hole
end_cap2 = cq.Workplane("XY").circle(end_cap_diameter/2).extrude(end_cap_thickness)
center_hole = cq.Workplane("XY").circle(center_hole_diameter/2).extrude(end_cap_thickness)
end_cap2 = end_cap2.cut(center_hole)
result = result.union(end_cap2.translate((0, 0, -shaft_length/2 - end_cap_thickness/2)))

# Create the helical lobes using a more precise approach
# Create the main shaft with helical lobes
shaft = cq.Workplane("XY").circle(shaft_diameter/2).extrude(shaft_length)

# Create a single lobe
lobe_profile = cq.Workplane("XY").circle(lobe_radius).extrude(lobe_height)

# Rotate the lobe to create the helical pattern
lobe_pattern = []
for i in range(lobe_count):
    angle = 2 * pi * i / lobe_count
    lobe = lobe_profile.rotate((0, 0, 0), (0, 0, 1), angle * 180 / pi)
    lobe = lobe.translate((0, 0, 0))  # This will be modified to create the helical effect
    lobe_pattern.append(lobe)

# Create helical lobes using the correct approach
lobes = cq.Workplane("XY").circle(shaft_diameter/2).extrude(shaft_length)
for i in range(lobe_count):
    angle = 2 * pi * i / lobe_count
    # Create the lobe at the correct position
    lobe_pos = (shaft_diameter/2 + lobe_radius) * cos(angle), (shaft_diameter/2 + lobe_radius) * sin(angle)
    lobe = cq.Workplane("XY").center(lobe_pos[0], lobe_pos[1]).circle(lobe_radius).extrude(lobe_height)
    lobes = lobes.union(lobe)

# Create the final object with a helical pattern of lobes
# Create the main shaft
shaft = cq.Workplane("XY").circle(shaft_diameter/2).extrude(shaft_length)

# Create helical lobes using a more appropriate method
# Create a single lobe and rotate it to form the pattern
base_lobe = cq.Workplane("XY").circle(lobe_radius).extrude(lobe_height)

# Create multiple lobes arranged in a circular pattern
lobes = cq.Workplane("XY")
for i in range(lobe_count):
    angle = 2 * pi * i / lobe_count
    lobe_pos = (shaft_diameter/2 + lobe_radius) * cos(angle), (shaft_diameter/2 + lobe_radius) * sin(angle)
    lobe = cq.Workplane("XY").center(lobe_pos[0], lobe_pos[1]).circle(lobe_radius).extrude(lobe_height)
    lobes = lobes.union(lobe)

# Combine with the shaft
result = shaft.union(lobes)

# Add end caps
# First end cap
end_cap1 = cq.Workplane("XY").circle(end_cap_diameter/2).extrude(end_cap_thickness)
result = result.union(end_cap1.translate((0, 0, shaft_length/2 + end_cap_thickness/2)))

# Second end cap with central hole
end_cap2 = cq.Workplane("XY").circle(end_cap_diameter/2).extrude(end_cap_thickness)
center_hole = cq.Workplane("XY").circle(center_hole_diameter/2).extrude(end_cap_thickness)
end_cap2 = end_cap2.cut(center_hole)
result = result.union(end_cap2.translate((0, 0, -shaft_length/2 - end_cap_thickness/2)))

# Create the final model with helical lobes
# Create the shaft
shaft = cq.Workplane("XY").circle(shaft_diameter/2).extrude(shaft_length)

# Create helical lobes pattern
# We'll use a more direct approach to create the helical effect
helical_lobe = cq.Workplane("XY").circle(lobe_radius).extrude(lobe_height)
helical_lobe = helical_lobe.translate((0, 0, 0))

# Create multiple lobes in a circular pattern around the shaft
lobes_group = cq.Workplane("XY")
for i in range(lobe_count):
    angle = 2 * pi * i / lobe_count
    lobe_x = (shaft_diameter/2 + lobe_radius) * cos(angle)
    lobe_y = (shaft_diameter/2 + lobe_radius) * sin(angle)
    lobe = cq.Workplane("XY").center(lobe_x, lobe_y).circle(lobe_radius).extrude(lobe_height)
    lobes_group = lobes_group.union(lobe)

# Combine shaft and lobes
result = shaft.union(lobes_group)

# Add end caps
end_cap1 = cq.Workplane("XY").circle(end_cap_diameter/2).extrude(end_cap_thickness)
result = result.union(end_cap1.translate((0, 0, shaft_length/2 + end_cap_thickness/2)))

end_cap2 = cq.Workplane("XY").circle(end_cap_diameter/2).extrude(end_cap_thickness)
center_hole = cq.Workplane("XY").circle(center_hole_diameter/2).extrude(end_cap_thickness)
end_cap2 = end_cap2.cut(center_hole)
result = result.union(end_cap2.translate((0, 0, -shaft_length/2 - end_cap_thickness/2)))

# For a more realistic helical pattern, we'll use a different approach:
# Create a single lobe, then rotate it around the axis
result = cq.Workplane("XY").circle(shaft_diameter/2).extrude(shaft_length)

# Add the lobes using a radial pattern
for i in range(lobe_count):
    angle = 2 * pi * i / lobe_count
    # Position the lobe at the appropriate radial distance
    lobe_x = (shaft_diameter/2 + lobe_radius) * cos(angle)
    lobe_y = (shaft_diameter/2 + lobe_radius) * sin(angle)
    
    # Create a lobe at that position
    lobe = cq.Workplane("XY").center(lobe_x, lobe_y).circle(lobe_radius).extrude(lobe_height)
    result = result.union(lobe)

# Add end caps
# Add first end cap
first_end = cq.Workplane("XY").circle(end_cap_diameter/2).extrude(end_cap_thickness)
result = result.union(first_end.translate((0, 0, shaft_length/2 + end_cap_thickness/2)))

# Add second end cap with hole
second_end = cq.Workplane("XY").circle(end_cap_diameter/2).extrude(end_cap_thickness)
hole = cq.Workplane("XY").circle(center_hole_diameter/2).extrude(end_cap_thickness)
second_end = second_end.cut(hole)
result = result.union(second_end.translate((0, 0, -shaft_length/2 - end_cap_thickness/2)))