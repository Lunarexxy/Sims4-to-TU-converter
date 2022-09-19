bl_info = {
    "name": "Sims4 to Tower Unite Converter",
    "blender": (2, 80, 0),
    "category": "Object",
    "author": "Lunarexxy"
}

import bpy


# If you seek to modify this script to automate renaming/merging vertex groups,
# then you'll want to modify the rename_list variable, and a chunk of calls to
# self.merge_groups() located in the execute() function.
#
# The reason merge_list isn't used for that is because Blender kept crashing.
# No clue why.


class OBJECT_OT_Sims4Importer(bpy.types.Operator):
    """Run this to make the model compatible with the Tower Unite Armature"""
    bl_idname = "object.sims4_fix_vertex_groups" # some unique internal id - can be called from console
    bl_label = "Fix Vertex Groups" # should be what's shown in the f3 menu
    bl_options = {'REGISTER', 'UNDO'} # apparently makes it work with the undo system
    
    # Vertex groups to be renamed, to match the names that Tower Unite expects.
    rename_list = [
    ["b__Head__","head"],
    ["b__Neck__","neck_01"],
    ["b__Pelvis__", "pelvis"],
    ["b__Spine0__", "spine_01"],
    ["b__Spine1__", "spine_02"],
    ["b__Spine2__", "spine_03"],
    ["b__L_Clavicle__", "clavicle_l"], #arms
    ["b__R_Clavicle__", "clavicle_r"],
    ["b__L_UpperArm__", "upperarm_l"],
    ["b__R_UpperArm__", "upperarm_r"],
    ["b__L_Forearm__", "lowerarm_l"],
    ["b__R_Forearm__", "lowerarm_r"],
    ["b__L_Hand__", "hand_l"],
    ["b__R_Hand__", "hand_r"],
    ["b__L_Thigh__", "thigh_l"], # legs
    ["b__R_Thigh__", "thigh_r"],
    ["b__L_Calf__", "calf_l"],
    ["b__R_Calf__", "calf_r"],
    ["b__L_Foot__", "foot_l"],
    ["b__R_Foot__", "foot_r"],
    ["b__L_Toe__", "ball_l"],
    ["b__R_Toe__", "ball_r"],
    ["b__L_Thumb0__", "thumb_01_l"], # fingers
    ["b__L_Index0__", "index_01_l"],
    ["b__L_Mid0__", "middle_01_l"],
    ["b__L_Ring0__", "ring_01_l"],
    ["b__L_Pinky0__", "pinky_01_l"],
    ["b__L_Thumb1__", "thumb_02_l"],
    ["b__L_Index1__", "index_02_l"],
    ["b__L_Mid1__", "middle_02_l"],
    ["b__L_Ring1__", "ring_02_l"],
    ["b__L_Pinky1__", "pinky_02_l"],
    ["b__L_Thumb2__", "thumb_03_l"],
    ["b__L_Index2__", "index_03_l"],
    ["b__L_Mid2__", "middle_03_l"],
    ["b__L_Ring2__", "ring_03_l"],
    ["b__L_Pinky2__", "pinky_03_l"],
    ["b__R_Thumb0__", "thumb_01_r"],
    ["b__R_Index0__", "index_01_r"],
    ["b__R_Mid0__", "middle_01_r"],
    ["b__R_Ring0__", "ring_01_r"],
    ["b__R_Pinky0__", "pinky_01_r"],
    ["b__R_Thumb1__", "thumb_02_r"],
    ["b__R_Index1__", "index_02_r"],
    ["b__R_Mid1__", "middle_02_r"],
    ["b__R_Ring1__", "ring_02_r"],
    ["b__R_Pinky1__", "pinky_02_r"],
    ["b__R_Thumb2__", "thumb_03_r"],
    ["b__R_Index2__", "index_03_r"],
    ["b__R_Mid2__", "middle_03_r"],
    ["b__R_Ring2__", "ring_03_r"],
    ["b__R_Pinky2__", "pinky_03_r"]
    ]
    
    # Vertex groups to be merged
    # (not actually used, but it was useful to keep as a guide)
    # (see the giant unrolled loop below, in execute(), for where to add new vertex groups that need merging)
    #merge_list = [
    #["head", "b__CAS_LowerMouthArea__"],
    #["head", "b__CAS_JawComp__"],
    #["head", "b__CAS_UpperMouthArea__"],
    #["head", "b__R_Mouth__"],
    #["head", "b__CAS_Chin__"],
    #["head", "b__L_Mouth__"],
    #["head", "b__LoLip__"],
    #["head", "b__R_LoLip__"],
    #["head", "b__L_LoLip__"],
    #["head", "b__UpLip__"],
    #["head", "b__L_UpLip__"],
    #["head", "b__R_UpLip__"],
    #["head", "b__R_Cheek__"],
    #["head", "b__Jaw__"],
    #["head", "b__L_Cheek__"],
    #["head", "b__L_Squint__"],
    #["head", "b__L_OutBrow__"],
    #["head", "b__CAS_NoseArea__"],
    #["head", "b__CAS_L_EyeScale__"],
    #["head", "b__L_LoLid__"],
    #["head", "b__CAS_L_Nostril__"],
    #["head", "b__CAS_R_Nostril__"],
    #["head", "b__CAS_NoseBridge__"],
    #["head", "b__CAS_NoseTip__"],
    #["head", "b__L_InBrow__"],
    #["head", "b__L_UpLid__"],
    #["head", "b__L_MidBrow__"],
    #["head", "b__CAS_L_EyeArea__"],
    #["head", "b__R_InBrow__"],
    #["head", "b__R_MidBrow__"],
    #["head", "b__R_OutBrow__"],
    #["head", "b__CAS_R_EyeArea__"],
    #["head", "b__CAS_R_EyeScale__"],
    #["head", "b__R_UpLid__"],
    #["head", "b__R_Squint__"],
    #["head", "b__R_LoLid__"],
    #["head", "b__R_Eye__"],
    #["head", "b__L_Eye__"],
    #["head", "b__CAS_Glasses__"],
    #["lowerarm_l", "b__L_ForearmTwist__"],
    #["lowerarm_r", "b__R_ForearmTwist__"],
    #["lowerarm_l", "b__L_Elbow__"],
    #["lowerarm_r", "b__R_Elbow__"],
    #["upperarm_l", "b__L_ShoulderTwist__"],
    #["upperarm_r", "b__R_ShoulderTwist__"],
    #["thigh_l", "b__L_ThighTwist__"],
    #["thigh_r", "b__R_ThighTwist__"],
    #["spine_02", "b__CAS_L_Breast__"],
    #["spine_02", "b__CAS_R_Breast__"]]

    # having to add "{'INFO'}, " to every print call was annoying, lol
    def debug(self, message):
        self.report({'INFO'}, message)
    
    # Merges group_b into group_a, leaving only group_a.
    def merge_groups(self, group_a_name, group_b_name):
        obj = bpy.context.active_object
        if group_a_name in obj.vertex_groups and group_b_name in obj.vertex_groups:
            # Merge
            bpy.ops.object.modifier_add(type='VERTEX_WEIGHT_MIX')
            obj.modifiers["VertexWeightMix"].mix_set = 'ALL'
            obj.modifiers["VertexWeightMix"].mix_mode = 'ADD'
            obj.modifiers["VertexWeightMix"].vertex_group_a = group_a_name
            obj.modifiers["VertexWeightMix"].vertex_group_b = group_b_name
            bpy.ops.object.modifier_apply(modifier="VertexWeightMix")
            # Delete
            bpy.ops.object.vertex_group_set_active(group=group_b_name)
            bpy.ops.object.vertex_group_remove()
        

    def execute(self, context):
        obj = context.active_object
        
        # Sanity checks
        if obj is None or obj.type != 'MESH' or obj.name == 'rig':
            self.debug("FAILED: Mesh is not selected. Make sure you didn't select the rig by accident.")
            return {'CANCELLED'}
        if len(obj.vertex_groups) == 0:
            self.debug("FAILED: Selected mesh has no vertex groups.")
            return {'CANCELLED'}
        # (since i apparently can't set the name, i have to rely on new modifiers being called "VertexWeightMix")
        if "VertexWeightMix" in obj.modifiers: 
            self.debug("FAILED: There's currently a modifier named VertexWeightMix on the model. Can't run script safely.")
            return {'CANCELLED'}

        # Replace names
        self.debug("Renaming vertex groups.")
        for group in obj.vertex_groups:
            for n in self.rename_list:
                if n[0] in obj.vertex_groups:
                    obj.vertex_groups[n[0]].name = n[1]
                    
        # Merge vertex groups (loop unrolled to fix Blender crashing with no useful error)
        self.debug("Merging extra vertex groups.")
        self.merge_groups("head", "b__CAS_LowerMouthArea__")
        self.merge_groups("head", "b__CAS_JawComp__")
        self.merge_groups("head", "b__CAS_UpperMouthArea__")
        self.merge_groups("head", "b__R_Mouth__")
        self.merge_groups("head", "b__CAS_Chin__")
        self.merge_groups("head", "b__L_Mouth__")
        self.merge_groups("head", "b__LoLip__")
        self.merge_groups("head", "b__R_LoLip__")
        self.merge_groups("head", "b__L_LoLip__")
        self.merge_groups("head", "b__UpLip__")
        self.merge_groups("head", "b__L_UpLip__")
        self.merge_groups("head", "b__R_UpLip__")
        self.merge_groups("head", "b__R_Cheek__")
        self.merge_groups("head", "b__Jaw__")
        self.merge_groups("head", "b__L_Cheek__")
        self.merge_groups("head", "b__L_Squint__")
        self.merge_groups("head", "b__L_OutBrow__")
        self.merge_groups("head", "b__CAS_NoseArea__")
        self.merge_groups("head", "b__CAS_L_EyeScale__")
        self.merge_groups("head", "b__L_LoLid__")
        self.merge_groups("head", "b__CAS_L_Nostril__")
        self.merge_groups("head", "b__CAS_R_Nostril__")
        self.merge_groups("head", "b__CAS_NoseBridge__")
        self.merge_groups("head", "b__CAS_NoseTip__")
        self.merge_groups("head", "b__L_InBrow__")
        self.merge_groups("head", "b__L_UpLid__")
        self.merge_groups("head", "b__L_MidBrow__")
        self.merge_groups("head", "b__CAS_L_EyeArea__")
        self.merge_groups("head", "b__R_InBrow__")
        self.merge_groups("head", "b__R_MidBrow__")
        self.merge_groups("head", "b__R_OutBrow__")
        self.merge_groups("head", "b__CAS_R_EyeArea__")
        self.merge_groups("head", "b__CAS_R_EyeScale__")
        self.merge_groups("head", "b__R_UpLid__")
        self.merge_groups("head", "b__R_Squint__")
        self.merge_groups("head", "b__R_LoLid__")
        self.merge_groups("head", "b__R_Eye__")
        self.merge_groups("head", "b__L_Eye__")
        self.merge_groups("head", "b__CAS_Glasses__")
        self.merge_groups("lowerarm_l", "b__L_ForearmTwist__")
        self.merge_groups("lowerarm_r", "b__R_ForearmTwist__")
        self.merge_groups("lowerarm_l", "b__L_Elbow__")
        self.merge_groups("lowerarm_r", "b__R_Elbow__")
        self.merge_groups("upperarm_l", "b__L_ShoulderTwist__")
        self.merge_groups("upperarm_r", "b__R_ShoulderTwist__")
        self.merge_groups("thigh_l", "b__L_ThighTwist__")
        self.merge_groups("thigh_r", "b__R_ThighTwist__")
        self.merge_groups("thigh_l", "b__L_Skirt__")
        self.merge_groups("thigh_r", "b__R_Skirt__")
        self.merge_groups("spine_02", "b__CAS_L_Breast__")
        self.merge_groups("spine_02", "b__CAS_R_Breast__")
                    
        
        self.report({'INFO'}, 'SUCCESS: Done!')
        return {'FINISHED'}

class VIEW3D_PT_Sims4Importer(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Sims 4'
    bl_label = 'Sims 4 to Tower Unite'
    
    def draw(self, context):
        self.layout.label(text="1: Import .dae model")
        self.layout.label(text="2: Select mesh")
        self.layout.label(text='3: Press "Fix Vertex Groups"')
        self.layout.operator('object.sims4_fix_vertex_groups', text="Fix Vertex Groups", icon="FUND")
        self.layout.label(text="4: Check for errors at")
        self.layout.label(text="the bottom of the screen")
    
    


def register():
    bpy.utils.register_class(OBJECT_OT_Sims4Importer)
    bpy.utils.register_class(VIEW3D_PT_Sims4Importer)

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_Sims4Importer)
    bpy.utils.unregister_class(VIEW3D_PT_Sims4Importer)

if __name__ == "__main__":
    register()
