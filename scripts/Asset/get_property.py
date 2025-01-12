import unreal

actor_subsys = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
level_actors = actor_subsys.get_all_level_actors()
filtered_list = unreal.EditorFilterLibrary.by_actor_label(
    level_actors,
    "my_actor",
    unreal.EditorScriptingStringMatchType.EXACT_MATCH
)
actor = filtered_list[0]

value = actor.get_editor_property("my_property")

print (value)
