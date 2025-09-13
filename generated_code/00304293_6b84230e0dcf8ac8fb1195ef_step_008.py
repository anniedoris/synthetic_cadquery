import cadquery as cq

# Define dimensions
length = 100.0
width = 60.0
height = 20.0
thickness = 5.0

# Create the open-topped rectangular box
result = (
    cq.Workplane("XY")
    .box(length, width, thickness)  # Base
    .faces(">Z")
    .workplane()
    .rect(length, width, forConstruction=True)
    .vertices()
    .hole(thickness)  # Remove material to create the open top
    .faces(">Z")
    .workplane()
    .rect(length - 2*thickness, width - 2*thickness, forConstruction=True)
    .vertices()
    .hole(thickness)  # Remove material to create the open top
    .faces(">Z")
    .workplane()
    .rect(length - 2*thickness, width - 2*thickness, forConstruction=True)
    .vertices()
    .hole(thickness)  # Remove material to create the open top
    .faces(">Z")
    .workplane()
    .rect(length - 2*thickness, width - 2*thickness, forConstruction=True)
    .vertices()
    .hole(thickness)  # Remove material to create the open top
)

# Actually, let's create a proper open-topped box with sides
result = (
    cq.Workplane("XY")
    .box(length, width, thickness)  # Base
    .faces(">Z")
    .workplane()
    .rect(length, width, forConstruction=True)
    .vertices()
    .hole(thickness)  # Remove material to create the open top
    .faces(">Z")
    .workplane()
    .rect(length - 2*thickness, width - 2*thickness, forConstruction=True)
    .vertices()
    .hole(thickness)  # Remove material to create the open top
    .faces(">Z")
    .workplane()
    .rect(length - 2*thickness, width - 2*thickness, forConstruction=True)
    .vertices()
    .hole(thickness)  # Remove material to create the open top
    .faces(">Z")
    .workplane()
    .rect(length - 2*thickness, width - 2*thickness, forConstruction=True)
    .vertices()
    .hole(thickness)  # Remove material to create the open top
)

# Simpler approach - create the box and then cut the top
result = (
    cq.Workplane("XY")
    .box(length, width, height)  # Full box
    .faces(">Z")
    .workplane()
    .rect(length - 2*thickness, width - 2*thickness)
    .cutBlind(-thickness)  # Cut the top to create an open box
)

# Even simpler approach - create the base and sides separately
result = (
    cq.Workplane("XY")
    .box(length, width, thickness)  # Base
    .faces(">Z")
    .workplane()
    .rect(length, width, forConstruction=True)
    .vertices()
    .hole(thickness)  # Remove material to create the open top
)

# Let's do it properly - create a rectangular box with open top
result = (
    cq.Workplane("XY")
    .box(length, width, height)  # Full box
    .faces(">Z")
    .workplane()
    .rect(length - 2*thickness, width - 2*thickness)
    .cutBlind(-thickness)  # Cut the top to create an open box
)

# Or even simpler - create the sides as separate extrusions
base = cq.Workplane("XY").box(length, width, thickness)
# Create the four sides
side1 = cq.Workplane("XY").box(length, thickness, height).translate((0, width/2 - thickness/2, thickness/2 + height/2))
side2 = cq.Workplane("XY").box(length, thickness, height).translate((0, -width/2 + thickness/2, thickness/2 + height/2))
side3 = cq.Workplane("XY").box(thickness, width, height).translate((length/2 - thickness/2, 0, thickness/2 + height/2))
side4 = cq.Workplane("XY").box(thickness, width, height).translate((-length/2 + thickness/2, 0, thickness/2 + height/2))

result = base.union(side1).union(side2).union(side3).union(side4)