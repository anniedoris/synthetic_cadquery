import cadquery as cq
from math import sin, cos, pi

# Parameters for the star-shaped object
outer_radius = 50.0
inner_radius = 30.0
core_radius = 15.0
layer_thickness = 5.0
num_points = 5
num_layers = 3

# Create the base workplane
result = cq.Workplane("XY")

# Create the outer star shape
outer_points = []
for i in range(num_points * 2):
    angle = i * pi / num_points
    radius = outer_radius if i % 2 == 0 else inner_radius
    x = radius * cos(angle)
    y = radius * sin(angle)
    outer_points.append((x, y))

# Create the outer star profile
result = result.polyline(outer_points).close()

# Extrude the outer layer
result = result.extrude(layer_thickness)

# Create inner layers
for layer in range(1, num_layers):
    # Create a smaller star for each layer
    scale_factor = 1 - (layer * 0.2)
    layer_points = []
    for i in range(num_points * 2):
        angle = i * pi / num_points
        radius = outer_radius * scale_factor if i % 2 == 0 else inner_radius * scale_factor
        x = radius * cos(angle)
        y = radius * sin(angle)
        layer_points.append((x, y))
    
    # Create the layer profile
    layer_profile = cq.Workplane("XY").polyline(layer_points).close()
    
    # Extrude the layer
    layer_extrude = layer_profile.extrude(layer_thickness)
    
    # Position the layer
    layer_extrude = layer_extrude.translate((0, 0, layer * layer_thickness))
    
    # Union with the main result
    result = result.union(layer_extrude)

# Create the central core
result = result.faces(">Z").workplane().circle(core_radius).extrude(layer_thickness)

# Create the innermost layer (pentagon)
pentagon_points = []
for i in range(5):
    angle = i * 2 * pi / 5 - pi/2
    x = core_radius * 0.8 * cos(angle)
    y = core_radius * 0.8 * sin(angle)
    pentagon_points.append((x, y))

# Create the pentagon layer
pentagon_layer = cq.Workplane("XY").polyline(pentagon_points).close().extrude(layer_thickness)
pentagon_layer = pentagon_layer.translate((0, 0, num_layers * layer_thickness))
result = result.union(pentagon_layer)

# Add fillets to edges for rounded appearance
result = result.edges("|Z").fillet(2.0)

# Create the final result
result = result