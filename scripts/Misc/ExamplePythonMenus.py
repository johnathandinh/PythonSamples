# Copyright Epic Games, Inc. All Rights Reserved.
#

import unreal

menu_owner = "TestPy"
tool_menus = unreal.ToolMenus.get()

def GetMainPythonMenu():
	main_menu = tool_menus.extend_menu("LevelEditor.MainMenu")
	main_menu.add_sub_menu(menu_owner, "", "Custom", "Custom", "")

	custom_menu = tool_menus.register_menu("LevelEditor.MainMenu.Custom", "", unreal.MultiBoxType.MENU, False)
	custom_menu.add_section("PythonSection", "Python Examples")
	custom_menu.add_sub_menu(menu_owner, "PythonSection", "Python", "Python", "")

	return tool_menus.register_menu("LevelEditor.MainMenu.Custom.Python", "", unreal.MultiBoxType.MENU, False)

@unreal.uclass()
class MenuEntryScript01(unreal.ToolMenuEntryScript):

	clicked_count = unreal.uproperty(int)

	def init_as_toolbar_button(self):
		self.data.menu = "LevelEditor.LevelEditorToolBar"
		self.data.advanced.entry_type = unreal.MultiBlockType.TOOL_BAR_BUTTON

	@unreal.ufunction(override=True)
	def execute(self, context):
		self.clicked_count += 1
		print("MenuEntryScript01 command has been called: " + str(self.clicked_count))

	@unreal.ufunction(override=True)
	def get_check_state(self, context):
		if self.clicked_count % 2 == 0:
			return unreal.CheckBoxState.UNCHECKED
		else:
			return unreal.CheckBoxState.CHECKED

	@unreal.ufunction(override=True)
	def can_execute(self, context):
		return True

	@unreal.ufunction(override=True)
	def is_visible(self, context):
		return True

	@unreal.ufunction(override=True)
	def get_label(self, context):
		return str(self.data.label) + ": " + str(self.clicked_count)

	@unreal.ufunction(override=True)
	def get_tool_tip(self, context):
		return "Python class MenuEntryScript01 ToolTip"

	@unreal.ufunction(override=True)
	def get_icon(self, context):
		if self.clicked_count % 2 == 0:
			return unreal.ScriptSlateIcon("EditorStyle", "LevelEditor.Build")
		else:
			return unreal.ScriptSlateIcon("EditorStyle", "LevelEditor.OpenLevelBlueprint")

@unreal.uclass()
class ContentBrowserAssetContextMenuExample(unreal.ToolMenuEntryScript):

	@unreal.ufunction(override=True)
	def execute(self, context):
		print("ContentBrowserAssetContextMenuExample command has been called")
		content_browser_context = context.find_by_class(unreal.ContentBrowserAssetContextMenuContext)
		if content_browser_context:
			selected_objects = content_browser_context.get_selected_objects()
			for x in selected_objects:
				print("  SelectedObject: ", x)

@unreal.uclass()
class ContentBrowserFolderContextMenuExample(unreal.ToolMenuEntryScript):

	@unreal.ufunction(override=True)
	def execute(self, context):
		print("ContentBrowserFolderContextMenuExample command has been called")

		content_browser_folder_context = context.find_by_class(unreal.ContentBrowserDataMenuContext_FolderMenu)
		if content_browser_folder_context:
			for x in content_browser_folder_context.selected_items:
				if x.is_folder():
					print("  Folder: ", x)
				if x.is_file():
					print("  File: ", x)
				print("    VirtualPath: ", x.get_virtual_path())

@unreal.uclass()
class AssetEditorMenuExample(unreal.ToolMenuEntryScript):
	@unreal.ufunction(override=True)
	def execute(self, context):
		print("AssetEditorMenuExample command has been called")
		asset_editor_toolkit_context = context.find_by_class(unreal.AssetEditorToolkitMenuContext)
		if asset_editor_toolkit_context:
			editing_objects = asset_editor_toolkit_context.get_editing_objects()
			for x in editing_objects:
				print("  editing_object: ", x)

