import cadquery as cq

# Define dimensions
length = 4.0   # length of the front face
width = 3.0    # width of the front face  
height = 2.0   # height of the object

# Create a rectangular prism
result = cq.Workplane("front").box(length, width, height)