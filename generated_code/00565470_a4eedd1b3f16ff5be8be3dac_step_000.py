import cadquery as cq

# Define cube dimensions
cube_size = 20.0
frame_thickness = 2.0

# Create the solid cube
solid_cube = cq.Workplane("XY").box(cube_size, cube_size, cube_size)

# Create the hollow cube frame
# First, create the outer cube
outer_cube = cq.Workplane("XY").box(cube_size, cube_size, cube_size)
# Then create the inner cube (to make it hollow)
inner_cube = cq.Workplane("XY").box(cube_size - 2*frame_thickness, 
                                   cube_size - 2*frame_thickness, 
                                   cube_size - 2*frame_thickness)
# Subtract the inner cube from the outer cube to create the frame
hollow_cube = outer_cube.cut(inner_cube)

# Position the solid cube slightly to the right and lower
solid_cube = solid_cube.translate((5, -5, 0))

# Position the hollow cube at an angle to create the connection
hollow_cube = hollow_cube.rotate((0, 0, 0), (0, 0, 1), 15)  # Rotate 15 degrees
hollow_cube = hollow_cube.translate((-5, 5, 0))

# Combine both cubes into the final result
result = solid_cube.union(hollow_cube)