import cadquery as cq

# Define dimensions
length = 100.0      # Length of the wedge
top_width = 60.0    # Width at the top (longer side)
bottom_width = 40.0 # Width at the bottom (shorter side)
height = 20.0       # Thickness/height of the wedge

# Define hole parameters
hole_diameter = 6.0
hole_spacing_x = 25.0
hole_spacing_y = 15.0

# Create the trapezoidal wedge
result = (
    cq.Workplane("XY")
    .rect(top_width, height)  # Start with top rectangle
    .workplane(offset=height)  # Move to bottom
    .rect(bottom_width, height)  # Bottom rectangle
    .loft(combine=True)  # Loft between top and bottom to create trapezoid
)

# Add holes to the top surface
result = (
    result.faces(">Z")
    .workplane()
    .pushPoints([
        (-hole_spacing_x/2, hole_spacing_y/2),  # Top left hole
        (hole_spacing_x/2, hole_spacing_y/2),   # Top right hole
        (-hole_spacing_x/2, -hole_spacing_y/2), # Bottom left hole
        (hole_spacing_x/2, -hole_spacing_y/2)   # Bottom right hole
    ])
    .hole(hole_diameter)
)

# Ensure the result is properly oriented and positioned
result = result.rotate((0, 0, 0), (0, 0, 1), 0)