import cadquery as cq

# Define dimensions
sphere_radius = 20.0
band_width = 2.0
band_height = 1.0
protrusion_radius = 2.5
protrusion_height = 1.5

# Create the base sphere
result = cq.Workplane("XY").sphere(sphere_radius)

# Create the horizontal band
# The band is a cylinder that intersects the sphere
band_cylinder = (
    cq.Workplane("XY")
    .circle(sphere_radius - band_width/2)
    .extrude(band_height)
    .translate((0, 0, 0))  # Position at the equator
)

# Create a box to cut the band from the sphere
band_cut_box = (
    cq.Workplane("XY")
    .box(sphere_radius * 2, sphere_radius * 2, band_height, centered=True)
    .translate((0, 0, 0))
)

# Position the band at the equator
band_position = cq.Workplane("XY").box(sphere_radius * 2, sphere_radius * 2, band_height, centered=True).translate((0, 0, 0))

# Create the horizontal band by cutting the sphere
# We'll create a ring that sits on the sphere's equator
band = (
    cq.Workplane("XY")
    .circle(sphere_radius)
    .extrude(band_height)
    .translate((0, 0, 0))
)

# Create a second circle to define the inner part of the band
inner_circle = (
    cq.Workplane("XY")
    .circle(sphere_radius - band_width)
    .extrude(band_height)
    .translate((0, 0, 0))
)

# Subtract to create the band
band = band.cut(inner_circle)

# Position the band on the sphere
band = band.translate((0, 0, 0))

# Create the circular protrusion on the band
# First create a cylinder for the protrusion
protrusion = (
    cq.Workplane("XY")
    .circle(protrusion_radius)
    .extrude(protrusion_height)
    .translate((0, 0, 0))  # This will be adjusted later
)

# Position the protrusion on the band
# Place it at the top of the band
protrusion = protrusion.translate((0, 0, sphere_radius - band_height/2 + protrusion_height/2))

# Now we need to properly create the spherical band and the protrusion
# Let's create it differently using a more precise approach

# Create base sphere
result = cq.Workplane("XY").sphere(sphere_radius)

# Create the horizontal band by cutting a ring from the sphere
# We'll create a cylindrical cut at the equator
band_cut = (
    cq.Workplane("XY")
    .circle(sphere_radius - band_width/2)
    .extrude(band_height)
    .translate((0, 0, 0))
)

# Create a box to define where to cut the band
band_cut_box = (
    cq.Workplane("XY")
    .box(sphere_radius * 2, sphere_radius * 2, band_height, centered=True)
    .translate((0, 0, 0))
)

# Create a more precise band by subtracting a cylinder
# Create a cylinder with a hole for the band
band_cylinder = (
    cq.Workplane("XY")
    .circle(sphere_radius)
    .extrude(band_height)
)

# Create a smaller circle to subtract from the band
inner_cylinder = (
    cq.Workplane("XY")
    .circle(sphere_radius - band_width)
    .extrude(band_height)
)

# Create the actual band
band = band_cylinder.cut(inner_cylinder)

# Position the band at the equator of the sphere
band = band.translate((0, 0, 0))

# Create the circular protrusion
protrusion = (
    cq.Workplane("XY")
    .circle(protrusion_radius)
    .extrude(protrusion_height)
)

# Position the protrusion at the top of the band
protrusion = protrusion.translate((0, 0, sphere_radius - band_height/2 + protrusion_height/2))

# Add the protrusion to the result
result = result.union(protrusion)

# Adjust the band to be cut into the sphere
# Create the sphere with the band cut in
result = cq.Workplane("XY").sphere(sphere_radius)

# Create a separate workplane to add the band
band = (
    cq.Workplane("XY")
    .circle(sphere_radius)
    .extrude(band_height)
    .translate((0, 0, 0))
)

# Create the inner hole
inner_band = (
    cq.Workplane("XY")
    .circle(sphere_radius - band_width)
    .extrude(band_height)
    .translate((0, 0, 0))
)

# Cut the band from the sphere
band_cut = band.cut(inner_band)
band_cut = band_cut.translate((0, 0, 0))

# Cut the band from the sphere
# Let's use a different approach
# Create a thin ring around the sphere to represent the band
band_ring = (
    cq.Workplane("XY")
    .circle(sphere_radius)
    .circle(sphere_radius - band_width)
    .extrude(band_height)
    .translate((0, 0, 0))
)

# Adjust to position the band correctly on the sphere
# The band should be at the equator, so we adjust the Z position
band_position = band_ring.translate((0, 0, 0))

# Now create the final object with both features
result = cq.Workplane("XY").sphere(sphere_radius)

# Add the band using a different approach - create it separately and then union
band_cylinder = (
    cq.Workplane("XY")
    .circle(sphere_radius)
    .extrude(band_height)
)

# Create a smaller circle to subtract and form the ring
inner_cylinder = (
    cq.Workplane("XY")
    .circle(sphere_radius - band_width)
    .extrude(band_height)
)

# Cut to make the ring
band_ring = band_cylinder.cut(inner_cylinder)

# Position the band on the equator
band_ring = band_ring.translate((0, 0, 0))

# Create a proper band at the equator
# Create a ring that sits on the sphere's surface
# Create a band that sits on the equator
band_height_offset = sphere_radius - band_height/2
band_position = cq.Workplane("XY").box(sphere_radius*2, sphere_radius*2, band_height, centered=True).translate((0, 0, band_height_offset))

# Create the actual object
result = cq.Workplane("XY").sphere(sphere_radius)

# Create the horizontal band as a ring
band = cq.Workplane("XY").circle(sphere_radius).extrude(band_height)
inner_band = cq.Workplane("XY").circle(sphere_radius - band_width).extrude(band_height)
band = band.cut(inner_band)

# Position the band at the equator
band = band.translate((0, 0, 0))

# Add the band to the sphere
result = result.union(band)

# Create the circular protrusion
protrusion = cq.Workplane("XY").circle(protrusion_radius).extrude(protrusion_height)
protrusion = protrusion.translate((0, 0, sphere_radius - band_height/2 + protrusion_height/2))

# Add the protrusion to the sphere
result = result.union(protrusion)

# Let's use a more accurate approach
result = cq.Workplane("XY").sphere(sphere_radius)

# Create a horizontal band around the sphere
# Create a cylinder and position it at the equator
band = (
    cq.Workplane("XY")
    .circle(sphere_radius)
    .extrude(band_height)
    .translate((0, 0, 0))
)

# Create the inner hole for the band
inner_band = (
    cq.Workplane("XY")
    .circle(sphere_radius - band_width)
    .extrude(band_height)
    .translate((0, 0, 0))
)

# Subtract to make the ring
band_ring = band.cut(inner_band)

# Position the band properly
# Calculate the correct position to put the band at the equator
band_position = sphere_radius - band_height/2
band_ring = band_ring.translate((0, 0, band_position))

# Add the band to the sphere
result = result.union(band_ring)

# Add the circular protrusion
protrusion = (
    cq.Workplane("XY")
    .circle(protrusion_radius)
    .extrude(protrusion_height)
    .translate((0, 0, sphere_radius - band_height/2 + protrusion_height/2))
)

result = result.union(protrusion)