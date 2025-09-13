import cadquery as cq

# Define dimensions
outer_radius = 50.0
inner_radius = 20.0
hub_thickness = 10.0
spoke_width = 8.0
spoke_height = 30.0
spoke_thickness = 5.0
spoke_taper = 2.0  # amount by which spoke tapers from hub to outer ring

# Create the outer ring
outer_ring = cq.Workplane("XY").circle(outer_radius).extrude(hub_thickness)

# Create the central hub
hub = cq.Workplane("XY").circle(inner_radius).extrude(hub_thickness)

# Create one spoke with taper
spoke = (
    cq.Workplane("XY")
    .rect(spoke_width, spoke_height)
    .extrude(spoke_thickness)
    .faces(">Z")
    .workplane()
    .rect(spoke_width - spoke_taper, spoke_height)
    .extrude(spoke_thickness)
    .faces("<Z")
    .workplane()
    .rect(spoke_width, spoke_height)
    .extrude(spoke_thickness)
    .faces(">Z")
    .workplane()
    .rect(spoke_width - spoke_taper, spoke_height)
    .extrude(spoke_thickness)
    .faces("<Z")
    .workplane()
    .rect(spoke_width, spoke_height)
    .extrude(spoke_thickness)
)

# Position and rotate the spoke to create 4 evenly spaced spokes
spoke1 = spoke
spoke2 = spoke.rotate((0, 0, 0), (0, 0, 1), 90)
spoke3 = spoke.rotate((0, 0, 0), (0, 0, 1), 180)
spoke4 = spoke.rotate((0, 0, 0), (0, 0, 1), 270)

# Combine all parts
result = outer_ring.union(hub).union(spoke1).union(spoke2).union(spoke3).union(spoke4)

# Apply fillets to improve aesthetics
result = result.edges("|Z").fillet(2.0)