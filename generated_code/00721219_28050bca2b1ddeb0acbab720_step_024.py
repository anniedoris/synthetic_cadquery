import cadquery as cq

# Dimensions
outer_diameter = 20.0
inner_diameter = 12.0
height = 18.0  # Slightly less than outer diameter
chamfer_size = 1.0

# Create the outer cylinder
result = cq.Workplane("XY").circle(outer_diameter / 2.0).extrude(height)

# Create the inner cylindrical bore
result = result.faces("<Z").workplane().circle(inner_diameter / 2.0).cutThruAll()

# Add chamfer to the top face
result = result.faces(">Z").edges().chamfer(chamfer_size)

# Ensure the bottom face is flat (it should already be from the extrusion)
# The object is now ready with:
# - Outer cylindrical surface
# - Inner cylindrical bore
# - Flat top and bottom faces
# - Chamfer on the top face
# - Uniform wall thickness

# The part is a sleeve/bushing with:
# - Outer diameter: 20.0
# - Inner diameter: 12.0
# - Height: 18.0
# - Wall thickness: (20.0 - 12.0) / 2 = 4.0
# - Chamfer on top edge: 1.0