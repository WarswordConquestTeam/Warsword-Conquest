ti_on_agent_hit = -28.0 #can only be used in module_mission_templates triggers
# Trigger Param 1: receiver agent no
# Trigger Param 2: dealer agent no
# Trigger Param 3: inflicted damage
# Trigger Param 4: hit bone
# Trigger Param 5: missile item kind no
# Trigger Param 6: raw damage (before being soaked by armor)
# Trigger Param 7: item modifier
# Trigger Param 8: missile item modifier
# Trigger Param 9: damage type
# Register 0: item kind no
# Register 1: hit bone
# Position Register 0: position of the blow
#                      rotation gives the direction of the blow
# Trigger Result: if set, damage dealt to agent

ti_on_scene_prop_stepped_on = -100.0 #can only be used in module_scene_props triggers
# Trigger Param 1: agent no
# Trigger Param 2: prop instance no

ti_on_init_missile = -101.0 #can only be used in module_items triggers
# Trigger Param 1: shooter agent no
# Trigger Param 2: launcher item kind no
# Trigger Param 3: launcher item modifier
# Trigger Param 4: missile item kind no
# Trigger Param 5: missile item modifier
# Trigger Param 6: missile no

ti_on_agent_turn = -102.0 #can only be used in module_mission_templates triggers (for multiplayer player's agents)
# Trigger Param 1: agent no
# Trigger Param 2: max rotation speed (fixed point)
# trigger result = replace max rotation speed (fixed point)

ti_on_agent_blocked = -103.0 #can only be used in module_mission_templates triggers
# Trigger Param 1: receiver agent no
# Trigger Param 2: dealer agent no
# Trigger Param 3: item kind no
# Trigger Param 4: missile item kind no

ti_on_missile_dive = -104.0 #can only be used in module_items triggers
# Trigger Param 1: shooter agent no
# Trigger Param 2: launcher item kind no
# Trigger Param 3: launcher item modifier
# Trigger Param 4: missile item kind no
# Trigger Param 5: missile item modifier
# Trigger Param 6: missile no
# Position Register 0: water impact position and rotation

ti_on_agent_start_reloading = -105.0 #can only be used in module_mission_templates triggers
# Trigger Param 1: agent no

ti_on_agent_end_reloading = -106.0 #can only be used in module_mission_templates triggers
# Trigger Param 1: agent no
