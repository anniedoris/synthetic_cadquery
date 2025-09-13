import cadquery as cq

# Define dimensions
main_length = 100.0
main_width = 20.0
main_height = 10.0

end_plate_length = 20.0
end_plate_width = 10.0
end_plate_thickness = 10.0

hole_diameter = 3.0
hole_spacing = 8.0

# Create the main body
result = cq.Workplane("XY").box(main_length, main_width, main_height)

# Create left end plate
result = (
    result.faces("<X")
    .workplane(offset=main_height/2)
    .rect(end_plate_length, end_plate_width)
    .extrude(end_plate_thickness)
    .faces("<Z")
    .workplane()
    .center(-hole_spacing/2, 0)
    .circle(hole_diameter/2)
    .center(hole_spacing, 0)
    .circle(hole_diameter/2)
    .cutThruAll()
)

# Create right end plate
result = (
    result.faces(">X")
    .workplane(offset=main_height/2)
    .rect(end_plate_length, end_plate_width)
    .extrude(end_plate_thickness)
    .faces("<Z")
    .workplane()
    .center(-hole_spacing/2, 0)
    .circle(hole_diameter/2)
    .center(hole_spacing, 0)
    .circle(hole_diameter/2)
    .cutThruAll()
)

# Add fillets to edges for better appearance
result = result.edges("|Z").fillet(1.0)