@unreal.uclass()
class MenuEntryScriptDynamic01(unreal.ToolMenuEntryScript):
	@unreal.ufunction(override=True)
	def construct_menu_entry(self, menu, section, context):
		entry = unreal.ToolMenuEntryExtensions.init_menu_entry(
			menu_owner,
			"MenuEntryScriptDymamic01",
			"Dynamic Entry",
			"Dynamic Entry ToolTip",
			unreal.ToolMenuStringCommandType.PYTHON,
			"",
			"print(\"Dynamic Python Menu Entry called\")")
		menu.add_menu_entry(section, entry)

@unreal.uclass()
class SubMenuEntryScript01(unreal.ToolMenuEntryScript):
	def init(self):
		self.data.advanced.is_sub_menu = True

@unreal.uclass()
class PyTestDynamicSection01(unreal.ToolMenuSectionDynamic):
	@unreal.ufunction(override=True)
	def construct_sections(self, menu, context):
		menu.add_section("DynamicSection01", "Dynamic Section 01")

		entry = unreal.ToolMenuEntryExtensions.init_menu_entry(
			menu_owner,
			"DynamicSection01Entry01",
			"Dynamic Section01 Entry01",
			"ToolTip",
			unreal.ToolMenuStringCommandType.PYTHON,
			"",
			"print(\"DynamicSection01Entry01 called\")")
		menu.add_menu_entry("DynamicSection01", entry)

		entry = unreal.ToolMenuEntryExtensions.init_menu_entry(
			menu_owner,
			"DynamicSection01Entry02",
			"Dynamic Section01 Entry02",
			"ToolTip",
			unreal.ToolMenuStringCommandType.PYTHON,
			"",
			"print(\"DynamicSection01Entry02 called\")")
		menu.add_menu_entry("DynamicSection01", entry)

def AddMenuStringCommands(menu):

	menu.add_section("StringCommands", "String Commands", "", unreal.ToolMenuInsertType.FIRST)

	entry = unreal.ToolMenuEntryExtensions.init_menu_entry(
		menu_owner,
		"StringCommandsCommand",
		"Command",
		"Execute Command",
		unreal.ToolMenuStringCommandType.COMMAND,
		"",
		"echo test string menu command")
	menu.add_menu_entry("StringCommands", entry)

	entry = unreal.ToolMenuEntryExtensions.init_menu_entry(
		menu_owner,
		"StringCommandsPython",
		"Python",
		"Execute Python",
		unreal.ToolMenuStringCommandType.PYTHON,
		"",
		"print(\"python command executed\")")
	menu.add_menu_entry("StringCommands", entry)

	entry = unreal.ToolMenuEntryExtensions.init_menu_entry(
		menu_owner,
		"StringCommandsCustom",
		"Custom",
		"Test Custom",
		unreal.ToolMenuStringCommandType.CUSTOM,
		"TestCustom",
		"Test handling of custom script language that does not exist")
	menu.add_menu_entry("StringCommands", entry)

def AddToolbarStringCommands(menu):

	menu.add_section("StringCommands", "String Commands")

	# Button
	entry = unreal.ToolMenuEntryExtensions.init_menu_entry(
		menu_owner,
		"TestStringPy",
		"TestStringPy",
		"Test Python toolbar button",
		unreal.ToolMenuStringCommandType.PYTHON,
		"",
		"print(\"test python toolbar button pressed\")")
	entry.type = unreal.MultiBlockType.TOOL_BAR_BUTTON
	menu.add_menu_entry("StringCommands", entry)

	# Combo button
	entry = unreal.ToolMenuEntryExtensions.init_menu_entry(
		menu_owner,
		"TestComboPy",
		"TestComboPy",
		"",
		unreal.ToolMenuStringCommandType.COMMAND,
		"",
		"")
	entry.type = unreal.MultiBlockType.TOOL_BAR_COMBO_BUTTON
	menu.add_menu_entry("StringCommands", entry)

	# Create menu that goes with the combo button above
	sub_menu = tool_menus.register_menu("LevelEditor.LevelEditorToolBar.TestComboPy", "", unreal.MultiBoxType.MENU, False)
	entry = unreal.ToolMenuEntryExtensions.init_menu_entry(
		menu_owner,
		"TestComboItem",
		"Test Item",
		"Tooltip",
		unreal.ToolMenuStringCommandType.PYTHON,
		"",
		"print(\"Toolbar combo button's Item01 has been clicked\")")
	sub_menu.add_menu_entry("Section01", entry)

