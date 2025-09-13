import cadquery as cq

# Define dimensions
outer_diameter = 20.0
inner_diameter = 8.0
height = 4.0
recess_diameter = 12.0
recess_depth = 0.5

# Create the cylindrical base
result = cq.Workplane("XY").circle(outer_diameter / 2.0).extrude(height)

# Create the central hole
result = result.faces(">Z").workplane().circle(inner_diameter / 2.0).cutThruAll()

# Create the recessed feature on the top face
result = result.faces(">Z").workplane().circle(recess_diameter / 2.0).cutBlind(recess_depth)