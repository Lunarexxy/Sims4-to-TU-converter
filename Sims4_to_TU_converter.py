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


bl_info = {
    "name": "Sims4 to Tower Unite Converter",
    "version": (1, 8),
    "blender": (2, 80, 0),
    "category": "Object",
    "author": "Lunarexxy",
    "support": "COMMUNITY"
}

import bpy
from math import *
from mathutils import Vector
import Sims4_Char_Transformations as SimData


class OBJECT_OT_Sims4VertexGroupFixer(bpy.types.Operator):
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
            
            # Merge
            bpy.ops.object.modifier_add(type='VERTEX_WEIGHT_MIX')
            obj.modifiers["VertexWeightMix"].mix_set = 'OR'
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
                    
        # Merge vertex groups
        self.debug("Merging extra vertex groups.")
        for group in self.merge_list:
            self.merge_groups(group[0], group[1])
                    
        
        self.report({'INFO'}, 'SUCCESS: Done!')
        return {'FINISHED'}

class VIEW3D_PT_Sims4VertexGroupFixer(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Sims 4'
    bl_label = 'S4TU - Fix Vertex Groups'
    
    def draw(self, context):
        obj = context.active_object

        self.layout.label(text="1: Import .dae model")
        self.layout.label(text="2: Select mesh")
        self.layout.label(text='3: Press "Fix Vertex Groups"')
        if not obj is None and obj.type == 'MESH':
            self.layout.operator('object.sims4_fix_vertex_groups', text="Fix Vertex Groups", icon="FUND")
        else:
            self.layout.operator('object.sims4_fix_vertex_groups', text="Select a mesh first.", icon="X")
        self.layout.label(text="4: Check for errors at")
        self.layout.label(text="the bottom of the screen")

class VIEW3D_PT_Sims4AutoRig(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Sims 4'
    bl_label = 'S4TU - Auto Rig'

    def draw(self, context):
        obj = context.active_object
        sim_properties = context.scene.sim_properties
        failed = False

        try:
            check_tu_suite_installed = context.scene.TU_Armature_Props
        except:
            failed = True
        
        if failed:
            self.layout.label(text="Auto Rig requires the")
            self.layout.label(text="Tower Unite Suite addon")
            self.layout.label(text="to be installed.")
        else:
            self.layout.label(text="1: Import .dae model")
            self.layout.label(text="2: Select Sim's gender & age")
            #self.layout.label(text=sim_properties.gender)
            self.layout.prop(sim_properties, "gender")
            self.layout.prop(sim_properties, "age")
            #self.layout.label(text=sim_properties.age)
            self.layout.label(text="3: Press Auto Rig")
            self.layout.operator('object.sims4_auto_rig', text="Auto Rig (WIP)", icon="FUND")
            self.layout.label(text="4: Check for errors at")
            self.layout.label(text="the bottom of the screen")
            

class SimProperties(bpy.types.PropertyGroup):
    gender: bpy.props.EnumProperty(
        name="Gender",
        description="The gender of the Sim",
        default="female",
        items=[("female", "Female", ""),
               ("male", "Male", "")]
    )
    age: bpy.props.EnumProperty(
        name="Age",
        description="The age of the Sim",
        default="adult",
        items=[("elder", "Elder", ""),
               ("adult", "Adult", ""),
               ("young_adult", "Young Adult", ""),
               ("teen", "Teen", ""),
               ("child", "Child", ""),]
    )

# This one's a work in progress.
# Ideally we could have a single button handle the rigging of the entire model
class OBJECT_OT_Sims4AutoRig(bpy.types.Operator):
    """Run this to automatically rig your model to the Tower Unite Armature"""
    bl_idname = "object.sims4_auto_rig" # some unique internal id - can be called from console
    bl_label = "Auto Rig" # should be what's shown in the f3 menu
    bl_options = {'REGISTER', 'UNDO'} # apparently makes it work with the undo system
    
     # having to add "{'INFO'}, " to every print call was annoying, lol
    def debug(self, message):
        self.report({'INFO'}, str(message))

    def select_bone(self, bone):
        bone.select = True
        bone.select_head = True
        bone.select_tail = True

    def get_sim_data(self, gender, age):
        match gender:
            case "male":
                match age:
                    case "elder":
                        return SimData.Male_Elder
                    case "adult":
                        return SimData.Male_Adult
                    case "young_adult":
                        return SimData.Male_Young_Adult
                    case "teen":
                        return SimData.Male_Teen
                    case "child":
                        return SimData.Male_Child
                    case _:
                        self.debug("FAILED: Invalid age")
                        return None
            case "female":
                match age:
                    case "elder":
                        return SimData.Female_Elder
                    case "adult":
                        return SimData.Female_Adult
                    case "young_adult":
                        return SimData.Female_Young_Adult
                    case "teen":
                        return SimData.Female_Teen
                    case "child":
                        return SimData.Female_Child
                    case _:
                        self.debug("FAILED: Invalid age")
                        return None
            case _:
                self.debug("FAILED: Invalid gender")
                return None

    
    def execute(self, context):
        rig = context.active_object
        sim_data = self.get_sim_data(context.scene.sim_properties.gender, context.scene.sim_properties.age)

        # Sanity checks
        if rig is None or rig.type != 'ARMATURE' or not rig.name.startswith('rig'):
            self.debug("FAILED: Armature not selected. Make sure you selected the item called 'rig'.")
            return {"CANCELLED"}
        if sim_data is None:
            # get_sim_data() already prints the error, if any
            return {"CANCELLED"}
        # Make sure Tower Unite Suite is installed, by checking if one of its property groups is registered.
        try:
            check_tu_suite_installed = context.scene.TU_Armature_Props
        except:
            self.debug("FAILED: Tower Unite Suite add-on not installed, or not enabled.")
            return {"CANCELLED"}

        # Get child meshes
        child_meshes = []
        for child in rig.children:
            if child is None:
                continue
            elif child.type == 'MESH':
                child_meshes.append(child)
        if len(child_meshes) == 0:
            self.debug("FAILED: Selected rig has no child mesh(es)")
            return {"CANCELLED"}

        # Perform the actions listed in the sim data
        for action in sim_data:
            # All actions need a transform type.
            if not "transform_type" in action:
                # Not the most user-friendly error... but hopefully it'll never show up.
                self.debug("FAILED: Missing transform_type data for "+context.scene.sim_properties.gender+" "+context.scene.sim_properties.age)
                return {"CANCELLED"}

            # Deselect everything
            # TODO
            # actually apparently you can temporarily override the context
            # in blender 3.2+ by doing:
            #  with bpy.context.temp_override(selected_objects=objs):
            #  bpy.ops.object.delete()

            temp_context = bpy.context.copy()
            print(str(temp_context))
            match action["transform_type"]:
                case "rotate": # INCOMPLETE
                    # Select the bone in action["bone_name"] and rotate it by action["X","Y","Z"] on the given local/global axis action["axis"]
                    # bpy.ops.transform.rotate()
                    if rig is None:
                        self.debug("FAILED: Trying to rotate bones on non-existent rig.")
                        return {"CANCELLED"}
                    #bone = rig.pose.bones.get(action["bone_name"])
                    bone = rig.data.bones.get(action["bone_name"])
                    if bone is None:
                        self.debug("FAILED: Trying to pose bone that doesn't exist: "+action["bone_name"])
                        return {"CANCELLED"}

                    self.debug("Rotating bone "+action["bone_name"])
                    vx = action["X"]
                    vy = action["Y"]
                    vz = action["Z"]
                    axis = action["axis"]
                    #with bpy.context.temp_override(active_object=rig, mode='POSE'):
                    #    bone.rotation_mode = "XYZ"
                    #    bone.rotation_euler.rotate_axis("X", radians(vx))
                    #    bone.rotation_euler.rotate_axis("Y", radians(vy))
                    #    bone.rotation_euler.rotate_axis("Z", radians(vz))
                    with bpy.context.temp_override(active_object=rig, mode='POSE'):
                        self.select_bone(bone)
                        bpy.ops.transform.rotate(value = radians(vx), orient_axis="X", orient_type='GLOBAL')
                        bpy.ops.transform.rotate(value = radians(vy), orient_axis="Y", orient_type='GLOBAL')
                        bpy.ops.transform.rotate(value = radians(vz), orient_axis="Z", orient_type='GLOBAL')
                
                case "move":
                    # Select the bone in action["bone_name"]
                    # bpy.ops.transform.translate()
                    if rig is None:
                        self.debug("FAILED: Trying to rotate bones on non-existent rig.")
                        return {"CANCELLED"}
                    bone = rig.pose.bones.get(action["bone_name"])
                    if bone is None:
                        self.debug("FAILED: Trying to pose bone that doesn't exist: "+action["bone_name"])
                        return {"CANCELLED"}

                    self.debug("Moving bone "+action["bone_name"])
                    with bpy.context.temp_override(active_object=rig, mode='POSE'):
                        move_vector = Vector((action["X"], action["Y"], action["Z"]))
                        self.debug( "Bone translate valid: "+ str(bpy.ops.transform.translate.poll()) )
                        #bpy.ops.transform.translate(value=move_vector, orient_type=action["axis"])
                        #bone.translate(move_vector)
                        bone.location = move_vector
                        #bpy.ops.object.transform_apply()
                
                case "scale_mesh":
                    # Scale the child meshes and apply the new scale
                    self.debug("Scaling mesh(es)")
                    for mesh in child_meshes:
                        with bpy.context.temp_override(active_object=mesh, mode='OBJECT'):
                            scale_vector = (action["X"], action["Y"], action["Z"])
                            self.debug( "Resize valid: "+ str(bpy.ops.transform.resize.poll()) )
                            bpy.ops.transform.resize(value=scale_vector, orient_type=action["axis"])
                            self.debug( "Transform_apply valid: "+ str(bpy.ops.object.transform_apply.poll()) )
                            bpy.ops.object.transform_apply(scale=True)
                
                case "apply_pose":
                    # Apply the current pose (a sanity check to make sure an Armature modifier named "Armature" exists would be nice)
                    self.debug("Applying pose")
                    #for mesh in child_meshes:
                    #    with bpy.context.temp_override(active_object=mesh, mode='OBJECT'):
                    #        self.debug( "Apply modifier armature valid: "+ str(bpy.ops.object.modifier_apply.poll()) )
                    #        bpy.ops.object.modifier_apply(modifier='Armature')
                
                case "delete_armature":
                    # Delete the Sims 4 rig.
                    #if not rig is None:
                    #    self.debug("Deleting armature")
                    #    with bpy.context.temp_override(active_object=rig, mode='OBJECT'):
                    #        self.debug( "Rig delete valid: "+str(bpy.ops.object.delete.poll()) )
                    #        bpy.ops.object.delete(confirm=False)
                    pass
                
                case "spawn_tu_rig":
                    # Configure and run TU Suite's armature-spawning code. Only the "arms raised" value should matter here.
                    self.debug("Spawning TU Armature (disabled)")
                    # This is kind of a ghetto way to do it but hopefully it works...
                    bpy.context.scene.TU_Adjust_Armature_Props.t_pose = action["arms_raised_percent"]
                    bpy.ops.tower_unite_suite.create_armature()
                    # TU Suite sets Blender to Edit mode after spawning its armature, for some reason.
                    bpy.ops.object.mode_set(mode='OBJECT')
                    # TODO: Give the meshes an Armature modifier
                    # TODO: Connect the new Armature modifer to the TU armature
                
                case "fix_vertex_groups":
                    pass
                    # Somehow run object.sims4_fix_vertex_groups
                    #for m in child_meshes:
                    #    self.debug("Fixing vertex groups on " + m.name)
                    #    with bpy.context.temp_override(active_object=m, mode='OBJECT'):
                    #        bpy.ops.object.sims4_fix_vertex_groups()
                
                case _:
                    # Apparently the list of actions can get stuck in memory even after re-installing the addon.
                    # This can make invalid actions remain.
                    self.debug("FAILED: Invalid transform_type data. Restart Blender if you've modified the list.")
                    return {"CANCELLED"}
                

        # The preferred setup would be:
        # - User selects the rig (obj = context.active_object)
        # - User inputs the model's age and gender
        # - User presses an "Auto Rig" button that activates this function.
        # - Script checks if the Tower Unite Suite is installed, and cancels with an error message if it isn't.
        # - Script gets a reference to the rig and the child mesh(es) (Object.children)
        # - Script poses the rig based on pre-defined values that differ by model age and gender. (defined in Sims4_Char_Transformations.py - bpy.ops.transform.rotate - bpy.types.Object.select_get())
        # - Script applies the Armature modifier on each child mesh (bpy.ops.object.modifier_apply(modifier='Armature')
        # - Script deletes the rig (bpy.ops.object.delete())
        # - Script scales each child mesh based on pre-defined values, which may differ by model age and gender. (bpy.ops.transform.resize())
        # ? Script applies the scale. (bpy.ops.object.transform_apply(scale=True))
        # X Script optionally adds the normal map from the same directory as the diffuse map. (OPTIONAL: this is a nice-to-have but not crucial so i'm leaving it for now)
        # ? Script spawns the Tower Unite Armature, with the right arm height.
        # ? Script adds Armature modifier to each child mesh and points it to the TU Armature
        # ? Script calls object.sims4_fix_vertex_groups on each child mesh.
        # - User manually fixes some weighting under the chin, if they want.
        # - User exports the model.
        self.debug("SUCCESS: Auto-Rigging completed! Except probably not because WIP.")
        return {"FINISHED"}

def register():
    bpy.utils.register_class(OBJECT_OT_Sims4VertexGroupFixer)
    bpy.utils.register_class(VIEW3D_PT_Sims4VertexGroupFixer)
    bpy.utils.register_class(OBJECT_OT_Sims4AutoRig)
    bpy.utils.register_class(VIEW3D_PT_Sims4AutoRig)
    bpy.utils.register_class(SimProperties)
    bpy.types.Scene.sim_properties = bpy.props.PointerProperty(type=SimProperties)

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_Sims4VertexGroupFixer)
    bpy.utils.unregister_class(VIEW3D_PT_Sims4VertexGroupFixer)
    bpy.utils.unregister_class(OBJECT_OT_Sims4AutoRig)
    bpy.utils.unregister_class(VIEW3D_PT_Sims4AutoRig)
    bpy.utils.unregister_class(SimProperties)
    del bpy.types.Scene.sim_properties

if __name__ == "__main__":
    register()
