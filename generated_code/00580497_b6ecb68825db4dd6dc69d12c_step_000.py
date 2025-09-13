import cadquery as cq

# Define dimensions
base_width = 40.0
base_depth = 20.0
base_height = 10.0

cylinder_diameter = 12.0
cylinder_height = 25.0

hole_diameter = 8.0
hole_depth = 8.0

slot_width = 6.0
slot_height = 15.0
slot_depth = 3.0

# Create the base
result = cq.Workplane("XY").box(base_width, base_depth, base_height)

# Add the cylindrical protrusion on the front edge, centered width-wise
# Position at front edge (depth/2 from center) and centered width-wise
result = (
    result.faces(">Y")  # Select front face
    .workplane(offset=base_height/2)  # Workplane on top of base
    .center(0, 0)  # Center on front face
    .circle(cylinder_diameter/2)  # Draw cylinder
    .extrude(cylinder_height)  # Extrude upward
)

# Add the circular hole on top of the cylinder
result = (
    result.faces(">Z")  # Select top face of cylinder
    .workplane()  # Workplane on top face
    .center(0, 0)  # Center on top face
    .circle(hole_diameter/2)  # Draw hole
    .cutBlind(-hole_depth)  # Cut hole downward
)

# Add the slot on the side near the front edge
# Position on the side of base, near front edge
result = (
    result.faces("<X")  # Select left face
    .workplane(offset=base_height/2)  # Workplane on middle height
    .center(0, 0)  # Center on left face
    .rect(slot_width, slot_height, forConstruction=True)  # Draw slot rectangle
    .vertices()  # Select vertices
    .hole(slot_depth)  # Cut slot
)

# Alternative approach for slot - create a rectangular cutout
# Create a workplane on the side face and make a rectangular cut
result = (
    result.faces("<X")  # Select left face
    .workplane(offset=base_height/2 - slot_height/2)  # Position vertically
    .center(0, 0)  # Center on face
    .rect(slot_width, slot_height)  # Rectangle for slot
    .cutBlind(slot_depth)  # Cut through the base
)

# The above approach might be better for a true slot - let me rewrite more precisely:
result = cq.Workplane("XY").box(base_width, base_depth, base_height)

# Add cylindrical protrusion
result = (
    result.faces(">Y")  # Front face
    .workplane(offset=base_height/2)
    .center(0, 0)  # Centered width-wise
    .circle(cylinder_diameter/2)
    .extrude(cylinder_height)
)

# Add hole on top of cylinder
result = (
    result.faces(">Z")
    .workplane()
    .center(0, 0)
    .circle(hole_diameter/2)
    .cutBlind(-hole_depth)
)

# Add slot on side
# Create slot in side face, near front edge
result = (
    result.faces("<X")  # Left face
    .workplane(offset=base_height/2)  # Middle height
    .center(0, 0)  # Centered on face
    .rect(slot_width, slot_height)  # Slot dimensions
    .cutBlind(slot_depth)  # Cut through base
)

# The slot might be better positioned - let me create a proper slot that goes through
# Create slot that extends through base depth and has proper width
result = cq.Workplane("XY").box(base_width, base_depth, base_height)

# Add cylindrical protrusion
result = (
    result.faces(">Y")  # Front face
    .workplane(offset=base_height/2)
    .center(0, 0)
    .circle(cylinder_diameter/2)
    .extrude(cylinder_height)
)

# Add hole on top of cylinder
result = (
    result.faces(">Z")
    .workplane()
    .center(0, 0)
    .circle(hole_diameter/2)
    .cutBlind(-hole_depth)
)

# Add slot on left side, near front edge
# Position slot in left face
result = (
    result.faces("<X")
    .workplane(offset=base_height/2)  # Middle height
    .center(0, 0)  # Centered on face
    .rect(slot_width, slot_height)  # Slot dimensions
    .cutBlind(-slot_depth)  # Cut through base
)