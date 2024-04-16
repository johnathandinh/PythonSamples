## Code for FBX export
import unreal
 
file_to_import = "C:\\temp\\CAD\\Clutch assembly.SLDASM"
final_fbx_file = "C:\\temp\\my_filename.fbx"
asset_folder = '/Game/Create/MyCADScene'
merge_actor_name = 'NEW_MESH_actor'
fbx_destination = '/Game/Create/NEW_MESH'
 
# clear anything existing in the level.
actorSubsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
assetSubsystem = unreal.get_editor_subsystem(unreal.EditorAssetSubsystem)
staticmeshsubsystem = unreal.get_editor_subsystem(unreal.StaticMeshEditorSubsystem)
all_actors = actorSubsystem.get_all_level_actors()

actorSubsystem.destroy_actors(all_actors)
 
# Construct the Datasmith Scene from a file on disk.
ds_scene_in_memory = unreal.DatasmithSceneElement.construct_datasmith_scene_from_file(file_to_import)
 
print('constructed the scene')
 
if ds_scene_in_memory is None:
    print('Scene loading failed.')
    quit()
 
# Set import options.
import_options = ds_scene_in_memory.get_options()
tessellation_options = ds_scene_in_memory.get_options(unreal.DatasmithCommonTessellationOptions)
if tessellation_options:
    tessellation_options.options.chord_tolerance = 1
    tessellation_options.options.max_edge_length = 40
    tessellation_options.options.normal_tolerance = 45
import_options.base_options.scene_handling = unreal.DatasmithImportScene.CURRENT_LEVEL
 
# Finalize the process by creating assets and actors.
ds_scene_in_memory.import_scene(asset_folder)
 
print('Import complete!')
 
# merge the actors into one object
all_actors = actorSubsystem.get_all_level_actors()
merge_options = unreal.MergeStaticMeshActorsOptions()
merge_options.new_actor_label = merge_actor_name
# look for the unreal.MeshMergingSettings class to see what options you can set in here
merge_options.base_package_name = fbx_destination

new_mesh_actor = staticmeshsubsystem.merge_static_mesh_actors(all_actors, merge_options)

# load the merged asset
#SM_ prefix added by meger static mesh actors will be removed in a future version of UE
assetname = fbx_destination.split('/')[-1]
fbx_destination2 = fbx_destination.rstrip(assetname) + '/SM_'+assetname
loaded_asset = assetSubsystem.load_asset(fbx_destination2)
 
# set up the FBX export options
task = unreal.AssetExportTask()
task.object = loaded_asset      # the asset to export
task.filename = final_fbx_file        # the filename to export as
task.automated = True           # don't display the export options dialog
task.replace_identical = True   # always overwrite the output
task.options = unreal.FbxExportOption()
 
# export!
result = unreal.Exporter.run_asset_export_task(task)
 
print('Export complete!')
for error_msg in task.errors:
    unreal.log_error('{}'.format(error_msg))



## Code for OBJ export
import unreal

file_to_import = "C:\\temp\\CAD\\Clutch assembly.SLDASM"
final_obj_file = "C:\\temp\\my_filename.obj"
asset_folder = '/Game/Create/MyCADScene'
obj_destination = '/Game/Create/NEW_MESH'
 
# clear anything existing in the level.
actorSubsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
assetSubsystem = unreal.get_editor_subsystem(unreal.EditorAssetSubsystem)
staticmeshsubsystem = unreal.get_editor_subsystem(unreal.StaticMeshEditorSubsystem)
all_actors = actorSubsystem.get_all_level_actors()
 
for a in all_actors:
    actorSubsystem.destroy_actor(a)
 
# Construct the Datasmith Scene from a file on disk.
ds_scene_in_memory = unreal.DatasmithSceneElement.construct_datasmith_scene_from_file(file_to_import)
 
print('constructed the scene')
 
if ds_scene_in_memory is None:
    print('Scene loading failed.')
    quit()
 
# Set import options.
import_options = ds_scene_in_memory.get_options()
tessellation_options = ds_scene_in_memory.get_options(unreal.DatasmithCommonTessellationOptions)
if tessellation_options:
    tessellation_options.options.chord_tolerance = 1
    tessellation_options.options.max_edge_length = 40
    tessellation_options.options.normal_tolerance = 45
import_options.base_options.scene_handling = unreal.DatasmithImportScene.CURRENT_LEVEL
 
# Finalize the process by creating assets and actors.
ds_scene_in_memory.import_scene(asset_folder)
 
print('Import complete!')
 
# merge the actors into one object
all_actors = actorSubsystem.get_all_level_actors()
merge_options = unreal.EditorScriptingMergeStaticMeshActorsOptions()
# look for the unreal.MeshMergingSettings class to see what options you can set in here
merge_options.base_package_name = obj_destination
new_mesh_actor = staticmeshsubsystem.merge_static_mesh_actors(all_actors, merge_options)
 
# load the merged asset
#SM_ prefix added by meger static mesh actors will be removed in a future version of UE
assetname = obj_destination.split('/')[-1]
obj_destination2 = obj_destination.rstrip(assetname) + '/SM_'+assetname
loaded_asset = assetSubsystem.load_asset(obj_destination2)
 
# set up the OBJ export options
task = unreal.AssetExportTask()
task.object = loaded_asset      # the asset to export
task.filename = final_obj_file        # the filename to export as
task.automated = True           # don't display the export options dialog
task.replace_identical = True   # always overwrite the output
task.exporter = unreal.StaticMeshExporterOBJ()
 
# export!
result = unreal.Exporter.run_asset_export_task(task)
 
print('Export complete!')
for error_msg in task.errors:
    unreal.log_error('{}'.format(error_msg))
