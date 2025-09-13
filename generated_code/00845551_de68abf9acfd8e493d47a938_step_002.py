import cadquery as cq

# Parameters for the elbow fittings
pipe_diameter = 20.0
wall_thickness = 2.0
elbow_radius = 10.0  # Radius of the elbow curve
curved_elbow_radius = 20.0  # Larger radius for curved elbow

# Create the 90-degree elbow
# Start with a workplane at the bottom face
elbow_90 = cq.Workplane("XY")

# Create the first cylindrical section (horizontal)
elbow_90 = elbow_90.box(pipe_diameter, pipe_diameter, elbow_radius)

# Create the curved section (quarter circle)
# Move to the end of the first cylinder and create the elbow curve
elbow_90 = elbow_90.faces(">Z").workplane(offset=elbow_radius).circle(elbow_radius).extrude(pipe_diameter)

# Create the second cylindrical section (vertical)
elbow_90 = elbow_90.faces(">Y").workplane(offset=pipe_diameter).box(pipe_diameter, pipe_diameter, elbow_radius)

# Create the curved elbow (45-degree or long-radius elbow)
# This will be a larger radius curve for smoother flow
curved_elbow = cq.Workplane("XY")

# Create the first cylindrical section (horizontal)
curved_elbow = curved_elbow.box(pipe_diameter, pipe_diameter, curved_elbow_radius)

# Create the curved section with larger radius
# For a smoother transition, we'll create a quarter-circle arc with larger radius
curved_elbow = curved_elbow.faces(">Z").workplane(offset=curved_elbow_radius).circle(curved_elbow_radius).extrude(pipe_diameter)

# Create the second cylindrical section (vertical)
curved_elbow = curved_elbow.faces(">Y").workplane(offset=pipe_diameter).box(pipe_diameter, pipe_diameter, curved_elbow_radius)

# Create a compound object with both elbows
result = elbow_90.translate((-50, 0, 0)).union(curved_elbow.translate((50, 0, 0)))

# Or create a simpler version with just the 90-degree elbow for clarity
# Create a more realistic 90-degree elbow with proper pipe connections
elbow_90_simple = cq.Workplane("XY").box(20, 20, 20)  # Base

# Create the curved section by cutting a quarter cylinder
elbow_90_simple = (
    elbow_90_simple
    .faces(">Z")
    .workplane()
    .circle(10)
    .extrude(20)
    .faces(">Y")
    .workplane()
    .circle(10)
    .extrude(20)
)

# Create a curved elbow with larger radius
curved_elbow_simple = cq.Workplane("XY").box(20, 20, 40)  # Base

# Create the curved section by cutting a quarter cylinder with larger radius
curved_elbow_simple = (
    curved_elbow_simple
    .faces(">Z")
    .workplane()
    .circle(20)
    .extrude(20)
    .faces(">Y")
    .workplane()
    .circle(20)
    .extrude(20)
)

# Create compound object with both elbows
result = elbow_90_simple.translate((-30, 0, 0)).union(curved_elbow_simple.translate((30, 0, 0)))