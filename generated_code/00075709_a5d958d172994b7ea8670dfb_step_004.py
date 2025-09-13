import cadquery as cq

# Parameters
outer_diameter = 20.0
inner_diameter = 12.0
height = 20.0  # Height equals outer diameter
thickness = (outer_diameter - inner_diameter) / 2

# Create the base hollow cylinder
result = cq.Workplane("XY").circle(outer_diameter/2).circle(inner_diameter/2).extrude(height)

# Create a rectangular cutout to remove 90 degrees of the circumference
# The rectangle should be positioned to cut through the cylinder
cutout_width = outer_diameter
cutout_height = height

# Create a workplane at the center of the cylinder
result = (
    result.faces(">Z")
    .workplane()
    .rect(cutout_width, cutout_height, forConstruction=True)
    .vertices()
    .rect(10, 10)  # Small rectangle to define the cutout area
    .cutBlind(-cutout_width/2)  # Cut to remove 90 degrees
)

# Alternative approach - create a proper quarter-circle cut
# Create a rectangular cutout that spans the full height and covers 90 degrees
result = (
    cq.Workplane("XY")
    .circle(outer_diameter/2)
    .circle(inner_diameter/2)
    .extrude(height)
    .faces(">Z")
    .workplane()
    .rect(outer_diameter, height, forConstruction=True)
    .vertices("<XY")
    .rect(outer_diameter, height/2)
    .cutBlind(outer_diameter/2)
)

# Better approach - use a proper quarter-circle cut
# Create the main hollow cylinder
result = cq.Workplane("XY").circle(outer_diameter/2).circle(inner_diameter/2).extrude(height)

# Create a cutting tool - a rectangular prism that will remove 90 degrees of the cylinder
# Position it to cut through 90 degrees of the circumference
cutting_plane = cq.Workplane("YZ").rect(outer_diameter, height).extrude(outer_diameter/2)

# Rotate the cutting tool to position it correctly
result = result.cut(cutting_plane.rotate((0,0,0), (0,1,0), 45))

# Even better approach - create a proper cut with a polygon
# Create a wedge that removes 90 degrees
result = cq.Workplane("XY").circle(outer_diameter/2).circle(inner_diameter/2).extrude(height)

# Create a cutting wedge that removes 90 degrees
cut_wedge = (
    cq.Workplane("XY")
    .moveTo(outer_diameter/2, 0)
    .lineTo(outer_diameter/2, height/2)
    .lineTo(-outer_diameter/2, height/2)
    .lineTo(-outer_diameter/2, 0)
    .close()
    .extrude(outer_diameter)
    .rotate((0,0,0), (0,1,0), 45)
)

result = result.cut(cut_wedge)

# Final approach - simpler and more robust
# Create the main solid
result = cq.Workplane("XY").circle(outer_diameter/2).circle(inner_diameter/2).extrude(height)

# Create a rectangular cutout that removes 90 degrees of the cylinder
# This creates a flat edge along the opening
cut_rect = cq.Workplane("YZ").rect(outer_diameter, height).extrude(outer_diameter/2)
result = result.cut(cut_rect.rotate((0,0,0), (0,1,0), 45))

# Even more precise approach - use a proper wedge shape
# Create base cylinder with hole
result = cq.Workplane("XY").circle(outer_diameter/2).circle(inner_diameter/2).extrude(height)

# Create the opening by cutting a wedge
# We'll create a rectangular section and rotate it
opening = (
    cq.Workplane("XY")
    .rect(outer_diameter, height/2)  # Rectangle covering half the height
    .extrude(outer_diameter/2)       # Extrude to full width
    .rotate((0,0,0), (0,1,0), 45)    # Rotate to position the opening
)

result = result.cut(opening)

# Apply fillets to the corners of the opening
result = result.edges("|Z").fillet(1.0)

# Actually, let me do this more carefully
result = cq.Workplane("XY").circle(outer_diameter/2).circle(inner_diameter/2).extrude(height)

# Create a rectangular section that cuts out 90 degrees
# The rectangle should extend 90 degrees around the circumference
cut_section = (
    cq.Workplane("XY")
    .rect(outer_diameter, height/2)
    .extrude(outer_diameter)
    .rotate((0,0,0), (0,1,0), 45)
)

result = result.cut(cut_section)

# Apply fillets to the edges
result = result.edges("|Z").fillet(1.0)