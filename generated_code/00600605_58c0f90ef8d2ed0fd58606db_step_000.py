import cadquery as cq

# Define dimensions
base_length = 60.0
base_width = 30.0
base_height = 10.0

upper_length = 60.0
upper_width = 30.0
upper_height = 10.0

connecting_height = 20.0
connecting_base = 15.0

circle_diameter = 12.0
notch_width = 8.0
notch_height = 6.0
notch_depth = 4.0

# Create base section
base = cq.Workplane("XY").box(base_length, base_width, base_height)

# Add circular cutout in base
base = base.faces(">Z").workplane().circle(circle_diameter/2).cutThruAll()

# Add notches to base
base = base.faces(">Z").workplane(offset=base_height/2).rect(notch_width, notch_height, forConstruction=True).vertices().rect(notch_width, notch_depth).extrude(notch_depth)

# Create upper section
upper = cq.Workplane("XY").box(upper_length, upper_width, upper_height)

# Add circular cutout in upper
upper = upper.faces(">Z").workplane().circle(circle_diameter/2).cutThruAll()

# Add notches to upper
upper = upper.faces(">Z").workplane(offset=upper_height/2).rect(notch_width, notch_height, forConstruction=True).vertices().rect(notch_width, notch_depth).extrude(notch_depth)

# Position upper section
upper = upper.translate((0, 0, base_height))

# Create connecting triangular piece
# This connects the base and upper sections
connecting = cq.Workplane("XY").polygon(3, connecting_base).extrude(connecting_height)
connecting = connecting.rotate((0, 0, 0), (0, 1, 0), 90)
connecting = connecting.translate((0, 0, base_height))

# Combine all parts
result = base.union(upper).union(connecting)

# Add a slight angle to the sections for trapezoidal shape
# Rotate upper section
upper = upper.rotate((0, 0, 0), (1, 0, 0), 15)
# Add the angled upper section to the result
result = result.union(upper)

# Create the base with angle
base = base.rotate((0, 0, 0), (1, 0, 0), -15)
result = result.union(base)

# Adjust to have correct alignment
result = result.translate((0, 0, 0))