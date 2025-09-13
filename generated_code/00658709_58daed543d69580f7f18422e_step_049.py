import cadquery as cq

# Parameters for the cylindrical sleeve
outer_diameter = 20.0
inner_diameter = 12.0
height = 25.0

# Create the outer cylinder
result = cq.Workplane("XY").circle(outer_diameter/2.0).extrude(height)

# Create the inner bore by subtracting a smaller cylinder
result = result.faces(">Z").workplane().circle(inner_diameter/2.0).cutBlind(height)