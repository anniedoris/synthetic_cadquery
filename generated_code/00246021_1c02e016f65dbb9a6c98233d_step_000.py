import cadquery as cq

# Define dimensions
cube_size = 20.0
cylinder_diameter = 8.0
shaft_diameter = 4.0
groove_diameter = 3.0
indentation_diameter = 12.0
hole_diameter = 2.0
hole_spacing = 4.0

# Create left component
left_cube = cq.Workplane("XY").box(cube_size, cube_size, cube_size)

# Add central cylindrical section
left_cylinder = (
    left_cube.faces(">Z")
    .workplane()
    .circle(cylinder_diameter / 2.0)
    .extrude(cube_size / 2.0)
)

# Add shaft end with groove
left_shaft = (
    left_cylinder.faces(">Z")
    .workplane()
    .circle(shaft_diameter / 2.0)
    .extrude(5.0)
)

# Add groove
left_groove = (
    left_shaft.faces(">Z")
    .workplane()
    .circle(groove_diameter / 2.0)
    .extrude(1.0)
)

# Add end plate with holes
left_plate = (
    left_groove.faces("<Z")
    .workplane()
    .circle(indentation_diameter / 2.0)
    .extrude(2.0)
)

# Add cross pattern holes
left_holes = (
    left_plate.faces("<Z")
    .workplane()
    .center(0, hole_spacing / 2.0)
    .circle(hole_diameter / 2.0)
    .center(0, -hole_spacing)
    .circle(hole_diameter / 2.0)
    .center(-hole_spacing / 2.0, 0)
    .circle(hole_diameter / 2.0)
    .center(hole_spacing, 0)
    .circle(hole_diameter / 2.0)
    .cutThruAll()
)

# Create right component
right_cube = cq.Workplane("XY").box(cube_size, cube_size, cube_size)

# Add central cylindrical section
right_cylinder = (
    right_cube.faces(">Z")
    .workplane()
    .circle(cylinder_diameter / 2.0)
    .extrude(cube_size / 2.0)
)

# Add shaft end with groove
right_shaft = (
    right_cylinder.faces(">Z")
    .workplane()
    .circle(shaft_diameter / 2.0)
    .extrude(5.0)
)

# Add groove
right_groove = (
    right_shaft.faces(">Z")
    .workplane()
    .circle(groove_diameter / 2.0)
    .extrude(1.0)
)

# Add end plate with holes
right_plate = (
    right_groove.faces("<Z")
    .workplane()
    .circle(indentation_diameter / 2.0)
    .extrude(2.0)
)

# Add cross pattern holes
right_holes = (
    right_plate.faces("<Z")
    .workplane()
    .center(0, hole_spacing / 2.0)
    .circle(hole_diameter / 2.0)
    .center(0, -hole_spacing)
    .circle(hole_diameter / 2.0)
    .center(-hole_spacing / 2.0, 0)
    .circle(hole_diameter / 2.0)
    .center(hole_spacing, 0)
    .circle(hole_diameter / 2.0)
    .cutThruAll()
)

# Position right component to connect with left
right_component = right_holes.translate((cube_size, 0, 0))

# Combine both components
result = left_holes.union(right_component)

# Move to center for better visualization
result = result.translate((-cube_size/2, -cube_size/2, -cube_size/2))