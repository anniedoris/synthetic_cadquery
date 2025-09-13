import cadquery as cq

# Parameters for the component
panel_width = 50.0
panel_length = 100.0
panel_thickness = 5.0
hub_diameter = 30.0
hub_hollow_diameter = 15.0
connector_width = 10.0
connector_length = 20.0
connector_thickness = 5.0
hole_diameter = 3.0
hole_spacing = 15.0
hole_rows = 4
hole_columns = 6

# Create the first rectangular panel
panel1 = cq.Workplane("XY").box(panel_width, panel_length, panel_thickness)

# Create the second rectangular panel (rotated 90 degrees)
panel2 = cq.Workplane("YZ").box(panel_width, panel_length, panel_thickness).rotate((0,0,0), (0,1,0), 90)

# Create the central hub
hub = cq.Workplane("XY").circle(hub_diameter/2).extrude(panel_thickness)
hub = hub.faces(">Z").workplane().circle(hub_hollow_diameter/2).cutThruAll()

# Position the hub between the panels
hub = hub.translate((0, 0, panel_thickness/2))

# Create holes in the panels
# First panel holes
panel1_holes = panel1.faces(">Z").workplane().rect(panel_width - hole_spacing, panel_length - hole_spacing, forConstruction=True).vertices().circle(hole_diameter/2).cutThruAll()

# Second panel holes  
panel2_holes = panel2.faces(">Z").workplane().rect(panel_width - hole_spacing, panel_length - hole_spacing, forConstruction=True).vertices().circle(hole_diameter/2).cutThruAll()

# Create connectors
connector1 = cq.Workplane("XY").box(connector_width, connector_length, connector_thickness).translate((0, panel_length/2 + connector_length/2, 0))
connector2 = cq.Workplane("XY").box(connector_width, connector_length, connector_thickness).translate((0, -panel_length/2 - connector_length/2, 0))

# Add holes to connectors
connector1_holes = connector1.faces(">Z").workplane().rect(connector_width - hole_spacing, connector_length - hole_spacing, forConstruction=True).vertices().circle(hole_diameter/2).cutThruAll()
connector2_holes = connector2.faces(">Z").workplane().rect(connector_width - hole_spacing, connector_length - hole_spacing, forConstruction=True).vertices().circle(hole_diameter/2).cutThruAll()

# Combine all parts
result = panel1_holes.union(panel2_holes).union(hub).union(connector1_holes).union(connector2_holes)