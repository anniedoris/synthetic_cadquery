import cadquery as cq
from math import pi

# Dimensions
base_diameter = 20.0
top_diameter = 22.0
height = 15.0
base_height = 10.0
central_protrusion_diameter = 6.0
central_protrusion_height = 3.0
groove_diameter = 10.0
groove_depth = 0.5
cutout_width = 4.0
cutout_height = 6.0
cutout_offset = 2.0

# Create the base cylinder
result = cq.Workplane("XY").cylinder(height, base_diameter/2)

# Create the concave top surface
# We'll create a smaller cylinder and subtract it to make the concave shape
top_cylinder = cq.Workplane("XY").cylinder(base_height, top_diameter/2)
top_cylinder = top_cylinder.translate((0, 0, height - base_height))

# Subtract to create concavity
result = result.cut(top_cylinder)

# Add the central protrusion
central_protrusion = cq.Workplane("XY").cylinder(central_protrusion_height, central_protrusion_diameter/2)
central_protrusion = central_protrusion.translate((0, 0, height - central_protrusion_height))

# Add the concentric grooves
groove = cq.Workplane("XY").cylinder(groove_depth, groove_diameter/2)
groove = groove.translate((0, 0, height - groove_depth))

# Subtract groove to create the groove
result = result.cut(groove)

# Add the side cutout
cutout = cq.Workplane("XY").rect(cutout_width, cutout_height).extrude(cutout_offset)
cutout = cutout.translate((0, -base_diameter/2 + cutout_width/2, cutout_offset/2))

# Subtract cutout
result = result.cut(cutout)

# Add the central protrusion to the final result
result = result.union(central_protrusion)

# Make the final result more precise by using a proper approach with lofting
# Create base cylinder
base_cylinder = cq.Workplane("XY").cylinder(base_height, base_diameter/2)

# Create top surface with concavity
# We'll make a more accurate top surface using a second cylinder with a smaller radius
top_surface = cq.Workplane("XY").cylinder(base_height, top_diameter/2)

# Create central protrusion
central = cq.Workplane("XY").cylinder(central_protrusion_height, central_protrusion_diameter/2)
central = central.translate((0, 0, base_height))

# Create the groove
groove_cylinder = cq.Workplane("XY").cylinder(groove_depth, groove_diameter/2)
groove_cylinder = groove_cylinder.translate((0, 0, base_height - groove_depth))

# Create cutout
cutout = cq.Workplane("XY").rect(cutout_width, cutout_height).extrude(cutout_offset)
cutout = cutout.translate((0, -base_diameter/2 + cutout_width/2, 0))

# Combine all features
result = base_cylinder.union(top_surface).cut(groove_cylinder).union(central).cut(cutout)

# Since the description mentioned a more complex concave shape, let's create a more accurate version
# Start with a basic cylindrical shape
result = cq.Workplane("XY").cylinder(base_height, base_diameter/2)

# Add the top part with a different approach
# Create a workplane at the top
top_wp = cq.Workplane("XY").center(0, 0).moveTo(0, top_diameter/2).circle(top_diameter/2).extrude(base_height)

# Subtract to create the concave effect
concave_cylinder = cq.Workplane("XY").cylinder(base_height, top_diameter/2 - 0.5)
concave_cylinder = concave_cylinder.translate((0, 0, base_height/2))

# Create the final shape
result = cq.Workplane("XY").cylinder(base_height, base_diameter/2)
result = result.faces(">Z").workplane().circle(top_diameter/2).extrude(base_height/2)
result = result.faces(">Z").workplane().circle(top_diameter/2 - 0.5).cutBlind(-base_height/2)

# Add the central protrusion
central = cq.Workplane("XY").cylinder(central_protrusion_height, central_protrusion_diameter/2)
central = central.translate((0, 0, base_height))

# Add the groove
groove = cq.Workplane("XY").circle(groove_diameter/2).extrude(groove_depth)
groove = groove.translate((0, 0, base_height - groove_depth))

# Create cutout
cutout = cq.Workplane("XY").rect(cutout_width, cutout_height).extrude(cutout_offset)
cutout = cutout.translate((0, -base_diameter/2 + cutout_width/2, 0))

# Combine everything
result = result.union(central).cut(groove).cut(cutout)

# Better approach with a more realistic shape
# Base cylinder
result = cq.Workplane("XY").cylinder(base_height, base_diameter/2)

# Top surface with concavity - use a loft operation
# Create the profile for the top surface
top_profile = cq.Workplane("XY").circle(top_diameter/2).circle(top_diameter/2 - 0.5).extrude(0.1)

# Add the central protrusion
central = cq.Workplane("XY").cylinder(central_protrusion_height, central_protrusion_diameter/2)
central = central.translate((0, 0, base_height))

# Add groove around central protrusion
groove = cq.Workplane("XY").circle(groove_diameter/2).circle(central_protrusion_diameter/2).extrude(groove_depth)
groove = groove.translate((0, 0, base_height - groove_depth))

# Create side cutout
cutout = cq.Workplane("XY").rect(cutout_width, cutout_height).extrude(cutout_offset)
cutout = cutout.translate((0, -base_diameter/2 + cutout_width/2, 0))

# Combine everything
result = result.union(central).cut(groove).cut(cutout)

# Final simplified approach - a clean implementation
result = cq.Workplane("XY").cylinder(base_height, base_diameter/2)

# Create top surface with concavity
top_cylinder = cq.Workplane("XY").cylinder(base_height/2, top_diameter/2)
top_cylinder = top_cylinder.translate((0, 0, base_height))

# Make a smaller cylinder to subtract for concavity
concave_cylinder = cq.Workplane("XY").cylinder(base_height/2, top_diameter/2 - 1)
concave_cylinder = concave_cylinder.translate((0, 0, base_height))

# Subtract to create the concave shape
result = result.union(top_cylinder).cut(concave_cylinder)

# Add central protrusion
central = cq.Workplane("XY").cylinder(central_protrusion_height, central_protrusion_diameter/2)
central = central.translate((0, 0, base_height))

# Add groove
groove = cq.Workplane("XY").circle(groove_diameter/2).circle(central_protrusion_diameter/2).extrude(groove_depth)
groove = groove.translate((0, 0, base_height - groove_depth))

# Add cutout
cutout = cq.Workplane("XY").rect(cutout_width, cutout_height).extrude(cutout_offset)
cutout = cutout.translate((0, -base_diameter/2 + cutout_width/2, 0))

# Combine everything
result = result.union(central).cut(groove).cut(cutout)