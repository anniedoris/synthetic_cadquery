import cadquery as cq
from math import pi, cos, sin

# Dimensions
top_diameter = 40.0
top_height = 10.0
base_diameter = 50.0
base_height = 8.0
rib_count = 6
rib_width = 2.0
rib_height = 4.0
tab_width = 8.0
tab_height = 6.0
tab_depth = 4.0
central_hole_diameter = 12.0
cutout_radius = 15.0

# Create the top circular section with hollow interior and ribs
top = cq.Workplane("XY").circle(top_diameter/2).extrude(top_height)
inner_cylinder = cq.Workplane("XY").circle((top_diameter - 2*rib_width)/2).extrude(top_height)
top = top.cut(inner_cylinder)

# Add radial ribs
for i in range(rib_count):
    angle = i * 2 * pi / rib_count
    rib_x = (top_diameter/2 - rib_width/2) * cos(angle)
    rib_y = (top_diameter/2 - rib_width/2) * sin(angle)
    rib = cq.Workplane("XY", origin=(rib_x, rib_y, 0)).rect(rib_width, rib_height, centered=True).extrude(top_height)
    top = top.union(rib)

# Create the hexagonal base
base = cq.Workplane("XY").polygon(6, base_diameter/2).extrude(base_height)

# Create tabs and cutouts
for i in range(6):
    angle = i * 2 * pi / 6
    tab_x = (base_diameter/2 - tab_depth) * cos(angle)
    tab_y = (base_diameter/2 - tab_depth) * sin(angle)
    
    # Create tab
    tab = cq.Workplane("XY", origin=(tab_x, tab_y, 0)).rect(tab_width, tab_height, centered=True).extrude(base_height)
    base = base.union(tab)
    
    # Create curved cutout between tabs
    cutout_x = (base_diameter/2 - cutout_radius) * cos(angle + pi/6)
    cutout_y = (base_diameter/2 - cutout_radius) * sin(angle + pi/6)
    cutout = cq.Workplane("XY", origin=(cutout_x, cutout_y, 0)).circle(cutout_radius).extrude(base_height)
    base = base.cut(cutout)

# Create central hole
central_hole = cq.Workplane("XY").circle(central_hole_diameter/2).extrude(base_height + top_height)
base = base.cut(central_hole)

# Position top section on base
result = base.union(top.translate((0, 0, base_height)))

# Ensure the top is properly aligned with the base
result = result.faces(">Z").workplane().circle(central_hole_diameter/2).cutThruAll()