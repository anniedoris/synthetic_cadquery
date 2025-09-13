import cadquery as cq

# Cabinet dimensions
cabinet_width = 40.0
cabinet_depth = 30.0
cabinet_height = 25.0

# Top compartment dimensions
top_width = cabinet_width
top_depth = cabinet_depth + 2.0  # Overhang
top_height = 2.0

# Compartment dimensions
compartment_width = top_width / 2.0
compartment_depth = top_depth
compartment_height = top_height

# Create the main cabinet body
cabinet = cq.Workplane("XY").box(cabinet_width, cabinet_depth, cabinet_height)

# Create the top section with overhang
top_section = cq.Workplane("XY").box(top_width, top_depth, top_height)
top_section = top_section.translate((0, 0, cabinet_height))

# Create the compartments on the top
compartment1 = cq.Workplane("XY").box(compartment_width, compartment_depth, compartment_height)
compartment1 = compartment1.translate((-(top_width/4.0), 0, cabinet_height))

compartment2 = cq.Workplane("XY").box(compartment_width, compartment_depth, compartment_height)
compartment2 = compartment2.translate((top_width/4.0, 0, cabinet_height))

# Combine all parts
result = cabinet.union(top_section).union(compartment1).union(compartment2)

# Add some subtle edge fillets for a more finished look
result = result.edges("|Z").fillet(0.5)