import cadquery as cq

# Define dimensions
large_diameter = 20.0
small_diameter = 12.0
large_length = 15.0
small_length = 25.0
bore_diameter = 8.0
fillet_radius = 2.0

# Create the stepped cylinder with central bore
result = (
    cq.Workplane("XY")
    # Create the larger diameter section
    .circle(large_diameter/2)
    .circle(bore_diameter/2)
    .extrude(large_length)
    # Create the smaller diameter section
    .faces(">Z")
    .workplane()
    .circle(small_diameter/2)
    .circle(bore_diameter/2)
    .extrude(small_length)
    # Add fillet at transition
    .faces("<Z").edges().fillet(fillet_radius)
)

# Ensure the final result is properly aligned
result = result.faces("<Z").workplane().circle(bore_diameter/2).cutThruAll()