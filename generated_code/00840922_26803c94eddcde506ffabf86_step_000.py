import cadquery as cq

# Define dimensions
frame_length = 200.0
frame_width = 100.0
frame_height = 50.0
thickness = 5.0
cutout_width = 10.0
cutout_height = 15.0
cutout_spacing = 20.0

# Create top and bottom frames with cutouts
top_bottom_frame = cq.Workplane("XY").box(frame_length, frame_width, thickness)

# Add cutouts to top and bottom frames
cutout_count = int((frame_length - cutout_width) / cutout_spacing) + 1
for i in range(cutout_count):
    x_pos = -frame_length/2 + cutout_width/2 + i * cutout_spacing
    top_bottom_frame = (
        top_bottom_frame.faces(">Z")
        .workplane(offset=0.1)
        .center(x_pos, 0)
        .rect(cutout_width, cutout_height, forConstruction=True)
        .vertices()
        .hole(2.0)
    )

# Create side panels
side_panel = cq.Workplane("XY").box(frame_width, frame_height, thickness)

# Create front and back panels (same size as top/bottom but no cutouts)
front_back_panel = cq.Workplane("XY").box(frame_length, frame_height, thickness)

# Create small reinforcement pieces
reinforcement = cq.Workplane("XY").box(20.0, 10.0, thickness)

# Combine all components
result = (
    top_bottom_frame.translate((0, 0, frame_height/2 + thickness/2))
    .union(side_panel.translate((frame_length/2 + thickness/2, 0, frame_height/2)))
    .union(side_panel.translate((-frame_length/2 - thickness/2, 0, frame_height/2)))
    .union(front_back_panel.translate((0, frame_height/2 + thickness/2, 0)))
    .union(front_back_panel.translate((0, -frame_height/2 - thickness/2, 0)))
    .union(reinforcement.translate((frame_length/2 - 30, frame_height/2 - 15, 0)))
    .union(reinforcement.translate((-frame_length/2 + 30, frame_height/2 - 15, 0)))
    .union(reinforcement.translate((frame_length/2 - 30, -frame_height/2 + 15, 0)))
    .union(reinforcement.translate((-frame_length/2 + 30, -frame_height/2 + 15, 0)))
)