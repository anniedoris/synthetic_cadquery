import cadquery as cq

# Define dimensions
bracket_width = 30.0
bracket_height = 20.0
bracket_thickness = 5.0
boss_diameter = 8.0
tube_diameter = 6.0
tube_length = 40.0
mounting_hole_diameter = 3.0
protrusion_width = 8.0
protrusion_height = 6.0
protrusion_depth = 3.0

# Create the mounting bracket
result = cq.Workplane("XY").box(bracket_width, bracket_height, bracket_thickness)

# Add the cylindrical boss on top of the bracket
result = (
    result.faces(">Z")
    .workplane()
    .center(0, bracket_height/2 - boss_diameter/2)
    .circle(boss_diameter/2)
    .extrude(boss_diameter)
)

# Add the mounting hole near bottom left corner
result = (
    result.faces("<Y")
    .workplane(offset=-bracket_thickness/2)
    .center(-bracket_width/2 + 5, -bracket_height/2 + 5)
    .hole(mounting_hole_diameter)
)

# Add the small rectangular protrusion on the left side
result = (
    result.faces("<X")
    .workplane(offset=bracket_thickness/2)
    .center(-bracket_width/2 + 5, 0)
    .rect(protrusion_width, protrusion_height)
    .extrude(protrusion_depth)
)

# Create the curved tube
# Start from the center of the boss and create a curved path
# The tube will go up from the boss, curve left, and then slightly angle down
tube_start_y = bracket_height/2 - boss_diameter/2
tube_end_y = tube_start_y + tube_length * 0.3  # Adjust for curve
tube_end_x = -bracket_width/2 - tube_length * 0.7  # Curved to the left

# Create the tube path
tube_path = (
    cq.Workplane("XY")
    .moveTo(0, tube_start_y)
    .threePointArc((tube_length/4, tube_start_y + tube_length/4), (tube_length/2, tube_end_y))
    .lineTo(tube_end_x, tube_end_y)
)

# Create the tube by revolving the path
result = (
    result.faces(">Z")
    .workplane()
    .center(0, tube_start_y)
    .circle(tube_diameter/2)
    .workplane(offset=tube_length/2)
    .circle(tube_diameter/2)
    .loft(combine=True)
)

# Alternative approach for the tube - simpler extrusion with curved path
# Create a circular profile at the base of the tube
tube_base = (
    cq.Workplane("XY")
    .center(0, bracket_height/2 - boss_diameter/2)
    .circle(tube_diameter/2)
    .extrude(2)
)

# Create the curved tube using a more direct approach
# Create the tube from the boss to the left
tube = (
    cq.Workplane("XY")
    .center(0, bracket_height/2 - boss_diameter/2)
    .circle(tube_diameter/2)
    .workplane(offset=15)  # Intermediate point
    .circle(tube_diameter/2)
    .workplane(offset=30)  # Another intermediate point
    .circle(tube_diameter/2)
    .workplane(offset=40)  # End point
    .circle(tube_diameter/2)
    .loft(combine=True)
)

# Add the tube to the result
result = result.union(tube)

# Simplified approach - create the curved tube directly
# First create the base bracket
result = cq.Workplane("XY").box(bracket_width, bracket_height, bracket_thickness)

# Add the boss
result = (
    result.faces(">Z")
    .workplane()
    .center(0, bracket_height/2 - boss_diameter/2)
    .circle(boss_diameter/2)
    .extrude(boss_diameter)
)

# Add mounting hole
result = (
    result.faces("<Y")
    .workplane(offset=-bracket_thickness/2)
    .center(-bracket_width/2 + 5, -bracket_height/2 + 5)
    .hole(mounting_hole_diameter)
)

# Add protrusion
result = (
    result.faces("<X")
    .workplane(offset=bracket_thickness/2)
    .center(-bracket_width/2 + 5, 0)
    .rect(protrusion_width, protrusion_height)
    .extrude(protrusion_depth)
)

# Create the curved tube - simple approach
# The tube starts at the boss and curves to the left
tube_profile = cq.Workplane("XY").circle(tube_diameter/2)

# Create a path for the tube (simplified arc)
tube_path_points = [
    (0, bracket_height/2 - boss_diameter/2),
    (-10, bracket_height/2 - boss_diameter/2 + 10),
    (-20, bracket_height/2 - boss_diameter/2 + 20),
    (-30, bracket_height/2 - boss_diameter/2 + 15),
    (-40, bracket_height/2 - boss_diameter/2 + 5)
]

# Create a smooth tube by extruding a circle along a path
# For a more accurate curved tube, let's create a more realistic approach:

# Create the main bracket structure
base_bracket = cq.Workplane("XY").box(bracket_width, bracket_height, bracket_thickness)

# Add boss
boss = (
    base_bracket.faces(">Z")
    .workplane()
    .center(0, bracket_height/2 - boss_diameter/2)
    .circle(boss_diameter/2)
    .extrude(boss_diameter)
)

# Add mounting hole
hole_bracket = (
    boss.faces("<Y")
    .workplane(offset=-bracket_thickness/2)
    .center(-bracket_width/2 + 5, -bracket_height/2 + 5)
    .hole(mounting_hole_diameter)
)

# Add protrusion
final_bracket = (
    hole_bracket.faces("<X")
    .workplane(offset=bracket_thickness/2)
    .center(-bracket_width/2 + 5, 0)
    .rect(protrusion_width, protrusion_height)
    .extrude(protrusion_depth)
)

# Create the tube as a curved extrusion
# Start with the tube profile at the boss location
tube_profile = cq.Workplane("XY").circle(tube_diameter/2)

# Create a curved tube with a smooth arc
# We'll create a tube by extruding along a curved path
tube = (
    cq.Workplane("XY")
    .center(0, bracket_height/2 - boss_diameter/2)
    .circle(tube_diameter/2)
    .workplane(offset=20)
    .circle(tube_diameter/2)
    .workplane(offset=40)
    .circle(tube_diameter/2)
    .loft(combine=True)
)

# The final result
result = final_bracket.union(tube)