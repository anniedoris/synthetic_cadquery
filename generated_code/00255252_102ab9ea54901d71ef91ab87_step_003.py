import cadquery as cq

# Create four cylinders with different dimensions and positions
result = (
    cq.Workplane("XY")
    # Tall cylinder in the center
    .center(0, 0)
    .circle(2.0)
    .extrude(8.0)
    # Short cylinder in foreground (smaller diameter)
    .center(-8, -4)
    .circle(1.0)
    .extrude(3.0)
    # Intermediate cylinder (shorter and wider)
    .center(6, 3)
    .circle(2.5)
    .extrude(5.0)
    # Intermediate cylinder (taller and narrower)
    .center(4, -6)
    .circle(1.5)
    .extrude(7.0)
)