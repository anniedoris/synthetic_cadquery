import cadquery as cq

# Define dimensions
cylinder_diameter = 20.0
cylinder_height = 12.0  # less than diameter
triangle_base = 8.0
triangle_height = 6.0
hole_diameter = 2.0
bar_width = 12.0
bar_height = 2.0

# Create the cylindrical base
result = cq.Workplane("XY").circle(cylinder_diameter/2).extrude(cylinder_height)

# Create the top feature
# Move to the top face
result = result.faces(">Z").workplane()

# Create the rectangular bar that spans the diameter
result = result.rect(bar_width, bar_height, forConstruction=True).vertices().center(0, bar_height/2).rect(triangle_base, triangle_height, forConstruction=True)

# Create the two triangles (isosceles)
# First triangle (left side)
result = result.moveTo(-bar_width/2, bar_height/2).lineTo(-bar_width/2 + triangle_base/2, bar_height/2 + triangle_height).lineTo(-bar_width/2 + triangle_base, bar_height/2).close()

# Second triangle (right side)
result = result.moveTo(bar_width/2, bar_height/2).lineTo(bar_width/2 - triangle_base/2, bar_height/2 + triangle_height).lineTo(bar_width/2 - triangle_base, bar_height/2).close()

# Extrude the top feature
result = result.extrude(2.0)

# Add the holes at the triangle tips
# Left hole
result = result.faces("<Z").workplane(offset=2.0).center(-bar_width/2 + triangle_base, bar_height/2 + triangle_height/2).hole(hole_diameter)

# Right hole  
result = result.faces("<Z").workplane(offset=2.0).center(bar_width/2 - triangle_base, bar_height/2 + triangle_height/2).hole(hole_diameter)

# Alternative approach - more precise construction
result = cq.Workplane("XY").circle(cylinder_diameter/2).extrude(cylinder_height)

# Create top feature using proper construction
top_face = result.faces(">Z").workplane()

# Create the bar connecting the triangles
bar = top_face.rect(bar_width, bar_height).extrude(2.0)

# Create the triangles on top of the bar
# Left triangle
left_triangle = top_face.moveTo(-bar_width/2, bar_height/2).lineTo(-bar_width/2 + triangle_base/2, bar_height/2 + triangle_height).lineTo(-bar_width/2 + triangle_base, bar_height/2).close()
left_triangle = left_triangle.extrude(2.0)

# Right triangle  
right_triangle = top_face.moveTo(bar_width/2, bar_height/2).lineTo(bar_width/2 - triangle_base/2, bar_height/2 + triangle_height).lineTo(bar_width/2 - triangle_base, bar_height/2).close()
right_triangle = right_triangle.extrude(2.0)

# Combine all elements
result = result.union(bar).union(left_triangle).union(right_triangle)

# Add holes at triangle tips
result = result.faces("<Z").workplane(offset=2.0).center(-bar_width/2 + triangle_base, bar_height/2 + triangle_height/2).hole(hole_diameter)
result = result.faces("<Z").workplane(offset=2.0).center(bar_width/2 - triangle_base, bar_height/2 + triangle_height/2).hole(hole_diameter)

# Final approach - cleaner construction
result = cq.Workplane("XY").circle(cylinder_diameter/2).extrude(cylinder_height)

# Create the top feature as a single solid
top_features = (
    cq.Workplane("XY")
    .center(0, 0)
    .rect(bar_width, bar_height)
    .extrude(2.0)
    .moveTo(-bar_width/2, bar_height/2)
    .lineTo(-bar_width/2 + triangle_base/2, bar_height/2 + triangle_height)
    .lineTo(-bar_width/2 + triangle_base, bar_height/2)
    .close()
    .extrude(2.0)
    .moveTo(bar_width/2, bar_height/2)
    .lineTo(bar_width/2 - triangle_base/2, bar_height/2 + triangle_height)
    .lineTo(bar_width/2 - triangle_base, bar_height/2)
    .close()
    .extrude(2.0)
)

result = result.union(top_features)

# Add the holes
result = (
    result.faces("<Z")
    .workplane(offset=2.0)
    .center(-bar_width/2 + triangle_base, bar_height/2 + triangle_height/2)
    .hole(hole_diameter)
    .center(2*bar_width/2 - triangle_base, bar_height/2 + triangle_height/2)
    .hole(hole_diameter)
)

# More precise approach
result = cq.Workplane("XY").circle(cylinder_diameter/2).extrude(cylinder_height)

# Create top feature using construction
# Create a workplane on top face
top_wp = result.faces(">Z").workplane()

# Create the bar that connects the triangles
bar = top_wp.rect(bar_width, bar_height).extrude(2.0)

# Create the two triangles
triangle_points = [
    (-bar_width/2, bar_height/2),  # base left
    (-bar_width/2 + triangle_base/2, bar_height/2 + triangle_height),  # tip
    (-bar_width/2 + triangle_base, bar_height/2)  # base right
]

# Left triangle
left_triangle = (
    cq.Workplane("XY")
    .moveTo(triangle_points[0][0], triangle_points[0][1])
    .lineTo(triangle_points[1][0], triangle_points[1][1])
    .lineTo(triangle_points[2][0], triangle_points[2][1])
    .close()
    .extrude(2.0)
)

# Right triangle
right_triangle = (
    cq.Workplane("XY")
    .moveTo(-triangle_points[2][0], triangle_points[0][1])
    .lineTo(-triangle_points[1][0], triangle_points[1][1])
    .lineTo(-triangle_points[0][0], triangle_points[2][1])
    .close()
    .extrude(2.0)
)

# Combine all top features
top_feature = bar.union(left_triangle).union(right_triangle)
result = result.union(top_feature)

# Add holes
result = (
    result.faces("<Z")
    .workplane(offset=2.0)
    .center(-bar_width/2 + triangle_base, bar_height/2 + triangle_height/2)
    .hole(hole_diameter)
    .center(2*bar_width/2 - triangle_base, bar_height/2 + triangle_height/2)
    .hole(hole_diameter)
)

# Cleaner final approach
result = cq.Workplane("XY").circle(cylinder_diameter/2).extrude(cylinder_height)

# Add the top feature with triangles and bar
top_wp = result.faces(">Z").workplane()

# Create the rectangular bar
bar = top_wp.rect(bar_width, bar_height).extrude(2.0)

# Create two triangles (isosceles)
# Left triangle
left_triangle = (
    top_wp.moveTo(-bar_width/2, bar_height/2)
    .lineTo(-bar_width/2 + triangle_base/2, bar_height/2 + triangle_height)
    .lineTo(-bar_width/2 + triangle_base, bar_height/2)
    .close()
    .extrude(2.0)
)

# Right triangle  
right_triangle = (
    top_wp.moveTo(bar_width/2, bar_height/2)
    .lineTo(bar_width/2 - triangle_base/2, bar_height/2 + triangle_height)
    .lineTo(bar_width/2 - triangle_base, bar_height/2)
    .close()
    .extrude(2.0)
)

# Combine all top elements
result = result.union(bar).union(left_triangle).union(right_triangle)

# Add holes at triangle tips
hole_positions = [
    (-bar_width/2 + triangle_base, bar_height/2 + triangle_height/2),
    (bar_width/2 - triangle_base, bar_height/2 + triangle_height/2)
]

for x, y in hole_positions:
    result = (
        result.faces("<Z")
        .workplane(offset=2.0)
        .center(x, y)
        .hole(hole_diameter)
    )

result = result