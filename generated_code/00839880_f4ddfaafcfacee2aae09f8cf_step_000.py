import cadquery as cq

# Define dimensions
length = 100.0
width = 80.0
height = 40.0

# Define hole parameters
hole_diameter = 8.0
hole_offset = 15.0

# Create the base rectangular prism
result = cq.Workplane("XY").box(length, width, height)

# Add holes to the top face
# Triangular pattern of holes on top face
top_face = result.faces(">Z")
top_face = top_face.workplane()

# Place three holes in triangular pattern
hole_positions = [
    (-length/2 + hole_offset, width/2 - hole_offset),  # Top-left
    (length/2 - hole_offset, width/2 - hole_offset),   # Top-right
    (0, -width/2 + hole_offset)                       # Bottom-center
]

top_face = top_face.pushPoints(hole_positions).hole(hole_diameter)

# Add holes to the left side face
left_face = result.faces("<X")
left_face = left_face.workplane()

# Three holes on left side face
left_hole_positions = [
    (-height/2 + hole_offset, width/2 - hole_offset),   # Top
    (-height/2 + hole_offset, -width/2 + hole_offset),  # Bottom
    (0, -width/2 + hole_offset)                        # Middle
]

left_face = left_face.pushPoints(left_hole_positions).hole(hole_diameter)

# Add holes to the front face
front_face = result.faces(">Y")
front_face = front_face.workplane()

# Two holes on front face
front_hole_positions = [
    (-height/2 + hole_offset, length/2 - hole_offset),   # Top
    (-height/2 + hole_offset, -length/2 + hole_offset)   # Bottom
]

front_face = front_face.pushPoints(front_hole_positions).hole(hole_diameter)

# Ensure we're working with the final solid
result = result.val()