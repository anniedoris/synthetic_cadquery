import cadquery as cq

# Define dimensions
panel_width = 200.0
panel_height = 150.0
panel_thickness = 10.0

# Define cutout dimensions and spacing
cutout_width = 20.0
cutout_height = 15.0
rows = 3
cols = 4

# Calculate spacing between cutouts
spacing_x = (panel_width - (cols * cutout_width)) / (cols + 1)
spacing_y = (panel_height - (rows * cutout_height)) / (rows + 1)

# Create the main panel
result = cq.Workplane("XY").box(panel_width, panel_height, panel_thickness)

# Add the cutouts in a grid pattern
for i in range(rows):
    for j in range(cols):
        # Calculate position for each cutout
        x_pos = -panel_width/2 + spacing_x + j * (cutout_width + spacing_x)
        y_pos = -panel_height/2 + spacing_y + i * (cutout_height + spacing_y)
        
        # Create workplane at the cutout position
        result = (
            result.faces(">Z")
            .workplane(offset=0.1)  # Slightly above the surface
            .center(x_pos, y_pos)
            .rect(cutout_width, cutout_height)
            .cutThruAll()
        )

# The cutThruAll() will cut through the entire thickness, creating recessed holes