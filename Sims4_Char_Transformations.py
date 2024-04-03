# This is a list of transformations that need to be performed on the sim, depending on the type of character.
# These transformations are done in order to align the character's pose with the Tower Unite Armature's pose.
# They are performed in order, so feel free to experiment with values that work better for you.
#
# Some of these transformations are performed on the armature, but a few affect the mesh itself.
# The different transform types are "move", "rotate", "scale_mesh", "apply_pose", "delete_armature", "spawn_tu_rig", "fix_vertex_groups".
#
# "move" and "rotate" both act on the armature's current pose.
# "move", "rotate", and "scale_mesh" all require an axis, either set to "global" or "local". They also require x, y, and z values to be set to numerical values.
# "move" and "rotate" require a "bone_name", which is the name of the bone to modify.
# "scale_mesh" scales each mesh. Right after scaling, the scale is applied.
# "apply_pose" will apply the current Armature modifier, locking in its pose.
# "delete_armature" deletes the original armature tracked by the Auto Rig system, and does nothing if it's already been deleted.
# "spawn_tu_rig" will spawn the TU Armature and create a modifier on each mesh that's linked to it. It needs an "arms_raised_percent" that's set to 0.0-100.0.

    # The preferred setup would be:
    # User selects the rig and clicks an "Auto Rig" button.
    # Script gets a reference to the rig and the child mesh(es)
    # Script poses the rig based on pre-defined values, which may differ by model age and gender.
    # Script applies the Armature modifier on each child mesh
    # Script deletes the rig
    # Script scales each child mesh based on pre-defined values, which may differ by model age and gender.
    # Script applies the scale.
    # Script spawns the Tower Unite Armature, if possible, and if the addon is installed, with the right arm height (may also differ by model age and gender)
    # Script adds Armature modifier to each child mesh and points it to the TU Armature
    # Script calls object.sims4_fix_vertex_groups on each child mesh.
    # User exports the model.

# TODO: I haven't received any characters like this to test on. May be the same as adult, not sure.
Sims4Char_Female_Elder = []
Sims4Char_Male_Elder = []

Sims4Char_Female_Adult = [
{transform_type:"rotate", bone_name:"b__R_UpperArm__", axis:"global", x:0.0, y:0.0, z:-5.0},
{transform_type:"rotate", bone_name:"b__L_UpperArm__", axis:"global", x:0.0, y:0.0, z:5.0},

{transform_type:"rotate", bone_name:"b__R_Thigh__", axis:"global", x:0.0, y:-1.5, z:0.0},
{transform_type:"rotate", bone_name:"b__L_Thigh__", axis:"global", x:0.0, y:1.5, z:0.0},

{transform_type:"rotate", bone_name:"b__R_Foot__", axis:"global", x:0.0, y:1.5, z:5.0},
{transform_type:"rotate", bone_name:"b__L_Foot__", axis:"global", x:0.0, y:-1.5, z:5.0},
# Rotating the feet and thighs has pushed the feet into the ground slightly. This nudges them back up. It should pretty much imperceptible either way, though.
{transform_type:"move", bone_name:"b__R_Foot__", axis:"global", x:0.0, y:0.0, z:0.062},
{transform_type:"move", bone_name:"b__L_Foot__", axis:"global", x:0.0, y:0.0, z:0.062},

{transform_type:"rotate", bone_name:"b__R_Pinky0__", axis:"local", x:0.0, y:0.0, z:15.0},
{transform_type:"rotate", bone_name:"b__L_Pinky0__", axis:"local", x:0.0, y:0.0, z:15.0},
{transform_type:"rotate", bone_name:"b__R_Pinky0__", axis:"local", x:0.0, y:10.0, z:0.0},
{transform_type:"rotate", bone_name:"b__L_Pinky0__", axis:"local", x:0.0, y:-10.0, z:0.0},

{transform_type:"rotate", bone_name:"b__R_Ring0__", axis:"local", x:0.0, y:0.0, z:13.0},
{transform_type:"rotate", bone_name:"b__L_Ring0__", axis:"local", x:0.0, y:0.0, z:13.0},
{transform_type:"rotate", bone_name:"b__R_Ring0__", axis:"local", x:0.0, y:3.0, z:0.0},
{transform_type:"rotate", bone_name:"b__L_Ring0__", axis:"local", x:0.0, y:-3.0, z:0.0},

{transform_type:"rotate", bone_name:"b__R_Mid0__", axis:"local", x:0.0, y:0.0, z:13.0},
{transform_type:"rotate", bone_name:"b__L_Mid0__", axis:"local", x:0.0, y:0.0, z:13.0},

{transform_type:"rotate", bone_name:"b__R_Index0__", axis:"local", x:0.0, y:0.0, z:14.0},
{transform_type:"rotate", bone_name:"b__L_Index0__", axis:"local", x:0.0, y:0.0, z:14.0},

{transform_type:"rotate", bone_name:"b__R_Thumb1__", axis:"local", x:0.0, y:0.0, z:10.0},
{transform_type:"rotate", bone_name:"b__L_Thumb1__", axis:"local", x:0.0, y:0.0, z:10.0},

{transform_type:"rotate", bone_name:"b__R_Thumb2__", axis:"local", x:0.0, y:0.0, z:15.0},
{transform_type:"rotate", bone_name:"b__L_Thumb2__", axis:"local", x:0.0, y:0.0, z:15.0},

{transform_type:"apply_pose"},
{transform_type:"delete_armature"},

{transform_type:"scale_mesh", axis:"global", x:112.0, y:112.0, z:112.0},
{transform_type:"apply_scale"},
{transform_type:"spawn_tu_rig", arms_raised_percent:51.5}, # Admittedly I don't know the precise percentage, but there's a sweet spot I usually reach with the slider that works best with these values. Consider it a TODO: needs tweaking.
{transform_type:"fix_vertex_groups"}

]

# TODO: I haven't found the right values for male models yet. might be able to copy over most of the female instructions. I think their scale was 110, though.
Sims4Char_Male_Adult = []

# TODO: I haven't received any characters like this to test on.
Sims4Char_Female_Young_Adult = []
Sims4Char_Male_Young_Adult = []

# TODO: I haven't received any characters like this to test on.
Sims4Char_Female_Teen = []
Sims4Char_Male_Teen = []

# TODO: I haven't received any characters like this to test on.
Sims4Char_Female_Child = []
Sims4Char_Female_Child = []