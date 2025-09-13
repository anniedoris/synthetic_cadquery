import cadquery as cq

# Define dimensions
shaft_diameter = 10.0
shaft_length = 50.0
flange_diameter = 15.0
flange_height = 5.0
cap_diameter = 12.0
cap_height = 3.0
thread_diameter = 8.0
thread_depth = 2.0
thread_pitch = 1.5

# Create the main shaft
result = cq.Workplane("XY").circle(shaft_diameter/2).extrude(shaft_length)

# Add the flange at the bottom
result = (
    result.faces("<Z")
    .workplane()
    .circle(flange_diameter/2)
    .extrude(flange_height)
)

# Add the cap at the top
result = (
    result.faces(">Z")
    .workplane()
    .circle(cap_diameter/2)
    .extrude(cap_height)
)

# Create internal threads in the flange
# We'll create a cylindrical hole for the threads
result = (
    result.faces("<Z")
    .workplane()
    .circle(thread_diameter/2)
    .extrude(thread_depth)
)

# For a more realistic thread representation, we could use a helix pattern
# But for simplicity and based on the description, the internal hole represents the threading

# The internal threads are represented by a cylindrical hole with the specified diameter
# This hole is positioned to show the threading at the interface between shaft and flange

# Since the description mentions internal threads, we'll add a simple representation
# by cutting a hole through the flange where the threads would be
result = (
    result.faces("<Z")
    .workplane()
    .circle(thread_diameter/2)
    .cutBlind(-thread_depth)
)

# The cap is a separate extrusion that sits on top of the shaft
# The final result is the complete assembly

# Position the workplane properly for the final object
result = result

# Since we're using a single workplane chain, we can finalize it with a proper reference
result = result