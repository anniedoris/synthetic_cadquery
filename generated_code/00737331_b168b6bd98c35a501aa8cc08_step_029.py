import cadquery as cq

# Define dimensions
platform_length = 100.0
platform_width = 60.0
platform_height = 10.0

counterweight_diameter = 30.0
counterweight_height = 20.0

support_width = 20.0
support_height = 60.0
support_depth = 20.0

beam_length = 80.0
beam_width = 15.0
beam_height = 15.0

# Create the base platform
result = cq.Workplane("XY").box(platform_length, platform_width, platform_height)

# Add the counterweight on top of the platform
result = (
    result.faces(">Z")
    .workplane()
    .circle(counterweight_diameter / 2)
    .extrude(counterweight_height)
)

# Add the vertical support structure at one end of the platform
result = (
    result.faces("<X")
    .workplane(offset=platform_height)
    .box(support_width, support_depth, support_height)
)

# Add the horizontal beam extending from the support
result = (
    result.faces(">Y")
    .workplane(offset=support_height)
    .box(beam_length, beam_width, beam_height)
)

# Add the smaller perpendicular beam at the end of the horizontal beam
result = (
    result.faces(">X")
    .workplane(offset=beam_height)
    .box(beam_width, 15.0, 20.0)
)

# The result variable now contains the complete counterbalance mechanism