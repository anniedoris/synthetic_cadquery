import cadquery as cq

# Dimensions
bed_length = 190.0   # Length of the bed frame
bed_width = 90.0     # Width of the bed frame
bed_height = 40.0    # Height of the bed frame (from ground to top of headboard)
base_thickness = 5.0 # Thickness of the base
headboard_height = 30.0 # Height of the headboard
leg_height = 35.0    # Height of the legs
leg_radius = 5.0     # Radius of cylindrical legs
slat_width = 2.0     # Width of vertical slats
slat_spacing = 8.0   # Spacing between slats
slat_count = 6       # Number of slats

# Create the base of the bed frame
base = cq.Workplane("XY").box(bed_length, bed_width, base_thickness)

# Create the headboard
headboard = cq.Workplane("XY").box(bed_length, bed_width, headboard_height)
headboard = headboard.translate((0, 0, base_thickness))

# Create vertical slats for the headboard
slats = cq.Workplane("XY")
for i in range(slat_count):
    slat_x = -bed_length/2 + (i * slat_spacing) + slat_width/2
    slat = cq.Workplane("XY").box(slat_width, bed_width, headboard_height)
    slat = slat.translate((slat_x, 0, base_thickness))
    slats = slats.union(slat)

# Combine base and headboard with slats
bed_frame = base.union(headboard).union(slats)

# Create legs at each corner
leg_positions = [
    (-bed_length/2 + leg_radius, -bed_width/2 + leg_radius),  # Bottom-left
    (bed_length/2 - leg_radius, -bed_width/2 + leg_radius),   # Bottom-right
    (-bed_length/2 + leg_radius, bed_width/2 - leg_radius),   # Top-left
    (bed_length/2 - leg_radius, bed_width/2 - leg_radius)     # Top-right
]

for x, y in leg_positions:
    leg = cq.Workplane("XY").circle(leg_radius).extrude(leg_height)
    leg = leg.translate((x, y, -leg_height))
    bed_frame = bed_frame.union(leg)

# Ensure the final object is properly assembled
result = bed_frame

# Add some fillets to make it look more realistic
result = result.edges("|Z").fillet(1.0)