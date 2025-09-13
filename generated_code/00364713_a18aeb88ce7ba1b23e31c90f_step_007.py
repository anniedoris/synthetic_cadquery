import cadquery as cq

# Define dimensions
base_length = 40.0
base_width = 25.0
base_height = 5.0

arm_length = 30.0
arm_width = 8.0
arm_height = 5.0

# Hole diameters and positions
hole_diameter = 3.0
top_hole_offset_x = 5.0
top_hole_offset_y = 3.0
bottom_hole_offset_y = -3.0

# Create the base
result = cq.Workplane("XY").box(base_length, base_width, base_height)

# Add holes to the front face
result = (
    result.faces(">Z")
    .workplane()
    .center(-top_hole_offset_x, top_hole_offset_y)
    .circle(hole_diameter/2)
    .center(2*top_hole_offset_x, -2*top_hole_offset_y)
    .circle(hole_diameter/2)
    .center(0, -2*bottom_hole_offset_y)
    .circle(hole_diameter/2)
    .cutThruAll()
)

# Create the arm with recess
# First, create the arm as a separate piece
arm = cq.Workplane("XY").box(arm_length, arm_width, arm_height)

# Create the recess in the base for the arm
recess_depth = 2.0
recess_width = arm_width
recess_height = arm_height

# Add recess to base on the right side
result = (
    result.faces(">X")
    .workplane(offset=-recess_depth)
    .rect(recess_width, recess_height, forConstruction=True)
    .vertices()
    .hole(1.0)  # Small holes for alignment if needed
)

# Position the arm to connect with the base
# The arm should be positioned so that it fits into the recess
result = result.union(
    arm.translate((base_length/2 + arm_length/2, 0, 0))
)

# Add fillets to corners for aesthetics and stress reduction
result = result.edges("|Z").fillet(0.5)

# Since the arm is a separate piece, let's create a more integrated design
# by creating a single solid with both base and arm

# Start fresh with a single solid
result = cq.Workplane("XY").box(base_length, base_width, base_height)

# Add the arm as part of the same solid
# We'll create a rectangular prism for the arm and union it with the base
arm_offset_x = base_length/2
arm_offset_y = 0
arm_offset_z = 0

# Create the arm
arm = cq.Workplane("XY").box(arm_length, arm_width, arm_height).translate((arm_offset_x, arm_offset_y, arm_offset_z))

# Union the arm with the base
result = result.union(arm)

# Add holes to the front face of the base
result = (
    result.faces(">Z")
    .workplane()
    .center(-top_hole_offset_x, top_hole_offset_y)
    .circle(hole_diameter/2)
    .center(2*top_hole_offset_x, -2*top_hole_offset_y)
    .circle(hole_diameter/2)
    .center(0, -2*bottom_hole_offset_y)
    .circle(hole_diameter/2)
    .cutThruAll()
)

# Add fillets to the base edges
result = result.edges("|Z").fillet(0.5)