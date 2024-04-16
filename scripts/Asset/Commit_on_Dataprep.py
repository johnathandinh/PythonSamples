import unreal
 
# Path to the Dataprep Asset
EditorLib_Path = '/Game/Manual/Dataprep/'
 
# List dataprep assets in path
asset_subsys = unreal.get_editor_subsystem(unreal.EditorAssetSubsystem)
loaded_dataprep = asset_subsys.list_assets(EditorLib_Path)

# Select the dataprep asset first in list
dataprepAsset =  asset_subsys.load_asset(loaded_dataprep[0])
 
# Execute (commit) the dataprep
unreal.EditorDataprepAssetLibrary.execute_dataprep(dataprepAsset,unreal.DataprepReportMethod.STANDARD_LOG,unreal.DataprepReportMethod.STANDARD_LOG)