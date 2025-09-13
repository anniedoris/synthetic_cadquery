import cadquery as cq
from math import sin, cos, pi

# Parameters for the structure
num_rods = 5
rod_length = 100.0
rod_diameter = 5.0
rect_width = 10.0
rect_height = 3.0
rect_depth = 2.0
vertical_spacing = 15.0
horizontal_spacing = 20.0

# Create the main structure
result = cq.Workplane("XY")

# Create rods with rectangular sections
for i in range(num_rods):
    # Position rods in a staggered pattern with perspective
    z_offset = i * vertical_spacing * 0.7  # Staggered in Z direction
    y_offset = i * horizontal_spacing * 0.8  # Staggered in Y direction
    
    # Create the rod - a cylinder
    rod = cq.Workplane("XY").center(0, y_offset).circle(rod_diameter/2).extrude(rod_length)
    
    # Position the rod with perspective (rotated for diagonal effect)
    rod = rod.rotateAboutCenter((0, 0, 1), 15 * i)  # Rotate each rod slightly
    
    # Add rectangular sections at various positions along the rod
    # Position sections at different points along the rod
    section_positions = [10, 30, 50, 70, 90]  # Positions along the rod
    
    # Add sections to this rod
    for pos in section_positions:
        if pos < rod_length:  # Only add if within rod length
            # Create rectangular section
            section = cq.Workplane("XY").center(0, y_offset).moveTo(0, 0).rect(rect_width, rect_height).extrude(rect_depth)
            
            # Position the section along the rod
            section = section.translate((0, y_offset, pos))
            
            # Rotate section to be perpendicular to the rod
            section = section.rotateAboutCenter((0, 1, 0), 90)
            
            # Add section to the rod
            rod = rod.union(section)
    
    # Add the rod to the main result
    result = result.union(rod)

# Create a base plate for stability
base_plate = cq.Workplane("XY").box(200, 150, 5)

# Add the base plate to the result
result = result.union(base_plate)

# Add some structural elements to make it more realistic
# Create connecting beams between the rods
for i in range(num_rods - 1):
    # Connect adjacent rods with a beam
    start_x = i * horizontal_spacing * 0.8
    end_x = (i + 1) * horizontal_spacing * 0.8
    
    # Create a connecting beam
    beam = cq.Workplane("XY").center(0, (start_x + end_x) / 2).rect(20, 3).extrude(5)
    beam = beam.rotateAboutCenter((0, 0, 1), 15 * i)
    result = result.union(beam)

# Position the entire assembly properly
result = result.translate((0, 0, 0))