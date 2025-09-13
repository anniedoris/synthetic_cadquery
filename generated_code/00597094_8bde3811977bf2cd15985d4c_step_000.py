import cadquery as cq

# Define dimensions
block_width = 20.0
block_height = 20.0
block_thickness = 5.0
ring_outer_diameter = 12.0
ring_inner_diameter = 8.0
ring_thickness = 2.0

# Create the central block
block = cq.Workplane("XY").box(block_width, block_height, block_thickness)

# Create a circular ring profile
ring_profile = cq.Workplane("XY").circle(ring_outer_diameter/2).circle(ring_inner_diameter/2).extrude(ring_thickness)

# Position the rings at the corners of the central block
# Top-left ring
ring1 = ring_profile.translate((-block_width/2 + ring_outer_diameter/2, block_height/2 - ring_outer_diameter/2, 0))

# Top-right ring
ring2 = ring_profile.translate((block_width/2 - ring_outer_diameter/2, block_height/2 - ring_outer_diameter/2, 0))

# Bottom-left ring
ring3 = ring_profile.translate((-block_width/2 + ring_outer_diameter/2, -block_height/2 + ring_outer_diameter/2, 0))

# Bottom-right ring
ring4 = ring_profile.translate((block_width/2 - ring_outer_diameter/2, -block_height/2 + ring_outer_diameter/2, 0))

# Combine the block with the rings
result = block.union(ring1).union(ring2).union(ring3).union(ring4)

# Add a central hole through the block
result = result.faces(">Z").workplane().circle(4.0).cutThruAll()