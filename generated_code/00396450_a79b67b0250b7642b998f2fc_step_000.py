import cadquery as cq

# Define dimensions
outer_diameter = 50.0
inner_diameter = 20.0
thickness = 10.0
bolt_hole_diameter = 4.0
bolt_circle_diameter = 35.0

# Create the flange
result = (
    cq.Workplane("XY")
    .circle(outer_diameter / 2.0)
    .circle(inner_diameter / 2.0)
    .extrude(thickness)
    .faces(">Z")
    .workplane()
    .rect(bolt_circle_diameter, bolt_circle_diameter, forConstruction=True)
    .vertices()
    .circle(bolt_hole_diameter / 2.0)
    .cutThruAll()
)