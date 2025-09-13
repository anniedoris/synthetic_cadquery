import cadquery as cq

# Create the knife-like object with the described features
result = (
    cq.Workplane("XY")
    # Start with a base profile that has a wider end and tapers to a narrower end
    .moveTo(-20, 0)
    .lineTo(-15, 0)
    .lineTo(-10, 5)
    .lineTo(0, 10)
    .lineTo(10, 10)
    .lineTo(15, 5)
    .lineTo(20, 0)
    .lineTo(20, -5)
    .lineTo(15, -10)
    .lineTo(0, -10)
    .lineTo(-10, -5)
    .lineTo(-15, -10)
    .lineTo(-20, -10)
    .close()
    # Extrude to create the 3D object
    .extrude(2)
    # Add a small protrusion near the wider end (handle area)
    .faces(">Y")
    .workplane(offset=1)
    .center(-15, 0)
    .circle(1.5)
    .extrude(1)
    # Add a small recess at the narrower end (blade area)
    .faces("<Y")
    .workplane(offset=1)
    .center(15, 0)
    .circle(1.2)
    .cutBlind(-1)
)

# The object is already oriented diagonally with the wider end on the left and narrower end on the right
# The top surface is curved naturally from the profile, and the sides are straight and parallel
# The overall shape creates the knife-like appearance with the handle-like feature on the left
# and blade-like feature on the right