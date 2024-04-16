import unreal
 
asset_name = "MyAwesomeBPActorClass"
package_path = "/Game/Create"
 
factory = unreal.BlueprintFactory()
factory.set_editor_property("ParentClass", unreal.Actor)
 
asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
my_new_asset = asset_tools.create_asset(asset_name, package_path, None, factory)

assetSubsystem = unreal.get_editor_subsystem(unreal.EditorAssetSubsystem) 
assetSubsystem.save_loaded_asset(my_new_asset)