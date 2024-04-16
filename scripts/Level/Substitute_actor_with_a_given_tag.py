
import unreal
 
##### Replace RPC assets
 
rpc_replacement_asset = '/Game/MultiUserViewer/Meshes/Tree/HillTree_02'
rpcs_to_replace = [
'Hawthorn',
'Honey_Locust',
'Largetooth_Aspen',
'Lombardy_Poplar',
'Red_Ash',
'Red_Maple',
'Scarlet_Oak'
]

actorSubsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
assetSubsystem = unreal.get_editor_subsystem(unreal.EditorAssetSubsystem)
all_actor_components = actorSubsystem.get_all_level_actors_components()
loaded_asset = assetSubsystem.load_asset(rpc_replacement_asset)
for component in all_actor_components:
    if component.component_has_tag("Revit.RPC"):
        actor_name = component.get_owner().get_actor_label()
        print("Found an RPC component: " + actor_name)
        for replacement_key in rpcs_to_replace:
            if (actor_name.startswith(replacement_key)):
                print("Replacing...")
                spawn_location = component.get_owner().get_actor_location()
                spawn_rotation = component.get_owner().get_actor_rotation()
                # randomize the rotation
                spawn_rotation.yaw = unreal.MathLibrary.random_float_in_range(0,360)
                # spawn the actor
                new_actor = actorSubsystem.spawn_actor_from_object(loaded_asset, spawn_location, spawn_rotation)
                new_actor.root_component.set_editor_property("mobility", unreal.ComponentMobility.MOVABLE)
                # randomize its scale factor
                scale_factor = unreal.MathLibrary.random_float_in_range(0.75,1.25)
                world_scale = new_actor.get_actor_scale3d()
                world_scale.z = world_scale.z * scale_factor
                new_actor.set_actor_scale3d( world_scale )
                # make the new actor a child of the RPC actor
                new_actor.attach_to_actor( component.get_owner(), "", unreal.AttachmentRule.KEEP_WORLD, unreal.AttachmentRule.KEEP_WORLD, unreal.AttachmentRule.KEEP_WORLD, False )
                break