import cadquery as cq

# Define dimensions
total_height = 50.0
top_diameter = 20.0
transition_diameter = 18.0
grooved_diameter = 16.0
bottom_diameter = 22.0
groove_depth = 1.0
groove_width = 1.5
groove_count = 8
polygon_sides = 6
polygon_radius = 8.0
transition_height = 5.0
grooved_height = 20.0
flared_height = 10.0

# Create the base workplane
result = cq.Workplane("XY")

# Create the top section with polygonal cavity
result = (
    result.circle(top_diameter/2)
    .extrude(transition_height)
    .faces(">Z")
    .workplane()
    .polygon(polygon_sides, polygon_radius)
    .cutBlind(-groove_depth)
)

# Create the smooth transition cylinder
result = (
    result.faces(">Z")
    .workplane()
    .circle(transition_diameter/2)
    .extrude(transition_height)
)

# Create the grooved section
result = (
    result.faces(">Z")
    .workplane()
    .circle(grooved_diameter/2)
    .extrude(grooved_height)
)

# Add circumferential grooves
groove_radius = grooved_diameter/2 - groove_width/2
for i in range(groove_count):
    angle = (i * 360 / groove_count)
    result = (
        result.faces(">Z")
        .workplane()
        .center(0, 0)
        .rotate((0, 0, 0), (0, 0, 1), angle)
        .rect(groove_width, groove_depth)
        .cutBlind(-groove_depth)
    )

# Create the flared base
result = (
    result.faces(">Z")
    .workplane()
    .circle(bottom_diameter/2)
    .extrude(flared_height)
)

# Ensure the result is properly constructed
result = result.val()

# If we need to adjust the flaring, we could add a fillet or use a more precise approach
# For now, let's make a cleaner version with better geometry

# Alternative approach with more precise grooves
result = cq.Workplane("XY")

# Base cylinder
result = result.circle(top_diameter/2).extrude(transition_height)

# Top polygonal cavity
result = (
    result.faces(">Z")
    .workplane()
    .polygon(polygon_sides, polygon_radius)
    .cutBlind(-groove_depth)
)

# Transition section
result = (
    result.faces(">Z")
    .workplane()
    .circle(transition_diameter/2)
    .extrude(transition_height)
)

# Grooved section
result = (
    result.faces(">Z")
    .workplane()
    .circle(grooved_diameter/2)
    .extrude(grooved_height)
)

# Add grooves using a more precise method
groove_radius = grooved_diameter/2 - groove_width/2
for i in range(groove_count):
    angle = i * 360 / groove_count
    # Create groove at specific angle
    result = (
        result.faces(">Z")
        .workplane()
        .center(0, 0)
        .rotate((0, 0, 0), (0, 0, 1), angle)
        .rect(groove_width, groove_depth)
        .cutBlind(-groove_depth)
    )

# Flared base
result = (
    result.faces(">Z")
    .workplane()
    .circle(bottom_diameter/2)
    .extrude(flared_height)
)

# Final result
result = result.val()