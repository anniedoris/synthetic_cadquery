import cadquery as cq

# Define dimensions
handle_diameter = 10.0
handle_length = 100.0
joint_diameter = 8.0
joint_length = 15.0
head_width = 20.0
head_height = 15.0
head_thickness = 5.0

# Create the handle (cylinder)
result = cq.Workplane("XY").circle(handle_diameter/2).extrude(handle_length)

# Create the joint (smaller cylinder at the end)
result = (
    result.faces(">Z")
    .workplane()
    .circle(joint_diameter/2)
    .extrude(joint_length)
)

# Create the head (flat, slightly curved trapezoidal shape)
# We'll create a rectangle and then slightly curve it
result = (
    result.faces(">Z")
    .workplane(offset=joint_length)
    .rect(head_width, head_height)
    .extrude(head_thickness)
)

# Add some rounding to the corners for a more realistic look
result = result.edges("|Z").fillet(1.0)

# Add slight curvature to the head (making it slightly curved)
# We'll create a curved surface on the top of the head
result = (
    result.faces(">Z")
    .workplane(offset=head_thickness)
    .rect(head_width * 0.9, head_height * 0.9)
    .extrude(0.5)
)

# Make the head slightly tapered (trapezoidal shape)
result = (
    result.faces(">Z")
    .workplane(offset=head_thickness + 0.5)
    .rect(head_width * 0.8, head_height * 0.8)
    .extrude(0.5)
)

# Final filleting for smoother edges
result = result.edges("|Z").fillet(1.5)

# The final result is the complete tool assembly
# The tool consists of:
# 1. Main handle (cylinder)
# 2. Joint (smaller cylinder) 
# 3. Head (flat trapezoidal shape)
result = result