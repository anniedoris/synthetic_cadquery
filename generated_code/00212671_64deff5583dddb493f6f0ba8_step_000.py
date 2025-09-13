import cadquery as cq

# Define dimensions
L = 100.0  # Length
W = 60.0   # Width
H = 20.0   # Height
W_h = 40.0 # Hollow width
H_h = 10.0 # Hollow height

# Create the outer rectangular prism
result = cq.Workplane("XY").box(L, W, H)

# Create the hollow section
# The hollow section should be centered in the object
# So we need to create a smaller box and cut it out
hollow_offset_x = (L - W_h) / 2
hollow_offset_y = (W - H_h) / 2

# Create the hollow section
hollow_box = cq.Workplane("XY").box(W_h, H_h, H)

# Position the hollow section in the center of the outer box
hollow_box = hollow_box.translate((0, 0, 0))  # Already centered in the XY plane

# Cut the hollow section from the outer box
result = result.cut(hollow_box)

# Alternatively, we can do it more explicitly:
# result = (
#     cq.Workplane("XY")
#     .box(L, W, H)
#     .faces(">Z")
#     .workplane()
#     .rect(W_h, H_h)
#     .cutThruAll()
# )

# Or even simpler approach:
result = (
    cq.Workplane("XY")
    .box(L, W, H)
    .faces(">Z")
    .workplane()
    .rect(W_h, H_h)
    .cutThruAll()
)