import unreal
 
def replace_material(original, replacement):
    assetSubsystem = unreal.get_editor_subsystem(unreal.EditorAssetSubsystem)
    original_asset = assetSubsystem.load_asset(original)
    replacement_asset = assetSubsystem.load_asset(replacement)
    assetSubsystem.consolidate_assets(replacement_asset, [original_asset])
    #still need to run fixup redirectors
 
replace_material("/Game/Materials/M_MetalShiny_3", "/Game/Materials/M_MetalShiny_4")