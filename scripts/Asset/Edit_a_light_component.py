import unreal

def getActor(actorName):
    """
    seach for an actor label
 
    arg:
    actorName =  str|label beaing searched for
 
    returns:
    list of actor(s)
    """
    actor_subsys = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
    level_actors = actor_subsys.get_all_level_actors()
 
    filtered_list = unreal.EditorFilterLibrary.by_actor_label(
        level_actors,
        actorName,
        unreal.EditorScriptingStringMatchType.EXACT_MATCH
    )
 
    if len(filtered_list) == 0:
        unreal.log_warning('Did not find any actor with label: "{}"'.format(actorName))
    if len(filtered_list) > 1:
        unreal.log_warning('More then one actor with label: "{}"'.format(actorName))
    return filtered_list
 
SEARCH_LABEL = "BP_Property"
DIRECTORY_NAME = "/game/Textures/IES/"

# Retrieve the actor that we are going to change the light profile.
myActor = getActor(SEARCH_LABEL)[0]
assetSubsystem = unreal.get_editor_subsystem(unreal.EditorAssetSubsystem)
 
# Get its light component
pointLightsComponents = myActor.get_components_by_class(unreal.PointLightComponent)
if len(pointLightsComponents)>0 :
    # List ie textures 
    my_textures = assetSubsystem.list_assets(DIRECTORY_NAME)
    
    # load the texture
    my_load_asset = assetSubsystem.load_asset(my_textures[0])
    print(my_load_asset)
    
    # Change the texture file
    pointLightsComponents[0].set_editor_property('ies_texture', my_load_asset)
