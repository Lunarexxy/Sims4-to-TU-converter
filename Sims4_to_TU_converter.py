# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 3
#  of the License, or any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# ##### END GPL LICENSE BLOCK #####



# If you seek to modify this script to automate renaming/merging vertex groups,
# then you'll want to modify the rename_list variable, as well as the merge_list variable.
#
# The rename list tries to create at least one version of each expected vertex group,
# while the merge list is used for merging everything that remains into those new groups.
# A fallback exists in the merge_groups function that creates any group that's missing.


bl_info = {
    "name": "Sims4 to Tower Unite Converter (S4TU)",
    "version": (1, 9),
    "blender": (2, 80, 0),
    "category": "Object",
    "author": "Lunarexxy",
    "support": "COMMUNITY"
}

import bpy

class OBJECT_OT_S4TUVertexGroupFixer(bpy.types.Operator):
    """Converts the mesh's vertex groups to match the Tower Unite Armature"""
    bl_idname = "object.s4tu_fix_vertex_groups" # some unique internal id - can be called from console
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
    merge_list = [
    ["head", "b__CAS_LowerMouthArea__"],
    ["head", "b__CAS_JawComp__"],
    ["head", "b__CAS_UpperMouthArea__"],
    ["head", "b__R_Mouth__"],
    ["head", "b__CAS_Chin__"],
    ["head", "b__L_Mouth__"],
    ["head", "b__LoLip__"],
    ["head", "b__R_LoLip__"],
    ["head", "b__L_LoLip__"],
    ["head", "b__UpLip__"],
    ["head", "b__L_UpLip__"],
    ["head", "b__R_UpLip__"],
    ["head", "b__R_Cheek__"],
    ["head", "b__Jaw__"],
    ["head", "b__L_Cheek__"],
    ["head", "b__L_Squint__"],
    ["head", "b__L_OutBrow__"],
    ["head", "b__CAS_NoseArea__"],
    ["head", "b__CAS_L_EyeScale__"],
    ["head", "b__L_LoLid__"],
    ["head", "b__CAS_L_Nostril__"],
    ["head", "b__CAS_R_Nostril__"],
    ["head", "b__CAS_NoseBridge__"],
    ["head", "b__CAS_NoseTip__"],
    ["head", "b__L_InBrow__"],
    ["head", "b__L_UpLid__"],
    ["head", "b__L_MidBrow__"],
    ["head", "b__CAS_L_EyeArea__"],
    ["head", "b__R_InBrow__"],
    ["head", "b__R_MidBrow__"],
    ["head", "b__R_OutBrow__"],
    ["head", "b__CAS_R_EyeArea__"],
    ["head", "b__CAS_R_EyeScale__"],
    ["head", "b__R_UpLid__"],
    ["head", "b__R_Squint__"],
    ["head", "b__R_LoLid__"],
    ["head", "b__R_Eye__"],
    ["head", "b__L_Eye__"],
    ["head", "b__CAS_Glasses__"],
    ["lowerarm_l", "b__L_ForearmTwist__"],
    ["lowerarm_r", "b__R_ForearmTwist__"],
    ["lowerarm_l", "b__L_Elbow__"],
    ["lowerarm_r", "b__R_Elbow__"],
    ["upperarm_l", "b__L_ShoulderTwist__"],
    ["upperarm_r", "b__R_ShoulderTwist__"],
    ["thigh_l", "b__L_ThighTwist__"],
    ["thigh_r", "b__R_ThighTwist__"],
    ["thigh_l", "b__L_Skirt__"],
    ["thigh_r", "b__R_Skirt__"],
    ["spine_02", "b__CAS_L_Breast__"],
    ["spine_02", "b__CAS_R_Breast__"]
    ]

    # having to add "{'INFO'}, " to every print call was annoying, lol
    def debug(self, message):
        self.report({'INFO'}, message)
    
    # Merges group_b into group_a, leaving only group_a.
    def merge_groups(self, group_a_name, group_b_name):
        obj = bpy.context.active_object
        if group_b_name in obj.vertex_groups:
            # If group_a doesn't exist but group_b does, create an empty group_a to merge into.
            # This can happen sometimes if a model is split into multiple meshes.
            # Example: A glasses mesh with "b__CAS_Glasses__" would try to merge into the "head" group,
            # but there was no "b__Head__" initially on the glasses mesh, so "head" was never created in the rename loop.
            if not group_a_name in obj.vertex_groups:
                obj.vertex_groups.new(name=group_a_name)
            
            # Merge group B into A.
            bpy.ops.object.modifier_add(type='VERTEX_WEIGHT_MIX')
            obj.modifiers["VertexWeightMix"].mix_set = 'OR'
            obj.modifiers["VertexWeightMix"].mix_mode = 'ADD'
            obj.modifiers["VertexWeightMix"].vertex_group_a = group_a_name
            obj.modifiers["VertexWeightMix"].vertex_group_b = group_b_name
            bpy.ops.object.modifier_apply(modifier="VertexWeightMix")
            # Delete group B.
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
            self.debug("FAILED: Can't run safely, there's a modifier named VertexWeightMix on the mesh.")
            return {'CANCELLED'}

        # Replace names
        self.debug("Renaming vertex groups.")
        for group in obj.vertex_groups:
            for n in self.rename_list:
                if n[0] in obj.vertex_groups:
                    obj.vertex_groups[n[0]].name = n[1]
                    
        # Merge vertex groups
        self.debug("Merging extra vertex groups.")
        for group in self.merge_list:
            self.merge_groups(group[0], group[1])
                    
        
        self.report({'INFO'}, 'SUCCESS: Done!')
        return {'FINISHED'}

