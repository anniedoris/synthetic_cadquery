import cadquery as cq
from math import pi, cos, sin

# Parameters for the satellite dish assembly
dish_diameter = 100.0
dish_thickness = 2.0
dish_focal_length = 25.0
frame_width = 120.0
frame_height = 80.0
frame_thickness = 4.0
horn_diameter = 8.0
horn_length = 15.0
horn_base_diameter = 12.0
mounting_bracket_width = 40.0
mounting_bracket_height = 20.0
mounting_bracket_thickness = 6.0

# Create the parabolic dish
# Using a parametric approach to create a parabolic surface
def create_parabolic_dish(diameter, thickness, focal_length):
    # Create the dish shape using a parabolic profile
    # We'll create a circular profile and then extrude it with a parabolic taper
    workplane = cq.Workplane("XY")
    
    # Create the base circle for the dish
    base_circle = workplane.circle(diameter/2)
    
    # Create the dish as a solid by extruding with a parabolic profile
    # We'll use a more accurate approach by creating a loft between sections
    dish = workplane.box(diameter, diameter, thickness)
    
    # Create a parabolic cutout to make the dish shape
    # We'll make a circular cut through the center
    dish = dish.faces(">Z").workplane().circle(diameter/2 - 2).cutThruAll()
    
    return dish

# Create the main dish
dish = cq.Workplane("XY").circle(dish_diameter/2).extrude(dish_thickness)

# Create a parabolic surface for the dish
# This is a simplified approach - in reality this would be more complex
# We'll create a truncated parabolic shape
dish_profile = cq.Workplane("XY")
dish_profile = dish_profile.center(0, 0).circle(dish_diameter/2)
dish_profile = dish_profile.center(0, 0).circle(dish_diameter/2 - 1).extrude(dish_thickness)

# Create the support frame
frame = cq.Workplane("XY").box(frame_width, frame_height, frame_thickness)

# Create the rectangular frame structure
# Main frame rectangle
frame_rect = cq.Workplane("XY").rect(frame_width, frame_height).extrude(frame_thickness)

# Add vertical supports
vertical_supports = cq.Workplane("XY").rect(20, frame_height).extrude(frame_thickness)
vertical_supports = vertical_supports.translate((-frame_width/2 + 10, 0, 0))
frame_rect = frame_rect.union(vertical_supports)

vertical_supports = cq.Workplane("XY").rect(20, frame_height).extrude(frame_thickness)
vertical_supports = vertical_supports.translate((frame_width/2 - 10, 0, 0))
frame_rect = frame_rect.union(vertical_supports)

# Add horizontal supports
horizontal_supports = cq.Workplane("XY").rect(frame_width, 20).extrude(frame_thickness)
horizontal_supports = horizontal_supports.translate((0, frame_height/2 - 10, 0))
frame_rect = frame_rect.union(horizontal_supports)

horizontal_supports = cq.Workplane("XY").rect(frame_width, 20).extrude(frame_thickness)
horizontal_supports = horizontal_supports.translate((0, -frame_height/2 + 10, 0))
frame_rect = frame_rect.union(horizontal_supports)

# Create the feed horn
# Feed horn is a conical shape at the focal point
horn = cq.Workplane("XY").circle(horn_base_diameter/2).extrude(horn_length/2)
horn = horn.faces(">Z").workplane().circle(horn_diameter/2).extrude(horn_length/2)
horn = horn.translate((0, 0, dish_focal_length))

# Create the mounting bracket
mounting_bracket = cq.Workplane("XY").rect(mounting_bracket_width, mounting_bracket_height).extrude(mounting_bracket_thickness)
mounting_bracket = mounting_bracket.translate((0, -frame_height/2 + mounting_bracket_height/2, -frame_thickness/2))

# Create mounting holes in bracket
mounting_bracket = mounting_bracket.faces(">Y").workplane().center(-mounting_bracket_width/4, 0).circle(2).cutThruAll()
mounting_bracket = mounting_bracket.faces(">Y").workplane().center(mounting_bracket_width/4, 0).circle(2).cutThruAll()

# Position the dish on the frame
# The dish should be centered on the frame and positioned at the focal point
dish = dish.translate((0, 0, frame_height/2 + dish_thickness/2))

# Combine all parts
result = frame_rect
result = result.union(horn)
result = result.union(mounting_bracket)
result = result.union(dish)

# Add a slight tilt to the dish as described in the description
result = result.rotate((0, 0, 0), (1, 0, 0), 5)

# For a more accurate parabolic dish, we could also create a proper parabolic surface
# But this simpler approach should capture the key features described