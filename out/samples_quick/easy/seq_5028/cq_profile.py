# Auto-generated CadQuery profile for seq 5028 (easy)
# Open this file in cq-editor. Set EXTRUDE=True to create a STEP.
import cadquery as cq

EXTRUDE = False
HEIGHT  = 5.0

def build_profile() -> cq.Workplane:
    wp = cq.Workplane("XY")
    # TODO: complex/unsupported profile; edit by hand
    return wp

if __name__ == "__main__":
    wp = build_profile()
    if EXTRUDE:
        solid = wp.extrude(HEIGHT)
        cq.exporters.export(solid, "part.step")
