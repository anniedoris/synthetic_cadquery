import cadquery as cq

# Define dimensions
main_length = 100.0
main_width = 20.0
main_height = 5.0

flange_width = 15.0
flange_height = 20.0

hole_diameter = 4.0
hole_offset = 7.5

# Create the main rectangular section
result = cq.Workplane("XY").box(main_length, main_width, main_height)

# Add the first flange on the left side
result = (
    result.faces("<X")
    .workplane(offset=-flange_width/2)
    .rect(flange_width, flange_height, forConstruction=True)
    .vertices()
    .hole(hole_diameter)
)

# Add the second flange on the right side
result = (
    result.faces(">X")
    .workplane(offset=flange_width/2)
    .rect(flange_width, flange_height, forConstruction=True)
    .vertices()
    .hole(hole_diameter)
)

# Ensure the holes are positioned correctly relative to the main section
result = (
    result.faces("<X")
    .workplane(offset=-flange_width/2)
    .center(0, -flange_height/2 + hole_offset)
    .hole(hole_diameter)
)

result = (
    result.faces(">X")
    .workplane(offset=flange_width/2)
    .center(0, -flange_height/2 + hole_offset)
    .hole(hole_diameter)
)