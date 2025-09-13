import cadquery as cq

# Define dimensions
length = 100.0
width = 20.0
height = 10.0
taper_length = 15.0  # Length of the tapered section

# Create the main rectangular prism
result = cq.Workplane("XY").box(length, width, height)

# Create a beveled end by cutting a triangular section
# We'll create a workplane at the tapered end and cut a triangular prism
result = (
    result.faces(">Z")
    .workplane(offset=-taper_length)
    .pushPoints([(length - taper_length/2, 0)])
    .rect(taper_length, width, forConstruction=True)
    .vertices()
    .hole(1.0)  # This won't work as intended, let's rethink
)

# Better approach: create the tapered end manually
# Create the main body
result = cq.Workplane("XY").box(length, width, height)

# Create the beveled end using a polygon to define the taper
# We'll add a triangular face at one end to create the bevel
result = (
    result.faces(">Z")
    .workplane(offset=-taper_length)
    .moveTo(-taper_length/2, width/2)
    .lineTo(taper_length/2, width/2)
    .lineTo(taper_length/2, -width/2)
    .lineTo(-taper_length/2, -width/2)
    .close()
    .extrude(taper_length)
)

# Actually, let me reconsider. A simpler approach:
# Create a box and then cut a triangular prism to create the bevel
result = cq.Workplane("XY").box(length, width, height)

# Create a triangular prism to cut out the beveled end
bevel_block = (
    cq.Workplane("XY")
    .moveTo(0, width/2)
    .lineTo(taper_length, width/2)
    .lineTo(taper_length, -width/2)
    .lineTo(0, -width/2)
    .close()
    .extrude(height)
    .translate((length-taper_length, 0, 0))
)

# Cut the bevel from the main object
result = result.cut(bevel_block)