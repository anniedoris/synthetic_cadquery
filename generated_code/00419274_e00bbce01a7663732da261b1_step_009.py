import cadquery as cq

# Define dimensions for each tier
bottom_width = 4.0
bottom_length = 6.0
bottom_height = 1.0

middle_width = 3.0
middle_length = 5.0
middle_height = 1.0

top_width = 2.0
top_length = 4.0
top_height = 1.0

# Create the bottom tier
bottom = cq.Workplane("XY").box(bottom_width, bottom_length, bottom_height)

# Create the middle tier and position it on top of the bottom tier
middle = cq.Workplane("XY").box(middle_width, middle_length, middle_height).translate((0, 0, bottom_height))

# Create the top tier and position it on top of the middle tier
top = cq.Workplane("XY").box(top_width, top_length, top_height).translate((0, 0, bottom_height + middle_height))

# Combine all tiers into a single object
result = bottom.union(middle).union(top)