def AddClassBasedMenuItems(menu):
	menu.add_section("MenuEntryScript", "Menu Entry Script")

	# Basic
	entry = MenuEntryScript01()
	entry.init_entry(menu_owner, "LevelEditor.MainMenu.Custom.Python", "MenuEntryScript", "MenuEntryScriptA", "Basic")
	menu.add_menu_entry_object(entry)

	# Checkbox
	entry = MenuEntryScript01()
	entry.init_entry(menu_owner, "LevelEditor.MainMenu.Custom.Python", "MenuEntryScript", "MenuEntryScriptToggleButton", "Toggle Button")
	entry.data.advanced.user_interface_action_type = unreal.UserInterfaceActionType.TOGGLE_BUTTON
	menu.add_menu_entry_object(entry)

	# Dynamic Entry
	entry = MenuEntryScriptDynamic01()
	entry.init_entry(menu_owner, "LevelEditor.MainMenu.Custom.Python", "MenuEntryScript", "MenuEntryScriptDymamic", "Dymamic")
	menu.add_menu_entry_object(entry)

	# SubMenu
	entry = SubMenuEntryScript01()
	entry.init_entry(menu_owner, "LevelEditor.MainMenu.Custom.Python", "MenuEntryScript", "MenuEntryScriptSubMenu", "Sub menu")
	entry.init()
	menu.add_menu_entry_object(entry)

	# SubMenu Menu
	sub_menu = tool_menus.register_menu("LevelEditor.MainMenu.Custom.Python.MenuEntryScriptSubMenu", "", unreal.MultiBoxType.MENU, False)
	entry = unreal.ToolMenuEntryExtensions.init_menu_entry(
		menu_owner,
		"ItemA",
		"SubMenu Item",
		"SubMenu Item ToolTip",
		unreal.ToolMenuStringCommandType.PYTHON,
		"",
		"print(\"Python submenu item has been called\")")
	sub_menu.add_menu_entry("Section01", entry)

	# Dynamic Section
	menu.add_dynamic_section("DynamicSection", PyTestDynamicSection01())

	# Toolbar Button
	entry = MenuEntryScript01()
	entry.init_as_toolbar_button()
	entry.data.label = "PyClass"
	toolbar = tool_menus.extend_menu("LevelEditor.LevelEditorToolBar")
	toolbar.add_menu_entry_object(entry)

def Run():

	# Allow iterating on this menu python file without restarting editor
	tool_menus.unregister_owner_by_name(menu_owner)

	menu = GetMainPythonMenu()
	AddMenuStringCommands(menu)
	AddToolbarStringCommands(tool_menus.extend_menu("LevelEditor.LevelEditorToolBar"))
	AddClassBasedMenuItems(menu)

	# Content Browser Asset
	menu = tool_menus.extend_menu("ContentBrowser.AssetContextMenu")
	entry = ContentBrowserAssetContextMenuExample()
	entry.init_entry(menu_owner, "ContentBrowser.AssetContextMenu", "CommonAssetActions", "PythonExample", "Python Example")
	menu.add_menu_entry_object(entry)

	# Content Browser Folder
	menu = tool_menus.extend_menu("ContentBrowser.FolderContextMenu")
	entry = ContentBrowserFolderContextMenuExample()
	entry.init_entry(menu_owner, "ContentBrowser.FolderContextMenu", "PathViewFolderOptions", "PythonExample", "Python Example")
	menu.add_menu_entry_object(entry)

	# Asset Editor
	menu = tool_menus.extend_menu("AssetEditor.TextureEditor.MainMenu.File")
	entry = AssetEditorMenuExample()
	entry.init_entry(menu_owner, "AssetEditor.TextureEditor.MainMenu.File", "Example", "PythonExample", "Python Example")
	menu.add_menu_entry_object(entry)

	tool_menus.refresh_all_widgets()

Run()