class VIEW3D_PT_S4TUVertexGroupFixer(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'S4TU'
    bl_label = 'Fix Vertex Groups'
    
    def draw(self, context):
        obj = context.active_object

        self.layout.label(text="1: Import Sims4 model")
        self.layout.label(text="2: Select mesh")
        self.layout.label(text='3: Press "Fix Vertex Groups"')
        if not obj is None and obj.type == 'MESH':
            self.layout.operator('object.s4tu_fix_vertex_groups', text="Fix Vertex Groups", icon="FUND")
        else:
            self.layout.label(text='   (Select the mesh first!)')
        self.layout.label(text="4: Check for errors at")
        self.layout.label(text="the bottom of the screen")


class OBJECT_OT_S4TUMergeFingersIntoHands(bpy.types.Operator):
    """Merges the finger vertex groups into the hand vertex groups, for characters where you don't want the fingers to be animated."""
    bl_idname = "object.s4tu_merge_fingers_into_hands" # some unique internal id - can be called from console
    bl_label = "Merge fingers into hands" # should be what's shown in the f3 menu
    bl_options = {'REGISTER', 'UNDO'} # apparently makes it work with the undo system

    # List of all the finger bones so they can be merged into the hand, if desired.
    finger_bones_list = [
    "thumb_01",
    "thumb_02",
    "thumb_03",
    "index_01",
    "index_02",
    "index_03",
    "middle_01",
    "middle_02",
    "middle_03",
    "ring_01",
    "ring_02",
    "ring_03",
    "pinky_01",
    "pinky_02",
    "pinky_03"
    ]

    # having to add "{'INFO'}, " to every print call was annoying, lol
    def debug(self, message):
        self.report({'INFO'}, message)
    
    # Merges group_b into group_a, leaving only group_a.
    # Returns true on success, false on failure.
    def merge_groups(self, group_a_name, group_b_name):
        obj = bpy.context.active_object
        # If the hand group doesn't exist, it's likely because the user hasn't run the Fix Vertex Groups yet.
        if not group_a_name in obj.vertex_groups:
            return False
        if not group_b_name in obj.vertex_groups:
            return False
        
        # Merge group B into A.
        bpy.ops.object.modifier_add(type='VERTEX_WEIGHT_MIX')
        obj.modifiers["VertexWeightMix"].mix_set = 'OR'
        obj.modifiers["VertexWeightMix"].mix_mode = 'ADD'
        obj.modifiers["VertexWeightMix"].vertex_group_a = group_a_name
        obj.modifiers["VertexWeightMix"].vertex_group_b = group_b_name
        bpy.ops.object.modifier_apply(modifier="VertexWeightMix")
        # Delete group B.
        bpy.ops.object.vertex_group_set_active(group=group_b_name)
        bpy.ops.object.vertex_group_remove()
        return True
    
    # Merges all the finger groups into the hand groups.
    # Returns false if nothing was changed, likely because the vertex groups didn't exist.
    def merge_all_fingers(self) -> bool:
        was_anything_changed = False
        for finger in self.finger_bones_list:
            if self.merge_groups("hand_l", finger+"_l"): was_anything_changed = True
            if self.merge_groups("hand_r", finger+"_r"): was_anything_changed = True
        return was_anything_changed
    
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
            self.debug("FAILED: Can't run safely, there's a modifier named VertexWeightMix on the mesh.")
            return {'CANCELLED'}

        # Replace names
        self.debug("Merging fingers into hand.")
        was_anything_changed = self.merge_all_fingers()
        
        if not was_anything_changed:
            self.debug("FAILED: Couldn't find anything to merge.")
            return {'CANCELLED'}
        
        self.report({'INFO'}, 'SUCCESS: Done!')
        return {'FINISHED'}

class VIEW3D_PT_S4TUMergeFingersIntoHands(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'S4TU'
    bl_label = 'Merge Fingers Into Hands'

    def mesh_has_required_vertex_groups(self, mesh):
        if not "hand_l" in mesh.vertex_groups and not "hand_r" in mesh.vertex_groups:
            return False

        # yoink
        fingers = OBJECT_OT_S4TUMergeFingersIntoHands.finger_bones_list
        found_a_finger_too = False
        for finger in fingers:
            if finger+"_l" in mesh.vertex_groups:
                found_a_finger_too = True
                break
            if finger+"_r" in mesh.vertex_groups:
                found_a_finger_too = True
                break
        return found_a_finger_too
    
    def draw(self, context):
        obj = context.active_object

        self.layout.label(text="1: Import Sims4 model")
        self.layout.label(text="2: Run Fix Vertex Groups on it.")
        self.layout.label(text="3: Select mesh.")
        self.layout.label(text='4: Press "Merge"')
        if obj is None:
            self.layout.label(text='   (Select the mesh first!)')
        elif obj.type != 'MESH':
            self.layout.label(text='   (Select the mesh first!)')
        elif not self.mesh_has_required_vertex_groups(obj):
            self.layout.label(text='   (No hands or fingers to merge.')
            self.layout.label(text='   Run Fix Vertex Groups first.)')
        else:
            self.layout.operator('object.s4tu_merge_fingers_into_hands', text="Merge", icon="FUND")
        self.layout.label(text="5: Check for errors at")
        self.layout.label(text="the bottom of the screen")


def register():
    bpy.utils.register_class(OBJECT_OT_S4TUVertexGroupFixer)
    bpy.utils.register_class(VIEW3D_PT_S4TUVertexGroupFixer)

    bpy.utils.register_class(OBJECT_OT_S4TUMergeFingersIntoHands)
    bpy.utils.register_class(VIEW3D_PT_S4TUMergeFingersIntoHands)

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_S4TUVertexGroupFixer)
    bpy.utils.unregister_class(VIEW3D_PT_S4TUVertexGroupFixer)

    bpy.utils.unregister_class(OBJECT_OT_S4TUMergeFingersIntoHands)
    bpy.utils.unregister_class(VIEW3D_PT_S4TUMergeFingersIntoHands)

if __name__ == "__main__":
    register()
