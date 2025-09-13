import cadquery as cq

# Dimensions
width = 50.0
height = 80.0
depth = 20.0
front_top_width = 60.0
front_bottom_width = 40.0
fin_height = 8.0
fin_width = 3.0
fin_spacing = 10.0
hole_diameter = 8.0
hole_offset = 20.0

# Create the base block with trapezoidal front face
result = cq.Workplane("XY").box(width, height, depth)

# Create the trapezoidal front face by cutting and reshaping
# First, create a workplane on the front face
front_face = result.faces(">Z").workplane()

# Create the trapezoidal profile for the front face
# This creates a trapezoid that's wider at the top
trapezoid_points = [
    (-front_top_width/2, height/2),
    (front_top_width/2, height/2),
    (front_bottom_width/2, -height/2),
    (-front_bottom_width/2, -height/2)
]

# Create the trapezoidal shape and cut it
trapezoid = (
    cq.Workplane("XY")
    .polyline(trapezoid_points)
    .close()
    .extrude(depth)
)

# Cut the trapezoid from the front face
result = result.cut(trapezoid)

# Add vertical fins to the side faces
# Create a single fin and duplicate it
fin = cq.Workplane("XY").box(fin_width, fin_height, depth)

# Add fins to the left side face
for i in range(int(height/fin_spacing)):
    y_pos = -height/2 + i * fin_spacing + fin_height/2
    if y_pos + fin_height/2 < height/2:
        result = (
            result.faces("<Y")
            .workplane(offset=-depth/2, centerOption="CenterOfBoundBox")
            .center(-width/2 + fin_width/2, y_pos)
            .union(fin)
        )

# Add fins to the right side face
for i in range(int(height/fin_spacing)):
    y_pos = -height/2 + i * fin_spacing + fin_height/2
    if y_pos + fin_height/2 < height/2:
        result = (
            result.faces(">Y")
            .workplane(offset=-depth/2, centerOption="CenterOfBoundBox")
            .center(width/2 - fin_width/2, y_pos)
            .union(fin)
        )

# Create the circular hole in the back face
result = (
    result.faces("<Z")
    .workplane(centerOption="CenterOfBoundBox")
    .center(0, -hole_offset)
    .circle(hole_diameter/2)
    .cutThruAll()
)

# Add chamfers to the top and bottom edges
# Chamfer the top edges of the front face
result = result.edges("|Z and >Y").chamfer(2.0)
result = result.edges("|Z and <Y").chamfer(2.0)

# Chamfer the bottom edges of the front face
result = result.edges("|Z and >X").chamfer(2.0)
result = result.edges("|Z and <X").chamfer(2.0)