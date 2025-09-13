import cadquery as cq

# Define dimensions
plate_width = 50.0
plate_length = 30.0
plate_thickness = 5.0

cylinder_diameter = 20.0
cylinder_height = 15.0

handle_width = 8.0
handle_length = 25.0
handle_thickness = 3.0

rod_diameter = 6.0
rod_length = 12.0

# Create the rectangular plate
result = cq.Workplane("XY").box(plate_width, plate_length, plate_thickness)

# Create the cylindrical component
cylinder = cq.Workplane("XY").box(cylinder_diameter, cylinder_diameter, cylinder_height)
cylinder = cylinder.translate((0, 0, plate_thickness + cylinder_height/2))

# Position the cylinder on the plate
result = result.union(cylinder)

# Create the handle protrusion
handle = cq.Workplane("XY").box(handle_width, handle_length, handle_thickness)
handle = handle.translate((cylinder_diameter/2 + handle_width/2, 0, plate_thickness + cylinder_height/2))

# Add the handle to the assembly
result = result.union(handle)

# Create the connecting rod
rod = cq.Workplane("XY").cylinder(rod_length, rod_diameter/2)
rod = rod.translate((0, 0, plate_thickness + cylinder_height/2))

# Add the rod to the assembly
result = result.union(rod)

# Create the pivot/bushing
bushing = cq.Workplane("XY").cylinder(3.0, rod_diameter/2 + 1.0)
bushing = bushing.translate((0, 0, plate_thickness + cylinder_height/2 - 1.5))

# Add the bushing to the assembly
result = result.union(bushing)

# Add holes for mounting
result = result.faces(">Z").workplane().pushPoints([(-plate_width/2 + 10, -plate_length/2 + 10), 
                                                    (plate_width/2 - 10, -plate_length/2 + 10)]).hole(3.0)

# Add a hole for the handle
result = result.faces("<Y").workplane().center(cylinder_diameter/2 + handle_width/2, 0).hole(2.0)

# Add a hole for the rod
result = result.faces(">Z").workplane().center(0, 0).hole(rod_diameter)

result = result