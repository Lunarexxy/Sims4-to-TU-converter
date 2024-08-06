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
        # User selects the rig (obj = context.active_object)
        # User inputs the model's age and gender (figure out how to make a dropdown menu for this)
        # User presses an "Auto Rig" button that activates this function.
        # Script checks if the Tower Unite Suite is installed, and cancels with an error message if it isn't.
        # Script gets a reference to the rig and the child mesh(es) (Object.children)
        # Script poses the rig based on pre-defined values that differ by model age and gender. (defined in Sims4_Char_Transformations.py - bpy.ops.transform.rotate)
        # Script applies the Armature modifier on each child mesh (bpy.ops.object.modifier_apply(modifier='Armature')
        # Script deletes the rig (bpy.ops.object.delete())
        # Script scales each child mesh based on pre-defined values, which may differ by model age and gender. (bpy.ops.transform.resize())
        # Script applies the scale. (bpy.ops.object.transform_apply(scale=True))
        # Script optionally adds the normal map from the same directory as the diffuse map. (OPTIONAL: this is a nice-to-have but not crucial so i'm leaving it for now)
        # Script spawns the Tower Unite Armature, with the right arm height.
        # Script adds Armature modifier to each child mesh and points it to the TU Armature
        # Script calls object.sims4_fix_vertex_groups on each child mesh.
        # User manually fixes some weighting under the chin, if they want.
        # User exports the model.

# TODO: I haven't received any characters like this to test on. May be the same as adult, not sure.
Female_Elder = []
Male_Elder = []

Female_Adult = [
{"transform_type":"rotate", "bone_name":"b__R_UpperArm__", "axis":"GLOBAL", "X":0.0, "Y":0.0, "Z":-5.0},
{"transform_type":"rotate", "bone_name":"b__L_UpperArm__", "axis":"GLOBAL", "X":0.0, "Y":0.0, "Z":5.0},

{"transform_type":"rotate", "bone_name":"b__R_Thigh__", "axis":"GLOBAL", "X":0.0, "Y":-1.5, "Z":0.0},
{"transform_type":"rotate", "bone_name":"b__L_Thigh__", "axis":"GLOBAL", "X":0.0, "Y":1.5, "Z":0.0},

{"transform_type":"rotate", "bone_name":"b__R_Foot__", "axis":"GLOBAL", "X":0.0, "Y":1.5, "Z":5.0},
{"transform_type":"rotate", "bone_name":"b__L_Foot__", "axis":"GLOBAL", "X":0.0, "Y":-1.5, "Z":5.0},

# Rotating the feet and thighs closer together has pushed the feet into the ground slightly.
# This nudges them back up. It should be pretty much imperceptible either way, though.
# This might need to be done after scaling...
{"transform_type":"move", "bone_name":"b__R_Foot__", "axis":"GLOBAL", "X":0.0, "Y":0.0, "Z":0.062},
{"transform_type":"move", "bone_name":"b__L_Foot__", "axis":"GLOBAL", "X":0.0, "Y":0.0, "Z":0.062},

{"transform_type":"rotate", "bone_name":"b__R_Pinky0__", "axis":"LOCAL", "X":0.0, "Y":0.0, "Z":15.0},
{"transform_type":"rotate", "bone_name":"b__L_Pinky0__", "axis":"LOCAL", "X":0.0, "Y":0.0, "Z":15.0},
{"transform_type":"rotate", "bone_name":"b__R_Pinky0__", "axis":"LOCAL", "X":0.0, "Y":10.0, "Z":0.0},
{"transform_type":"rotate", "bone_name":"b__L_Pinky0__", "axis":"LOCAL", "X":0.0, "Y":-10.0, "Z":0.0},

{"transform_type":"rotate", "bone_name":"b__R_Ring0__", "axis":"LOCAL", "X":0.0, "Y":0.0, "Z":13.0},
{"transform_type":"rotate", "bone_name":"b__L_Ring0__", "axis":"LOCAL", "X":0.0, "Y":0.0, "Z":13.0},
{"transform_type":"rotate", "bone_name":"b__R_Ring0__", "axis":"LOCAL", "X":0.0, "Y":3.0, "Z":0.0},
{"transform_type":"rotate", "bone_name":"b__L_Ring0__", "axis":"LOCAL", "X":0.0, "Y":-3.0, "Z":0.0},

{"transform_type":"rotate", "bone_name":"b__R_Mid0__", "axis":"LOCAL", "X":0.0, "Y":0.0, "Z":13.0},
{"transform_type":"rotate", "bone_name":"b__L_Mid0__", "axis":"LOCAL", "X":0.0, "Y":0.0, "Z":13.0},

{"transform_type":"rotate", "bone_name":"b__R_Index0__", "axis":"LOCAL", "X":0.0, "Y":0.0, "Z":14.0},
{"transform_type":"rotate", "bone_name":"b__L_Index0__", "axis":"LOCAL", "X":0.0, "Y":0.0, "Z":14.0},

{"transform_type":"rotate", "bone_name":"b__R_Thumb1__", "axis":"LOCAL", "X":0.0, "Y":0.0, "Z":10.0},
{"transform_type":"rotate", "bone_name":"b__L_Thumb1__", "axis":"LOCAL", "X":0.0, "Y":0.0, "Z":10.0},

{"transform_type":"rotate", "bone_name":"b__R_Thumb2__", "axis":"LOCAL", "X":0.0, "Y":0.0, "Z":15.0},
{"transform_type":"rotate", "bone_name":"b__L_Thumb2__", "axis":"LOCAL", "X":0.0, "Y":0.0, "Z":15.0},

{"transform_type":"apply_pose"},
{"transform_type":"delete_armature"},

{"transform_type":"scale_mesh", "axis":"GLOBAL", "X":112.0, "Y":112.0, "Z":112.0},

# Admittedly I don't know the precise percentage here, but there's a sweet spot I usually reach
# with the slider that works best with the values above. Consider it a TODO: needs tweaking.
{"transform_type":"spawn_tu_rig", "arms_raised_percent":50.8475},
{"transform_type":"fix_vertex_groups"}
]

# TODO: I haven't found the right values for male models yet. might be able to copy over most of the female instructions. I think their scale was 110, though.
Male_Adult = []

# TODO: I haven't received any characters like this to test on.
Female_Young_Adult = []
Male_Young_Adult = []

# TODO: I haven't received any characters like this to test on.
Female_Teen = []
Male_Teen = []

# TODO: I haven't received any characters like this to test on.
Female_Child = []
Female_Child = []