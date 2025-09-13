import cadquery as cq

# Dimensions
body_length = 100.0
body_width = 30.0
body_height = 25.0
nozzle_diameter = 8.0
nozzle_length = 15.0
trigger_width = 20.0
trigger_height = 15.0
trigger_depth = 10.0
handle_diameter = 25.0
handle_length = 40.0
stand_width = 20.0
stand_height = 10.0
stand_depth = 15.0
rear_diameter = 12.0
rear_length = 20.0

# Create the main body
body = cq.Workplane("XY").box(body_length, body_width, body_height)

# Create the taper towards the nozzle end
body = body.faces(">Z").workplane().rect(body_length * 0.8, body_width * 0.9).extrude(body_height * 0.2)

# Create the nozzle
nozzle = cq.Workplane("XY").moveTo(body_length/2, 0).circle(nozzle_diameter/2).extrude(nozzle_length)
nozzle = nozzle.faces(">Z").workplane().circle(nozzle_diameter/3).extrude(nozzle_length/3)

# Create the trigger
trigger = cq.Workplane("XY").moveTo(-body_length/2 + 10, -body_width/2).rect(trigger_width, trigger_height).extrude(trigger_depth)
trigger = trigger.faces("<Z").workplane().circle(trigger_height/2).extrude(trigger_depth/2)

# Create the handle
handle = cq.Workplane("XY").moveTo(-body_length/2 - handle_length/2, 0).circle(handle_diameter/2).extrude(handle_length)
handle = handle.faces(">Z").workplane().circle(handle_diameter/3).extrude(handle_length/3)

# Create the support stand
stand = cq.Workplane("XY").moveTo(body_length/2 - stand_width/2, -body_width/2).rect(stand_width, stand_height).extrude(stand_depth)
stand = stand.faces("<Z").workplane().rect(stand_width * 0.8, stand_height * 0.8).extrude(stand_depth/2)

# Create the rear end
rear = cq.Workplane("XY").moveTo(-body_length/2 - rear_length/2, 0).circle(rear_diameter/2).extrude(rear_length)

# Combine all parts
result = body.union(nozzle).union(trigger).union(handle).union(stand).union(rear)

# Add the label text
result = (
    result.faces(">Z")
    .workplane()
    .text("Glue Gun", 6, -1, halign="center", valign="center")
)

# Add some detail to the body with a small rectangle for a power port
result = (
    result.faces("<X")
    .workplane()
    .rect(8, 4)
    .extrude(-2)
)