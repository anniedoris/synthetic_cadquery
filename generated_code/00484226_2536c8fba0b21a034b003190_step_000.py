import cadquery as cq

# Container dimensions
base_length = 100.0
base_width = 60.0
base_height = 20.0
recess_diameter = 10.0
recess_depth = 5.0
lid_thickness = 3.0
hinge_width = 8.0
hinge_height = 15.0

# Create the base
base = cq.Workplane("XY").box(base_length, base_width, base_height)

# Add rounded edges to the base
base = base.edges("|Z").fillet(5.0)

# Create grid of recesses
# Calculate number of recesses in each direction
num_rows = 4
num_cols = 6
row_spacing = base_width / (num_rows + 1)
col_spacing = base_length / (num_cols + 1)

# Create recesses
recesses = base.faces(">Z").workplane(offset=-0.1)
for i in range(num_rows):
    for j in range(num_cols):
        x = (j + 1) * col_spacing - base_length / 2
        y = (i + 1) * row_spacing - base_width / 2
        recesses = recesses.center(x, y).circle(recess_diameter/2).cutBlind(-recess_depth)

# Create the lid
lid = cq.Workplane("XY").box(base_length, base_width, lid_thickness)

# Add rounded edges to the lid
lid = lid.edges("|Z").fillet(5.0)

# Create hinge slot in the base
hinge_slot = base.faces(">Z").workplane(offset=-0.1).center(-base_length/2 + hinge_width/2, 0).rect(hinge_width, base_width - 10, forConstruction=True).vertices().hole(2.0)

# Create hinge tab on lid
hinge_tab = lid.faces(">Z").workplane(offset=lid_thickness).center(-base_length/2 + hinge_width/2, 0).rect(hinge_width, hinge_height, forConstruction=True).vertices().hole(2.0)

# Position the lid
lid = lid.translate((0, 0, base_height))

# Create the final result
result = base.union(lid)

# Add some clearance for the lid to slide on
result = result.faces(">Z").workplane(offset=-0.1).rect(base_length - 2, base_width - 2, forConstruction=True).vertices().hole(1.0)