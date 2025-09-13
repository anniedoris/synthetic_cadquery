import cadquery as cq

# Dimensions
base_width = 100.0
base_length = 150.0
base_thickness = 10.0

beam_height = 80.0
beam_width = 20.0
beam_thickness = 10.0

connecting_plate_width = 100.0
connecting_plate_length = 20.0
connecting_plate_thickness = 10.0

hopper_wall_width = 100.0
hopper_wall_length = 80.0
hopper_wall_thickness = 10.0

hopper_base_width = 100.0
hopper_base_length = 80.0
hopper_base_thickness = 10.0

bracing_width = 10.0
bracing_height = 20.0
bracing_thickness = 10.0

hole_diameter = 6.0
hole_spacing = 20.0

# Create base plate
result = cq.Workplane("XY").box(base_width, base_length, base_thickness)

# Add support beams
beam_offset_x = (base_width - 2 * beam_width - beam_thickness) / 2
result = (
    result.faces(">Z")
    .workplane()
    .rect(beam_width, beam_thickness, forConstruction=True)
    .vertices()
    .box(beam_width, beam_thickness, beam_height)
)

# Add connecting plate
result = (
    result.faces(">Z")
    .workplane(offset=beam_height)
    .rect(connecting_plate_width, connecting_plate_length)
    .extrude(connecting_plate_thickness)
)

# Add hopper walls
hopper_wall_offset_x = (base_width - hopper_wall_width) / 2
hopper_wall_offset_y = (base_length - hopper_wall_length) / 2

# Create hopper walls with inclination
hopper_wall = (
    cq.Workplane("XY")
    .box(hopper_wall_width, hopper_wall_length, hopper_wall_thickness)
    .rotate((0, 0, 0), (1, 0, 0), 45)
    .translate((0, 0, -hopper_wall_thickness/2))
)

# Add hopper walls to the structure
result = result.union(hopper_wall.translate((0, 0, beam_height + connecting_plate_thickness)))

# Add hopper base
result = (
    result.faces(">Z")
    .workplane(offset=beam_height + connecting_plate_thickness + hopper_wall_thickness)
    .rect(hopper_base_width, hopper_base_length)
    .extrude(hopper_base_thickness)
)

# Add bracing elements
bracing_offset_x = (base_width - bracing_width) / 2
result = (
    result.faces(">Z")
    .workplane(offset=beam_height)
    .rect(bracing_width, bracing_height, forConstruction=True)
    .vertices()
    .box(bracing_width, bracing_height, bracing_thickness)
)

# Add holes to base plate
result = (
    result.faces("<Z")
    .workplane()
    .rect(base_width - hole_spacing, base_length - hole_spacing, forConstruction=True)
    .vertices()
    .hole(hole_diameter)
)

# Add holes to connecting plate
result = (
    result.faces(">Z")
    .workplane(offset=beam_height)
    .rect(connecting_plate_width - hole_spacing, connecting_plate_length - hole_spacing, forConstruction=True)
    .vertices()
    .hole(hole_diameter)
)

# Add holes to hopper walls
result = (
    result.faces("<Z")
    .workplane(offset=beam_height + connecting_plate_thickness + hopper_wall_thickness)
    .rect(hopper_wall_width - hole_spacing, hopper_wall_length - hole_spacing, forConstruction=True)
    .vertices()
    .hole(hole_diameter)
)

# Add holes to hopper base
result = (
    result.faces(">Z")
    .workplane(offset=beam_height + connecting_plate_thickness + hopper_wall_thickness + hopper_base_thickness)
    .rect(hopper_base_width - hole_spacing, hopper_base_length - hole_spacing, forConstruction=True)
    .vertices()
    .hole(hole_diameter)
)

# Add holes to support beams
result = (
    result.faces(">Z")
    .workplane(offset=beam_height)
    .rect(beam_width - hole_spacing, beam_thickness - hole_spacing, forConstruction=True)
    .vertices()
    .hole(hole_diameter)
)

result = result.translate((-base_width/2, -base_length/2, 0))