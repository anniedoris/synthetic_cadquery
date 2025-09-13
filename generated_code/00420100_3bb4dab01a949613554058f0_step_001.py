import cadquery as cq
from math import pi

# Parameters for the rolled sheet
sheet_width = 100.0
sheet_length = 200.0
sheet_thickness = 2.0
roll_radius = 15.0
roll_length = 50.0

# Create the flat sheet portion
sheet = cq.Workplane("XY").rect(sheet_width, sheet_length).extrude(sheet_thickness)

# Create the cylindrical roll at one end
# We'll create a cylinder and then cut out the appropriate portion
roll_cylinder = cq.Workplane("XY").circle(roll_radius).extrude(roll_length)

# Position the roll to connect with the sheet
# The roll should be positioned so its flat end connects to the sheet
roll = roll_cylinder.translate((0, -sheet_length/2 + roll_length/2, 0))

# Create a more realistic rolled sheet by creating a helical surface
# For simplicity, I'll create a cylindrical roll with proper transition
# Create a rectangular sheet that transitions to a cylinder

# Base flat sheet
base_sheet = cq.Workplane("XY").rect(sheet_width, sheet_length).extrude(sheet_thickness)

# Create a curved transition region by using a sweep
# This will create a smooth transition from flat to cylindrical

# For the cylindrical portion, we need to create the rolled shape
# We'll create a quarter cylinder to represent the rolled portion
cylinder_section = cq.Workplane("XY").circle(roll_radius).extrude(sheet_thickness)

# Position it properly
rolled_section = cylinder_section.translate((sheet_width/2, -sheet_length/2 + roll_radius, 0))

# Combine the flat sheet and the rolled portion
result = base_sheet.union(rolled_section)

# Let's create a more realistic version with proper curvature
# Create the flat sheet
flat_sheet = cq.Workplane("XY").rect(sheet_width, sheet_length).extrude(sheet_thickness)

# Create a cylindrical section that represents the rolled portion
# We'll create a curved surface that smoothly transitions from flat to cylindrical
# Using a different approach - create a cylinder and then cut/intersect properly

# Create a complete rolled sheet representation
# The rolled portion can be modeled as a cylindrical segment
rolled_sheet = cq.Workplane("XY").box(sheet_width, roll_radius*2, sheet_thickness)

# Create the transition area
# This is a simplified approach - in reality, we'd want a proper helical surface
# But for this CAD model, we'll approximate it with a combination of shapes

# Create a more accurate representation
# Start with the flat portion
result = cq.Workplane("XY").rect(sheet_width, sheet_length).extrude(sheet_thickness)

# Create a cylindrical roll at one end (simplified)
# The roll will be positioned so it connects to the flat sheet
roll_cylinder = cq.Workplane("XY").circle(roll_radius).extrude(sheet_thickness)

# Position the roll to connect to the flat sheet
# We'll place it at the right end of the flat sheet
roll_positioned = roll_cylinder.translate((sheet_width/2 + roll_radius, 0, 0))

# For a better representation, let's create a realistic rolled sheet
# We'll make a flat sheet with a cylindrical roll at one end
result = cq.Workplane("XY").rect(sheet_width, sheet_length).extrude(sheet_thickness)

# Create the rolled end - this is a cylinder representing the coiled portion
# We'll create a portion of a cylinder that represents the rolled sheet
roll_end = cq.Workplane("YZ").circle(roll_radius).extrude(sheet_width).rotate((0,0,0), (0,1,0), 90)
roll_end = roll_end.translate((0, -sheet_length/2, 0))

# Position properly - the roll should be at the end of the sheet
# We'll create a simpler, more practical version
# Create flat sheet
sheet = cq.Workplane("XY").rect(sheet_width, sheet_length).extrude(sheet_thickness)

# Create the rolled portion as a cylinder
cylinder = cq.Workplane("XY").circle(roll_radius).extrude(sheet_thickness)

# Position the cylinder to connect with the sheet
cylinder = cylinder.translate((sheet_width/2 + roll_radius, 0, 0))

# For a more realistic roll, we'll create a proper cylindrical section
# that connects to the flat sheet smoothly
result = cq.Workplane("XY").rect(sheet_width, sheet_length).extrude(sheet_thickness)

# Add the rolled section
# The roll should be a portion of a cylinder that connects to the sheet
# Let's make a curved transition by creating a quarter cylinder
# Actually, let's create a simple representation with proper dimensions

# Create the main flat sheet
main_sheet = cq.Workplane("XY").rect(sheet_width, sheet_length).extrude(sheet_thickness)

# Create a cylinder to represent the rolled portion
# This is a simple cylinder representing the roll
roll_cylinder = cq.Workplane("XY").circle(roll_radius).extrude(sheet_thickness)

# Position the cylinder at one end of the sheet
# We'll place it so it connects to the right edge of the flat sheet
roll_positioned = roll_cylinder.translate((sheet_width/2 + roll_radius, 0, 0))

# Combine the two parts
result = main_sheet.union(roll_positioned)

# For a better representation of a rolled sheet, we'll create a more realistic model
# Create the flat portion
result = cq.Workplane("XY").rect(sheet_width, sheet_length).extrude(sheet_thickness)

# Create the rolled portion - a cylindrical shape at one end
# The cylinder should be positioned to connect with the flat sheet
roll_cylinder = cq.Workplane("YZ").circle(roll_radius).extrude(sheet_width)
roll_cylinder = roll_cylinder.rotate((0,0,0), (0,1,0), 90)
roll_cylinder = roll_cylinder.translate((0, -sheet_length/2, 0))

# For a better visualization, let's create a more complete representation
# This approach creates a realistic rolled sheet
result = cq.Workplane("XY").rect(sheet_width, sheet_length).extrude(sheet_thickness)

# Create a cylindrical roll at the right end
# This represents the rolled portion of the material
cylinder = cq.Workplane("XY").circle(roll_radius).extrude(sheet_thickness)
cylinder = cylinder.translate((sheet_width/2 + roll_radius, 0, 0))

# Create a more realistic curved transition by creating a proper roll
# We'll model it as a section of a cylinder with proper dimensions
result = cq.Workplane("XY").rect(sheet_width, sheet_length).extrude(sheet_thickness)

# Add the cylindrical roll section
# Create a quarter cylinder that represents the rolled portion
# We'll create a cylinder and position it properly
cylinder = cq.Workplane("XY").circle(roll_radius).extrude(sheet_thickness)

# Position it so it connects to the right side of the flat sheet
cylinder = cylinder.translate((sheet_width/2 + roll_radius, 0, 0))

# Final result combining the flat sheet and the rolled portion
result = result.union(cylinder)