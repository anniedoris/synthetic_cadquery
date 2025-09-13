import cadquery as cq
from math import sin, cos, pi

# Define dimensions
hub_diameter = 10.0
hub_length = 15.0
section_width = 4.0
section_height = 8.0
section_length = 30.0

# Create the central hub
hub = cq.Workplane("XY").circle(hub_diameter/2).extrude(hub_length)

# Create the three rectangular sections
sections = cq.Workplane("XY")

# Define the three positions (120 degrees apart)
angles = [0, 2*pi/3, 4*pi/3]

for angle in angles:
    # Create a workplane for each section
    section_wp = cq.Workplane("XY").transformed(
        offset=cq.Vector(0, 0, hub_length/2),
        rotate=cq.Vector(0, 0, angle)
    )
    
    # Create the rectangular section
    section = (
        section_wp
        .rect(section_width, section_height, centered=True)
        .extrude(section_length)
    )
    
    # Position the section correctly
    section = section.translate(cq.Vector(
        (hub_diameter/2 + section_length/2) * cos(angle),
        (hub_diameter/2 + section_length/2) * sin(angle),
        0
    ))
    
    sections = sections.union(section)

# Combine the hub and sections
result = hub.union(sections)

# Add a slight reinforcement at the connection points
reinforcements = cq.Workplane("XY")

for angle in angles:
    # Create reinforcement at connection points
    reinforcement_wp = cq.Workplane("XY").transformed(
        offset=cq.Vector(0, 0, hub_length/2),
        rotate=cq.Vector(0, 0, angle)
    )
    
    # Create slightly thicker connection area
    reinforcement = (
        reinforcement_wp
        .rect(section_width + 2, section_height + 2, centered=True)
        .extrude(2)
    )
    
    # Position the reinforcement
    reinforcement = reinforcement.translate(cq.Vector(
        (hub_diameter/2 + 1) * cos(angle),
        (hub_diameter/2 + 1) * sin(angle),
        0
    ))
    
    reinforcements = reinforcements.union(reinforcement)

# Combine everything together
result = result.union(reinforcements)