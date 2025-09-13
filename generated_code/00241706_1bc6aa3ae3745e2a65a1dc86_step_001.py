import cadquery as cq

# Define dimensions
leg_length = 50.0
leg_width = 10.0
leg_height = 5.0
curve_radius = 15.0

# Create the 2D profile of the U-shape
# Start with a workplane
result = cq.Workplane("XY")

# Draw the U-shape profile
# Start at the bottom left corner
result = result.moveTo(-leg_length/2, -leg_height/2)
# Draw to the bottom right corner
result = result.lineTo(leg_length/2, -leg_height/2)
# Draw the curved section (quarter circle)
result = result.threePointArc((leg_length/2 + curve_radius, -leg_height/2), (leg_length/2 + curve_radius, leg_height/2))
# Draw to the top right corner
result = result.lineTo(leg_length/2, leg_height/2)
# Draw to the top left corner
result = result.lineTo(-leg_length/2, leg_height/2)
# Draw to the bottom left corner (closing the shape)
result = result.lineTo(-leg_length/2, -leg_height/2)
result = result.close()

# Extrude to create the 3D object
result = result.extrude(leg_width)

# Alternative approach using a more direct method
# Create a rectangular profile and use it to make the U-shape
result = cq.Workplane("XY")

# Create the U-shape using a rectangle and cutting operations
# Base rectangle for the U-shape
result = result.rect(leg_length, leg_height, centered=True)
# Create a hole for the curved section
result = result.center(0, -leg_height/2 + curve_radius)
result = result.circle(curve_radius)
# This approach is complex, let me use a cleaner method

# Let me start over with a clearer approach:
# Create the 2D profile
profile = (
    cq.Workplane("XY")
    .moveTo(-leg_length/2, -leg_height/2)
    .lineTo(leg_length/2, -leg_height/2)
    .threePointArc((leg_length/2 + curve_radius, -leg_height/2), (leg_length/2 + curve_radius, leg_height/2))
    .lineTo(leg_length/2, leg_height/2)
    .lineTo(-leg_length/2, leg_height/2)
    .lineTo(-leg_length/2, -leg_height/2)
    .close()
)

# Extrude the profile
result = profile.extrude(leg_width)