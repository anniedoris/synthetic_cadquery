import cadquery as cq
from math import pi, cos, sin

# Define dimensions
segment_length = 50.0
segment_diameter = 8.0
joint_diameter = 6.0
joint_length = 12.0
end_protrusion_diameter = 10.0
end_protrusion_length = 15.0
hole_diameter = 2.0
hole_spacing = 15.0

# Create the main body with three curved segments
# Segment 1: Top-left to middle
segment1 = cq.Workplane("XY").circle(segment_diameter/2).extrude(segment_length/3)

# Create a curved path for the segments
# We'll create a 30-degree bend between segments
path_points = [
    (0, 0, 0),
    (segment_length/3 * cos(pi/6), segment_length/3 * sin(pi/6), 0),
    (segment_length/3 * cos(pi/6) + segment_length/3 * cos(pi/6), 
     segment_length/3 * sin(pi/6) + segment_length/3 * sin(pi/6), 0),
    (segment_length/3 * cos(pi/6) + segment_length/3 * cos(pi/6) + segment_length/3 * cos(pi/6),
     segment_length/3 * sin(pi/6) + segment_length/3 * sin(pi/6) + segment_length/3 * sin(pi/6), 0)
]

# Create a curved path for the segments
# For simplicity, we'll create segments manually and add joints
result = cq.Workplane("XY").circle(segment_diameter/2).extrude(segment_length/3)

# Move to second segment position with a 30-degree bend
result = result.translate((segment_length/3 * cos(pi/6), segment_length/3 * sin(pi/6), 0))

# Second segment
result = result.circle(segment_diameter/2).extrude(segment_length/3)

# Move to third segment position
result = result.translate((segment_length/3 * cos(pi/6), segment_length/3 * sin(pi/6), 0))

# Third segment
result = result.circle(segment_diameter/2).extrude(segment_length/3)

# Add the first joint
joint1_pos = (segment_length/3 * cos(pi/6), segment_length/3 * sin(pi/6), 0)
result = result.faces(">Z").workplane(offset=segment_length/3).circle(joint_diameter/2).extrude(joint_length)

# Add the second joint
joint2_pos = (segment_length/3 * cos(pi/6) + segment_length/3 * cos(pi/6), 
              segment_length/3 * sin(pi/6) + segment_length/3 * sin(pi/6), 0)
result = result.faces(">Z").workplane(offset=segment_length/3).circle(joint_diameter/2).extrude(joint_length)

# Add the top-left end protrusion
result = result.faces(">Z").workplane(offset=segment_length).circle(end_protrusion_diameter/2).extrude(end_protrusion_length)

# Add the bottom-right end structure
result = result.faces("<Z").workplane(offset=-segment_length/3).circle(end_protrusion_diameter/2).extrude(end_protrusion_length/2)

# Add the smaller protrusion on bottom-right
result = result.faces("<Z").workplane(offset=-segment_length/3 - end_protrusion_length/2).circle(end_protrusion_diameter/4).extrude(end_protrusion_length/3)

# Add holes along segments
# Hole on first segment
result = result.faces(">Z").workplane(offset=segment_length/6).circle(hole_diameter/2).cutThruAll()

# Hole on second segment
result = result.faces(">Z").workplane(offset=segment_length/2).circle(hole_diameter/2).cutThruAll()

# Hole on third segment
result = result.faces(">Z").workplane(offset=5*segment_length/6).circle(hole_diameter/2).cutThruAll()

# Add additional holes in the joints
# Hole in first joint
result = result.faces(">Z").workplane(offset=segment_length/3 + joint_length/2).circle(hole_diameter/2).cutThruAll()

# Hole in second joint
result = result.faces(">Z").workplane(offset=2*segment_length/3 + joint_length/2).circle(hole_diameter/2).cutThruAll()

# Add more holes for fasteners along the segments
# First segment holes
result = result.faces(">Z").workplane(offset=segment_length/6).pushPoints([(0, 0), (0, hole_spacing/2), (0, -hole_spacing/2)]).circle(hole_diameter/2).cutThruAll()

