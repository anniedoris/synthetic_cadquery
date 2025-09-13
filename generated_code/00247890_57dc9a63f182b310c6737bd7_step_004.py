import cadquery as cq

# Define parameters for the stack of prisms
num_prisms = 10
prism_width = 10.0
prism_depth = 10.0
prism_height = 50.0
offset = 2.0

# Create the base prism
base_prism = cq.Workplane("XY").box(prism_width, prism_depth, prism_height)

# Create the stacked prisms with offset
result = base_prism

for i in range(1, num_prisms):
    # Offset each subsequent prism
    offset_x = (i % 2) * offset  # Alternate offset direction
    offset_y = (i % 2) * offset
    
    # Create a new workplane at the appropriate height
    current_height = i * prism_height
    
    # Create the offset prism
    prism = cq.Workplane("XY", origin=(offset_x, offset_y, current_height)).box(
        prism_width, prism_depth, prism_height
    )
    
    # Add it to the result
    result = result.union(prism)

# Alternative approach using a more efficient method
# result = cq.Workplane("XY")
# 
# # Create base prism
# base = cq.Workplane("XY").box(prism_width, prism_depth, prism_height)
# 
# # Stack prisms with offset
# for i in range(num_prisms):
#     offset_x = (i % 2) * offset
#     offset_y = (i % 2) * offset
#     height_offset = i * prism_height
#     
#     prism = base.translate((offset_x, offset_y, height_offset))
#     result = result.union(prism)

# Clean up the result to ensure proper solid geometry
result = result.clean()