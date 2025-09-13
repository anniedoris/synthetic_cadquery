import cadquery as cq

# Define dimensions
vertical_width = 20.0
vertical_height = 40.0
horizontal_width = 40.0
horizontal_height = 20.0
thickness = 3.0
hole_diameter = 4.0
hole_distance_from_edge = 5.0

# Create the L-shaped bracket
result = (
    cq.Workplane("XY")
    # Create the vertical plate
    .rect(vertical_width, vertical_height)
    .extrude(thickness)
    # Create the horizontal plate
    .faces(">Y")
    .workplane()
    .rect(horizontal_width, horizontal_height)
    .extrude(thickness)
    # Add hole in vertical plate
    .faces("<Y")
    .workplane()
    .moveTo(0, hole_distance_from_edge - vertical_height/2)
    .circle(hole_diameter/2)
    .cutThruAll()
    # Add hole in horizontal plate
    .faces(">Z")
    .workplane()
    .moveTo(hole_distance_from_edge - horizontal_width/2, 0)
    .circle(hole_diameter/2)
    .cutThruAll()
)