# Second segment holes
result = result.faces(">Z").workplane(offset=segment_length/2).pushPoints([(0, 0), (0, hole_spacing/2), (0, -hole_spacing/2)]).circle(hole_diameter/2).cutThruAll()

# Third segment holes
result = result.faces(">Z").workplane(offset=5*segment_length/6).pushPoints([(0, 0), (0, hole_spacing/2), (0, -hole_spacing/2)]).circle(hole_diameter/2).cutThruAll()

# Create a more realistic 3D model with proper curves
result = cq.Workplane("XY")

# Main curved structure
# Create three segments connected with curved joints
segment1 = cq.Workplane("XY").circle(segment_diameter/2).extrude(segment_length/3)
segment1 = segment1.translate((0, 0, 0))

segment2 = cq.Workplane("XY").circle(segment_diameter/2).extrude(segment_length/3)
segment2 = segment2.translate((segment_length/3 * cos(pi/6), segment_length/3 * sin(pi/6), 0))

segment3 = cq.Workplane("XY").circle(segment_diameter/2).extrude(segment_length/3)
segment3 = segment3.translate((segment_length/3 * cos(pi/6) + segment_length/3 * cos(pi/6), 
                               segment_length/3 * sin(pi/6) + segment_length/3 * sin(pi/6), 0))

# Join segments
result = segment1.union(segment2).union(segment3)

# Add the joints
joint1 = cq.Workplane("XY").circle(joint_diameter/2).extrude(joint_length)
joint1 = joint1.translate((segment_length/3 * cos(pi/6), segment_length/3 * sin(pi/6), 0))

joint2 = cq.Workplane("XY").circle(joint_diameter/2).extrude(joint_length)
joint2 = joint2.translate((segment_length/3 * cos(pi/6) + segment_length/3 * cos(pi/6), 
                           segment_length/3 * sin(pi/6) + segment_length/3 * sin(pi/6), 0))

result = result.union(joint1).union(joint2)

# Add end features
# Top-left end protrusion
top_protrusion = cq.Workplane("XY").circle(end_protrusion_diameter/2).extrude(end_protrusion_length)
top_protrusion = top_protrusion.translate((0, 0, segment_length))

# Bottom-right end structure
bottom_structure = cq.Workplane("XY").circle(end_protrusion_diameter/2).extrude(end_protrusion_length/2)
bottom_structure = bottom_structure.translate((segment_length/3 * cos(pi/6) + segment_length/3 * cos(pi/6), 
                                               segment_length/3 * sin(pi/6) + segment_length/3 * sin(pi/6), 
                                               -end_protrusion_length/2))

# Add small protrusion
small_protrusion = cq.Workplane("XY").circle(end_protrusion_diameter/4).extrude(end_protrusion_length/3)
small_protrusion = small_protrusion.translate((segment_length/3 * cos(pi/6) + segment_length/3 * cos(pi/6), 
                                              segment_length/3 * sin(pi/6) + segment_length/3 * sin(pi/6), 
                                              -end_protrusion_length/2 - end_protrusion_length/3))

result = result.union(top_protrusion).union(bottom_structure).union(small_protrusion)

# Add holes
# Holes on segments
for i in range(3):
    hole_y = (i - 1) * hole_spacing
    result = result.faces(">Z").workplane(offset=segment_length/3 + i * segment_length/3).circle(hole_diameter/2).cutThruAll()

# Holes on joints
result = result.faces(">Z").workplane(offset=segment_length/3 + joint_length/2).circle(hole_diameter/2).cutThruAll()
result = result.faces(">Z").workplane(offset=2*segment_length/3 + joint_length/2).circle(hole_diameter/2).cutThruAll()

# Add hole pattern for fasteners on the main segments
for i in range(3):
    for j in range(3):
        if i != 1 or j != 1:  # Skip center hole
            hole_x = (j - 1) * hole_spacing/2
            hole_y = (i - 1) * hole_spacing/2
            result = result.faces(">Z").workplane(offset=segment_length/3 + i * segment_length/3).move(hole_x, hole_y).circle(hole_diameter/2).cutThruAll()

# Create the final result
result = result