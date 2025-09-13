import cadquery as cq

# Define dimensions
length = 40.0
width = 20.0
height = 10.0
indentation_diameter = 12.0
inner_circle_diameter = 6.0

# Create the main rectangular block
result = cq.Workplane("XY").box(length, width, height)

# Create the circular indentation on the top surface
result = (
    result.faces(">Z")
    .workplane()
    .circle(indentation_diameter / 2.0)
    .cutThruAll()
)

# Create the smaller red circular feature inside the indentation
result = (
    result.faces(">Z")
    .workplane()
    .center(0, 0)
    .circle(inner_circle_diameter / 2.0)
    .extrude(-2.0)  # Extrude slightly into the indentation to create the feature
)

# The red circle is represented by the extruded feature above
# For a more realistic representation, we could also create a separate solid
# but in CadQuery, the visual representation depends on the rendering environment
# The above creates the geometric feature that would be visually distinct

# Add a slight tilt to match the perspective described
# This is achieved by rotating the object around the X-axis
result = result.rotate((0, 0, 0), (1, 0, 0), 10)