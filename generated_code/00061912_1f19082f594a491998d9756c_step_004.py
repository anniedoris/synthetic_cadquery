import cadquery as cq

# Define the dimensions of the rectangular prism
length = 100.0
width = 30.0
height = 20.0

# Create the base rectangular prism
result = cq.Workplane("XY").box(length, width, height)

# Define the cavity profile points (irregular amoeba-like shape)
# These points define a smooth, irregular shape centered in the prism
cavity_points = [
    (0, 10),      # Center top
    (5, 8),       # Right top
    (8, 5),       # Right middle
    (7, 0),       # Right bottom
    (3, -5),      # Bottom center
    (-3, -5),     # Bottom center left
    (-7, 0),      # Left bottom
    (-8, 5),      # Left middle
    (-5, 8),      # Left top
    (0, 10),      # Back to center top
]

# Create the cavity by drawing the profile and extruding it
# The cavity extends from the front face to the back face, leaving a solid section
cavity_profile = (
    cq.Workplane("XY")
    .polyline(cavity_points)
    .close()
    .extrude(height)
)

# Cut the cavity from the main prism
result = result.cut(cavity_profile)

# Add fillets to the internal edges of the cavity for smooth transitions
# This will make the cavity walls smooth and avoid sharp corners
result = result.edges("|Z").fillet(1.0)

# The object is now a rectangular prism with a smooth, irregular cavity cut out
# from the center, extending from front to back face