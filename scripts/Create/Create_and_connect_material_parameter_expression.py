
import unreal

assetSubsystem = unreal.get_editor_subsystem(unreal.EditorAssetSubsystem)

#load the material asset and the material parameter collection asset from content folder
materialTest = assetSubsystem.load_asset('/game/Create/MAT_1')
materialParameterCollectionTest = assetSubsystem.load_asset('/game/Create/MPC_1')
 
 
#create a material expression of type MaterialExpressionCollectionParameter
mecpc = unreal.MaterialEditingLibrary.create_material_expression(materialTest, unreal.MaterialExpressionCollectionParameter, -1000, 200)
#specify which collection parameter we want to use
mecpc.set_editor_property('collection',materialParameterCollectionTest)
#specify which parameter we want to use. MPC_1 has a parameter_name called 'Scalar1'
mecpc.set_editor_property('parameter_name','Scalar1')
#connect the expression to the output. The second parameter is supposed to be a string describing which output from the expression we want to use. leaving it empty the first one is selected
unreal.MaterialEditingLibrary.connect_material_property(mecpc, '', unreal.MaterialProperty.MP_METALLIC)
 
#recompile material
unreal.MaterialEditingLibrary.recompile_material(materialTest)
#save the material
assetSubsystem.save_loaded_asset(materialTest, True)
 
 