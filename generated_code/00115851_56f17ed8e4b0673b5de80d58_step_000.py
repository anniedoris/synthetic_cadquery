import cadquery as cq

# Base plate dimensions
base_length = 100.0
base_width = 60.0
base_thickness = 5.0
base_radius = 5.0  # Rounded edges radius

# Central shaft and hub dimensions
shaft_diameter = 10.0
hub_diameter = 20.0
hub_height = 15.0

# Ring dimensions
ring_inner_diameter = 60.0
ring_outer_diameter = 80.0
ring_thickness = 10.0

# Support beam dimensions
beam_width = 8.0
beam_height = 30.0
beam_depth = 10.0

# Create base plate with rounded edges and mounting holes
base = (
    cq.Workplane("XY")
    .rect(base_length, base_width)
    .extrude(base_thickness)
    .edges("|Z")
    .fillet(base_radius)
)

# Add mounting holes at each corner
hole_offset_x = (base_length - 20) / 2
hole_offset_y = (base_width - 20) / 2
base = (
    base.faces(">Z")
    .workplane()
    .pushPoints([
        (hole_offset_x, hole_offset_y),
        (-hole_offset_x, hole_offset_y),
        (-hole_offset_x, -hole_offset_y),
        (hole_offset_x, -hole_offset_y)
    ])
    .hole(4.0)
)

# Create central shaft and hub
shaft = (
    cq.Workplane("XY", origin=(0, 0, base_thickness))
    .circle(shaft_diameter / 2)
    .extrude(hub_height)
)

hub = (
    cq.Workplane("XY", origin=(0, 0, base_thickness + hub_height))
    .circle(hub_diameter / 2)
    .extrude(5.0)
)

# Combine shaft and hub
shaft_hub = shaft.union(hub)

# Create the large circular ring
ring = (
    cq.Workplane("XY", origin=(0, 0, base_thickness + hub_height + 5.0))
    .circle(ring_inner_diameter / 2)
    .circle(ring_outer_diameter / 2)
    .extrude(ring_thickness)
)

# Create support beams
beam1 = (
    cq.Workplane("XY", origin=(-base_length/2 + 10, 0, base_thickness))
    .rect(beam_width, beam_height)
    .extrude(beam_depth)
)

beam2 = (
    cq.Workplane("XY", origin=(base_length/2 - 10, 0, base_thickness))
    .rect(beam_width, beam_height)
    .extrude(beam_depth)
)

# Add smaller cylindrical component near base (bearing)
bearing = (
    cq.Workplane("XY", origin=(0, 0, base_thickness + 5.0))
    .circle(8.0)
    .extrude(3.0)
)

# Add arm extending from the side
arm_length = 20.0
arm_width = 4.0
arm_thickness = 2.0
arm = (
    cq.Workplane("XY", origin=(base_length/2 - 10, 0, base_thickness + 30))
    .rect(arm_length, arm_width)
    .extrude(arm_thickness)
)

# Combine all parts
result = base.union(shaft_hub).union(ring).union(beam1).union(beam2).union(bearing).union(arm)

# Make sure all components are properly positioned
result = result.translate((0, 0, 0))