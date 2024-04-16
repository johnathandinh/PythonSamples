import unreal
 
######### fill list of actors #########
def get_selected():
    actor_subsys = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
    return actor_subsys.get_selected_level_actors()
     
selected_actors = get_selected()
#filter to retain only static mesh actors
selected_static_mesh_actors = unreal.EditorFilterLibrary.by_class(selected_actors, unreal.StaticMeshActor.static_class())  
#iterate over static mesh actors
for sma in selected_static_mesh_actors:
    #get static mesh component
    smc = sma.static_mesh_component
    if smc is None:
        continue
    #get static mesh
    sm = smc.static_mesh
    if sm is None:
        continue
    #edit the property
    sm.set_editor_property('light_map_resolution',1024)
    #save the modification of the related asset in the content folder
    assetSubsystem = unreal.get_editor_subsystem(unreal.EditorAssetSubsystem)
    assetSubsystem.save_loaded_asset(sm)