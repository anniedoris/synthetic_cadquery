import cadquery as cq

# Define dimensions
base_length = 50.0
base_width = 30.0
top_length = 20.0
height = 10.0
hole_diameter = 6.0
notch_width = 4.0
notch_height = 3.0
notch_spacing = 8.0
notch_count = 3

# Create the base plate with triangular profile
result = (
    cq.Workplane("XY")
    .box(base_length, base_width, height)
    .faces(">Z")
    .workplane()
    .rect(top_length, base_width, forConstruction=True)
    .vertices()
    .hole(hole_diameter)
)

# Add notches to the base
for i in range(notch_count):
    x_pos = (base_length - (notch_count - 1) * notch_spacing) / 2 + i * notch_spacing
    result = (
        result.faces("<Z")
        .workplane(offset=height/2)
        .center(x_pos - top_length/2, 0)
        .rect(notch_width, notch_height, forConstruction=True)
        .vertices()
        .hole(2.0)
    )

# Add protrusions to the base
for i in range(notch_count):
    x_pos = (base_length - (notch_count - 1) * notch_spacing) / 2 + i * notch_spacing
    result = (
        result.faces("<Z")
        .workplane(offset=height/2)
        .center(x_pos - top_length/2, 0)
        .rect(notch_width, notch_height, forConstruction=True)
        .vertices()
        .hole(2.0)
    )

# Create a triangular cutout on the top surface
result = (
    result.faces(">Z")
    .workplane()
    .moveTo(-top_length/2, 0)
    .lineTo(top_length/2, 0)
    .lineTo(0, -base_width/2)
    .close()
    .cutThruAll()
)

# Add additional holes on the top surface
result = (
    result.faces(">Z")
    .workplane()
    .center(0, -base_width/4)
    .circle(2.0)
    .cutThruAll()
)

result = (
    result.faces(">Z")
    .workplane()
    .center(0, base_width/4)
    .circle(2.0)
    .cutThruAll()
)

# Add a central hole with counterbore
result = (
    result.faces("<Z")
    .workplane()
    .center(0, 0)
    .circle(hole_diameter/2)
    .extrude(height)
    .faces(">Z")
    .workplane()
    .circle(hole_diameter/2)
    .cutBlind(-height/2)
)