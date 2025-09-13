import cadquery as cq

#####
# Lego Brick Constants-- these make a Lego brick a Lego :)
######
pitch = 8.0
clearance = 0.1
bumpDiam = 4.8
bumpHeight = 1.8
height = 9.6  # thick Lego brick

t = (pitch - (2 * clearance) - bumpDiam) / 2.0
postDiam = pitch - t  # works out to 6.5
total_length = 4 * pitch - 2.0 * clearance  # 4 bumps wide
total_width = 2 * pitch - 2.0 * clearance  # 2 bumps long

# make the base
s = cq.Workplane("XY").box(total_length, total_width, height)

# shell inwards not outwards to create the hollow interior
s = s.faces("<Z").shell(-1.0 * t)

# make the bumps on the top
s = (
    s.faces(">Z")
    .workplane()
    .rarray(pitch, pitch, 4, 2, True)  # 4 bumps wide, 2 bumps long
    .circle(bumpDiam / 2.0)
    .extrude(bumpHeight)
)

# add hollow centers to the bumps
s = (
    s.faces(">Z")
    .workplane()
    .rarray(pitch, pitch, 4, 2, True)
    .circle(bumpDiam / 2.0 - 1.0)  # smaller circle for hollow center
    .extrude(bumpHeight - 0.5)  # extrude partially to create hollow
)

# chamfer the edges
s = s.edges("|Z").chamfer(0.5)

result = s