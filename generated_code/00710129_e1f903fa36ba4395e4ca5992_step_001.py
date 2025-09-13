import cadquery as cq

# Dimensions
length = 100.0
width = 60.0
height = 40.0
thickness = 3.0
hole_diameter = 2.5
screw_hole_diameter = 4.0
ventilation_slot_width = 2.0
ventilation_slot_height = 8.0
ventilation_slot_spacing = 10.0
circular_cutout_diameter = 10.0

# Create the main housing
housing = cq.Workplane("XY").box(length, width, height)

# Create the top panel with holes and circular cutout
top_panel = (
    housing.faces(">Z")
    .workplane()
    .rect(length - 2*thickness, width - 2*thickness, forConstruction=True)
    .vertices()
    .hole(screw_hole_diameter)
    .center(-length/2 + thickness + circular_cutout_diameter/2, 0)
    .circle(circular_cutout_diameter/2)
    .cutThruAll()
)

# Create side panels with ventilation slots
side_panel = (
    top_panel.faces("<X")
    .workplane(offset=thickness)
    .rect(height - 2*thickness, width - 2*thickness, forConstruction=True)
    .vertices()
    .hole(screw_hole_diameter)
    .edges("|Z")
    .rect(ventilation_slot_width, ventilation_slot_height, forConstruction=True)
    .vertices()
    .hole(ventilation_slot_width)
)

# Add back panel with ventilation slots
back_panel = (
    side_panel.faces("<Y")
    .workplane(offset=thickness)
    .rect(length - 2*thickness, height - 2*thickness, forConstruction=True)
    .vertices()
    .hole(screw_hole_diameter)
    .edges("|Z")
    .rect(ventilation_slot_width, ventilation_slot_height, forConstruction=True)
    .vertices()
    .hole(ventilation_slot_width)
)

# Create internal shelf
internal_shelf = (
    back_panel.faces("<Y")
    .workplane(offset=thickness)
    .rect(length - 2*thickness, height - 2*thickness)
    .extrude(-thickness)
)

# Final result
result = internal_shelf