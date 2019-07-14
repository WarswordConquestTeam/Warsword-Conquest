#Add the following definitions to the end (!) of header_operations.py
server_set_max_num_players   = 491 #(server_set_max_num_players, <max_players>, [<max_private_players>]), #Sets maximum players to <max_players> and maximum private players to [<max_private_players>] (default = same as <max_players>). Both values must be in the range 2-250, [<max_private_players>] can't be lower than <max_players>
position_rotate_x            = 723 #(position_rotate_x, <position_register>, <angle>, [<use_global_axis>]), #Rotates <position_register> around the x-axis by <angle> degrees
position_rotate_y            = 724 #(position_rotate_y, <position_register>, <angle>, [<use_global_axis>]), #Rotates <position_register> around the y-axis by <angle> degrees
position_rotate_z            = 725 #(position_rotate_z, <position_register>, <angle>, [<use_global_axis>]), #Rotates <position_register> around the z-axis by <angle> degrees
position_rotate_z_floating   = 734 #(position_rotate_z_floating, <position_register>, <angle_fixed_point>, [<use_global_axis>]), #Rotates <position_register> around the z-axis by <angle_fixed_point> degrees
position_rotate_x_floating   = 738 #(position_rotate_x_floating, <position_register>, <angle_fixed_point>, [<use_global_axis>]), #Rotates <position_register> around the x-axis by <angle_fixed_point> degrees
position_rotate_y_floating   = 739 #(position_rotate_y_floating, <position_register>, <angle_fixed_point>, [<use_global_axis>]), #Rotates <position_register> around the y-axis by <angle_fixed_point> degrees
is_vanilla_warband           = 1004 #(is_vanilla_warband), #Fails only when WSE is running
prop_instance_receive_damage = 1877 #(prop_instance_receive_damage, <prop_instance_no>, <agent_no>, <damage>, [<advanced>]), #<prop_instance_no> received <damage> damage from <agent_no>. If [<advanced>] is non-zero ti_on_scene_prop_hit will be called and the damage dealt will be sent to clients.

val_shr    = 2800 #(val_shr, <value>, <shift>), #Performs an arithmetic right bit shift by <shift> on <value>
store_shr  = 2801 #(store_shr, <destination>, <value>, <shift>), #Performs an arithmetic right bit shift by <shift> on <value> and stores the result into <destination>
val_lshr   = 2802 #(val_lshr, <value>, <shift>), #Performs a logical right bit shift by <shift> on <value>
store_lshr = 2803 #(store_lshr, <destination>, <value>, <shift>), #Performs a logical right bit shift by <shift> on <value> and stores the result into <destination>
val_shl    = 2804 #(val_shl, <value>, <shift>), #Performs a left bit shift by <shift> on <value>
store_shl  = 2805 #(store_shl, <destination>, <value>, <shift>), #Performs a left bit shift by <shift> on <value> and stores the result into <destination>
val_xor    = 2806 #(val_xor, <value1>, <value2>), #Performs a bitwise exclusive or between <value1> and <value2>
store_xor  = 2807 #(store_xor, <destination>, <value1>, <value2>), #Performs a bitwise exclusive or between <value1> and <value2> and stores the result into <destination>
val_not    = 2808 #(val_not, <value>), #Performs a bitwise complement on <value>
store_not  = 2809 #(store_not, <destination>, <value>), #Performs a bitwise complement on <value> and stores the result into <destination>

player_set_skin               = 2900 #(player_set_skin, <player_no>, <skin_no>), #Sets <player_no>'s skin (gender) to <skin_no> (requires network_compatible = 0 in wse_settings.ini)
player_stop_controlling_agent = 2901 #(player_stop_controlling_agent, <player_no>), #Gives <player_no>'s agent back to AI control (requires network_compatible = 0 in wse_settings.ini)
player_set_banner_id          = 2902 #(player_set_banner_id, <player_no>, <banner_no>), #Sets <player_no>'s banner to <banner_no>
player_set_username           = 2903 #(player_set_username, <player_no>, <string_no>), #Sets <player_no>'s username to <string_no>
player_temp_ban               = 2904 #(player_temp_ban, <player_no>, <ban_time>), #Bans <player_no> temporarily for <ban_time> seconds

register_get                  = 3000 #(register_get, <destination>, <index>), #Stores the value of register <index> into <destination>
register_set                  = 3001 #(register_set, <index>, <value>), #Sets the value of register <index> to <value>
store_wse_version             = 3002 #(store_wse_version, <destination>, <component>), #Stores <component> of the WSE version (0: major, 1: minor, 2: build) version into <destination>
item_slot_gt                  = 3003 #(item_slot_gt, <item_kind_no>, <slot_no>, <value>), #Fails if <item_kind_no>'s <slot_no> is not greater than <value>
party_template_slot_gt        = 3004 #(party_template_slot_gt, <party_template_no>, <slot_no>, <value>), #Fails if <party_template_no>'s <slot_no> is not greater than <value>
troop_slot_gt                 = 3005 #(troop_slot_gt, <troop_no>, <slot_no>, <value>), #Fails if <troop_no>'s <slot_no> is not greater than <value>
faction_slot_gt               = 3006 #(faction_slot_gt, <faction_no>, <slot_no>, <value>), #Fails if <faction_no>'s <slot_no> is not greater than <value>
quest_slot_gt                 = 3007 #(quest_slot_gt, <quest_no>, <slot_no>, <value>), #Fails if <quest_no>'s <slot_no> is not greater than <value>
scene_slot_gt                 = 3008 #(scene_slot_gt, <site_no>, <slot_no>, <value>), #Fails if <site_no>'s <slot_no> is not greater than <value>
party_slot_gt                 = 3009 #(party_slot_gt, <party_no>, <slot_no>, <value>), #Fails if <party_no>'s <slot_no> is not greater than <value>
player_slot_gt                = 3010 #(player_slot_gt, <player_no>, <slot_no>, <value>), #Fails if <player_no>'s <slot_no> is not greater than <value>
team_slot_gt                  = 3011 #(team_slot_gt, <team_no>, <slot_no>, <value>), #Fails if <team_no>'s <slot_no> is not greater than <value>
agent_slot_gt                 = 3012 #(agent_slot_gt, <agent_no>, <slot_no>, <value>), #Fails if <agent_no>'s <slot_no> is not greater than <value>
scene_prop_slot_gt            = 3013 #(scene_prop_slot_gt, <prop_instance_no>, <slot_no>, <value>), #Fails if <prop_instance_no>'s <slot_no> is not greater than <value>
store_current_trigger         = 3014 #(store_current_trigger, <destination>), #Stores the current trigger into <destination> (0 if not in a trigger)
return_values                 = 3015 #(return_values, [<value_1>], [<value_2>], [<value_3>], [<value_4>], [<value_5>], [<value_6>], [<value_7>], [<value_8>], [<value_9>], [<value_10>], [<value_11>], [<value_12>], [<value_13>], [<value_14>], [<value_15>], [<value_16>]), #Stores up to 16 return values
store_num_return_values       = 3016 #(store_num_return_values, <destination>), #Stores the amount of return values available into <destination>
store_return_value            = 3017 #(store_return_value, <destination>, [<value>]), #Stores return value no. [<value>] into <destination>
set_forced_lod                = 3018 #(set_forced_lod, <lod_level>), #Forces the current trigger entity's LOD level to <lod_level> (0 = auto)
send_message_to_url_advanced  = 3019 #(send_message_to_url_advanced, <url_string>, <user_agent_string>, [<success_callback_script_no>], [<failure_callback_script_no>], [<skip_parsing>], [<timeout>]), #Sends a HTTP request to <url_string> with <user_agent_string>. If the request succeeds, [<success_callback_script_no>] will be called. The script will behave like game_receive_url_response, unless [<skip_parsing>] is non-zero, in which case the script will receive no arguments and s0 will contain the full response. If the request fails, [<failure_callback_script_no>] will be called.
mtsrand                       = 3020 #(mtsrand, <value>), #Seeds the MT19937 random generator with <value>
mtrand                        = 3021 #(mtrand, <destination>, <min>, <max>), #Stores a random value between <min> and <max> into <destination> using the MT19937 random generator
get_time                      = 3022 #(get_time, <destination>, [<local>]), #Stores the current UNIX time into <destination>. If [<local>] is non-zero, it will store local time instead of universal time.
order_flag_is_active          = 3023 #(order_flag_is_active), #Fails if the order flag is not being placed
play_bink_file                = 3024 #(play_bink_file, <path_from_module_directory>, [<duration_in_ms>]), #Plays a .bik file located at <path_from_module_directory>. If [<duration_in_ms>] is not set the full movie will be played
process_advanced_url_messages = 3025 #(process_advanced_url_messages), #Forces processing of URL messages sent with send_message_to_url_advanced
sleep_ms                      = 3026 #(sleep_ms, <time>), #Sleeps (blocking the game) for <time> ms
timer_reset                   = 3027 #(timer_reset, <timer_register_no>, [<use_game_time>]), #Resets <timer_register_no>. If [<use_game_time>] is non-zero the timer will count game time rather than mission time
timer_get_elapsed_time        = 3028 #(timer_get_elapsed_time, <destination>, <timer_register_no>), #Stores <timer_register_no>'s elapsed time into <destination>
shell_open_url                = 3029 #(shell_open_url, <url>), #Opens <url> in default browser. Support only http://, https://, ftp:// and ts3server:// urls.
set_main_party                = 3030 #(set_main_party, <party_no>), #Sets player's main party to <party_no>. Dynamic spawned party (not listed in module_parties.py) will corrupt the savegame!
get_main_party                = 3031 #(get_main_party, <destination>), #Stores player's main party to <destination>
make_screenshot               = 3032 #(make_screenshot, <format>, <file>), #Make game screenshot. For security reasons, <file> will be saved into a Screenshots directory. Supported <format>s: BMP - 0, JPG - 1, TGA - 2, PNG - 3.

game_key_get_key  = 3100 #(game_key_get_key, <destination>, <game_key_no>), #Stores the key mapped to <game_key_no> into <destination>
key_released      = 3101 #(key_released, <key>), #Fails if <key> wasn't released in the current frame
game_key_released = 3102 #(game_key_released, <game_key_no>), #Fails if <game_key_no> wasn't released in the current frame

dict_create                = 3200 #(dict_create, <destination>), #Creates an empty dictionary object and stores it into <destination>
dict_free                  = 3201 #(dict_free, <dict>), #Frees the dictionary object <dict>. A dictionary can't be used after freeing it
dict_load_file             = 3202 #(dict_load_file, <dict>, <file>, [<mode>]), #Loads a dictionary file into <dict>. Setting [<mode>] to 0 (default) clears <dict> and then loads the file, setting [<mode>] to 1 doesn't clear <dict> but overrides any key that's already present, [<mode>] to 2 doesn't clear <dict> and doesn't overwrite keys that are already present
dict_load_dict             = 3203 #(dict_load_dict, <dict_1>, <dict_2>, [<mode>]), #Loads <dict_2> into <dict_1>. [<mode>]: see above
dict_save                  = 3204 #(dict_save, <dict>, <file>), #Saves <dict> into a file. For security reasons, <file> is just a name, not a full path, and will be stored into a WSE managed directory
dict_clear                 = 3205 #(dict_clear, <dict>), #Clears all key-value pairs from <dict>
dict_is_empty              = 3206 #(dict_is_empty, <dict>), #Fails if <dict> is not empty
dict_has_key               = 3207 #(dict_has_key, <dict>, <key>), #Fails if <key> is not present in <dict>
dict_get_size              = 3208 #(dict_get_size, <destination>, <dict>), #Stores the count of key-value pairs in <dict> into <destination>
dict_delete_file           = 3209 #(dict_delete_file, <file>), #Deletes dictionary file <file> from disk
dict_get_str               = 3210 #(dict_get_str, <string_register>, <dict>, <key>, [<default>]), #Stores the string value paired to <key> into <string_register>. If the key is not found and [<default>] is set, [<default>] will be stored instead. If [<default>] is not set, an empty string will be stored
dict_get_int               = 3211 #(dict_get_int, <destination>, <dict>, <key>, [<default>]), #Stores the numeric value paired to <key> into <destination>. If the key is not found and [<default>] is set, [<default>] will be stored instead. If [<default>] is not set, 0 will be stored
dict_set_str               = 3212 #(dict_set_str, <dict>, <key>, <string_no>), #Adds (or changes) <string_no> as the string value paired to <key>
dict_set_int               = 3213 #(dict_set_int, <dict>, <key>, <value>), #Adds (or changes) <value> as the numeric value paired to <key>
dict_get_key_by_iterator   = 3214 #(dict_get_key_by_iterator, <string_register>, <dict>, <iterator>), #Stores the key <string_register> by iterator <iterator>
dict_get_pos               = 3215 #(dict_get_pos, <position_register>, <dict>, <key>, [<default_position_register>]), #Stores the position paired to <key> into <position_register>. If the key is not found and [<default_position_register>] is set, [<default_position_register>] will be stored instead. If [<default_position_register>] is not set, (x:0,y:0,z:0,rotX:0,rotY:0,rotZ:0) will be stored
dict_set_pos               = 3216 #(dict_set_pos, <dict>, <key>, <position_register>), #Adds (or changes) <position_register> as the position value paired to <key>
dict_load_file_json        = 3217 #(dict_load_file_json, <dict>, <file>, [<mode>]), #Loads a dictionary json file into <dict>. [<mode>]: see above
dict_save_json             = 3218 #(dict_save_json, <dict>, <file>), #Saves <dict> into a json file. For security reasons, <file> is just a name, not a full path, and will be stored into a WSE managed directory
dict_from_url_encoded_json = 3219 #(dict_from_url_encoded_json, <dict>, <string>, [<mode>]), #Loads a url encoded json <string> into <dict>. [<mode>]: see above
dict_to_url_encoded_json   = 3220 #(dict_to_url_encoded_json, <string_register>, <dict>), #Saves <dict> into a url encoded json and stores into <string_register>

agent_get_item_modifier                         = 3300 #(agent_get_item_modifier, <destination>, <agent_no>), #Stores <agent_no>'s horse item modifier (-1 if agent is not a horse) into <destination>
agent_get_item_slot_modifier                    = 3301 #(agent_get_item_slot_modifier, <destination>, <agent_no>, <item_slot_no>), #Stores <agent_no>'s <item_slot_no> modifier into <destination>
agent_get_animation_progress                    = 3302 #(agent_get_animation_progress, <destination>, <agent_no>, [<channel_no>]), #Stores <agent_no>'s channel [<channel_no>] animation progress (in %%) into <destination>
agent_get_dna                                   = 3303 #(agent_get_dna, <destination>, <agent_no>), #Stores <agent_no>'s dna into <destination>
agent_get_ground_scene_prop                     = 3304 #(agent_get_ground_scene_prop, <destination>, <agent_no>), #Stores the prop instance on which <agent_no> is standing into <destination>
agent_set_item_slot_ammo                        = 3305 #(agent_set_item_slot_ammo, <agent_no>, <item_slot_no>, <value>), #Sets <agent_no>'s <item_slot_no> ammo count to <value>
agent_get_item_slot_hit_points                  = 3306 #(agent_get_item_slot_hit_points, <destination>, <agent_no>, <item_slot_no>), #Stores <agent_no>'s <item_slot_no> shield hitpoints into <destination>
agent_set_item_slot_hit_points                  = 3307 #(agent_set_item_slot_hit_points, <agent_no>, <item_slot_no>, <value>), #Sets <agent_no>'s <item_slot_no> shield hitpoints to <value>
agent_get_wielded_item_slot_no                  = 3308 #(agent_get_wielded_item_slot_no, <destination>, <agent_no>, [<hand_no>]), #Stores <agent_no>'s wielded item slot for [<hand_no>] into <destination>
agent_get_scale                                 = 3309 #(agent_get_scale, <destination_fixed_point>, <agent_no>), #Stores <agent_no>'s scale into <destination_fixed_point>
agent_set_forced_lod                            = 3310 #(agent_set_forced_lod, <agent_no>, <lod_level>), #Forces <agent_no>'s LOD level to <lod_level> (0 = auto)
agent_get_item_slot_flags                       = 3311 #(agent_get_item_slot_flags, <destination>, <agent_no>, <item_slot_no>), #Stores <agent_no>'s <item_slot_no> item slot flags into <destination>
agent_ai_get_move_target_position               = 3312 #(agent_ai_get_move_target_position, <position_register>, <agent_no>), #Stores <agent_no>'s move target position agent into <position_register>
agent_set_horse                                 = 3313 #(agent_set_horse, <agent_no>, <horse_agent_no>), #Sets <agent_no>'s horse to <horse_agent_no> (-1 for no horse)
agent_ai_set_simple_behavior                    = 3314 #(agent_ai_set_simple_behavior, <agent_no>, <simple_behavior>, [<guaranteed_time>]), #Sets <agent_no>'s behavior to <simple_behavior> and guarantees it won't be changed for [<guaranteed_time>] seconds. If [<guaranteed_time>] is not specified or <= 0, it won't be changed until agent_force_rethink is called
agent_accelerate                                = 3315 #(agent_accelerate, <agent_no>, <position_register_no>), #Uses x, y, z components of <position_register_no> to apply acceleration to <agent_no>
agent_set_item_slot_modifier                    = 3316 #(agent_set_item_slot_modifier, <agent_no>, <item_slot_no>, <item_modifier_no>), #Sets <agent_no>'s <item_slot_no> modifier to <item_modifier_no>
agent_body_meta_mesh_set_vertex_keys_time_point = 3317 #(agent_body_meta_mesh_set_vertex_keys_time_point, <agent_no>, <body_meta_mesh>, <time_point>), #Sets <agent_no>'s <body_meta_mesh> vertex keys time point to <time_point>
agent_body_meta_mesh_set_visibility             = 3318 #(agent_body_meta_mesh_set_visibility, <agent_no>, <body_meta_mesh>, <value>), #Shows (<value> = 1) or hides (<value> = 0) <agent_no>'s <body_meta_mesh>
agent_set_personal_animation                    = 3319 #(agent_set_personal_animation, <agent_no>, <anim_no>, <anim_no>), #Replaces <agent_no>'s default <anim_no> to personal <anim_no>
agent_get_personal_animation                    = 3320 #(agent_get_personal_animation, <destination>, <agent_no>, <anim_no>), #Stores <agent_no>'s personal <anim_no> into <destination>
agent_set_default_animations                    = 3321 #(agent_set_default_animations, <agent_no>), #Removes <agent_no>'s personal animations
agent_cancel_current_animation                  = 3322 #(agent_cancel_current_animation, <agent_no>, <channel_no>), #Cancels <agent_no>'s channel <2> animation

multiplayer_send_chat_message_to_player      = 3400 #(multiplayer_send_chat_message_to_player, <player_no>, <sender_player_no>, <text>, [<type>]), #Sends <text> to <player_no> as a (native compatible) chat message by <sender_player_no>. Works only on servers. [<type>]: 0 = chat, 1 = team chat
multiplayer_send_composite_message_to_player = 3401 #(multiplayer_send_composite_message_to_player, <player_no>, <message_type>, <message_register>), #Sends <message_register> with <message_type> to <player_no> (requires network_compatible = 0 in wse_settings.ini)
multiplayer_send_composite_message_to_server = 3402 #(multiplayer_send_composite_message_to_server, <message_type>, <message_register>), #Sends <message_register> with <message_type> to the server (requires network_compatible = 0 in wse_settings.ini)
multiplayer_get_cur_profile                  = 3403 #(multiplayer_get_cur_profile, <destination>), #Stores the current multiplayer profile into <destination>
multiplayer_get_num_profiles                 = 3404 #(multiplayer_get_num_profiles, <destination>), #Stores the number of multiplayer profiles into <destination>
multiplayer_message_init                     = 3405 #(multiplayer_message_init, <message_register>), #Initializes (empties) <message_register> (requires network_compatible = 0 in wse_settings.ini)
multiplayer_message_put_string               = 3406 #(multiplayer_message_put_string, <message_register>, <string>), #Puts <string> into <message_register> (requires network_compatible = 0 in wse_settings.ini)
multiplayer_message_put_int                  = 3407 #(multiplayer_message_put_int, <message_register>, <value>, [<num_bits>]), #Puts [<num_bits>] of <value> into <message_register> (requires network_compatible = 0 in wse_settings.ini)
multiplayer_message_put_position             = 3408 #(multiplayer_message_put_position, <message_register>, <position_register>, [<local>]), #Puts <position_register> into <9>. Set [<local>] to non-zero for small, relative positions (default: scene positions) (requires network_compatible = 0 in wse_settings.ini)
multiplayer_message_put_coordinate           = 3409 #(multiplayer_message_put_coordinate, <message_register>, <position_register>, [<local>]), #Puts x, y, z coordinates from <position_register> into <message_register>. Set [<local>] to non-zero for small, relative positions (default: scene positions) (requires network_compatible = 0 in wse_settings.ini)
multiplayer_cur_message_get_string           = 3410 #(multiplayer_cur_message_get_string, <string_register>), #Stores a string from the current message register into <string_register> (requires network_compatible = 0 in wse_settings.ini)
multiplayer_cur_message_get_int              = 3411 #(multiplayer_cur_message_get_int, <destination>, [<num_bits>]), #Stores [<num_bits>] of an int from the current message register into <destination>. [<num_bits>] MUST match the number of bits sent (requires network_compatible = 0 in wse_settings.ini)
multiplayer_cur_message_get_position         = 3412 #(multiplayer_cur_message_get_position, <position_register>, [<local>]), #Stores a position from the current message register into <position_register>. [<local>] MUST match the type sent (requires network_compatible = 0 in wse_settings.ini)
multiplayer_cur_message_get_coordinate       = 3413 #(multiplayer_cur_message_get_coordinate, <position_register>, [<local>]), #Stores x, y, z coordinates from the current message register into <position_register>. [<local>] MUST match the type sent (requires network_compatible = 0 in wse_settings.ini)

server_set_password_admin      = 3500 #(server_set_password_admin, <password>), #Sets <password> as server administrator password
server_set_password_private    = 3501 #(server_set_password_private, <password>), #Sets <password> as server private player password
server_map_rotation_get_count  = 3502 #(server_map_rotation_get_count, <destination>), #Stores the number of maps in rotation into <destination>
server_map_rotation_get_index  = 3503 #(server_map_rotation_get_index, <destination>), #Stores the current map rotation index into <destination>
server_map_rotation_set_index  = 3504 #(server_map_rotation_set_index, <index>), #Sets the current rotation index to <index>
server_map_rotation_get_map    = 3505 #(server_map_rotation_get_map, <destination>, <index>), #Stores the map at <index> into <destination>
server_map_rotation_add_map    = 3506 #(server_map_rotation_add_map, <site_no>, [<index>]), #Adds <site_no> to the map rotation at [<index>]
server_map_rotation_remove_map = 3507 #(server_map_rotation_remove_map, [<index>]), #Removes the map at [<index>] from the map rotation (does not work when only one left)
server_get_horse_friendly_fire = 3508 #(server_get_horse_friendly_fire, <destination>), #Stores horse friendly fire status into <destination> (requires network_compatible = 0 in wse_settings.ini)
server_set_horse_friendly_fire = 3509 #(server_set_horse_friendly_fire, <value>), #Enables or disables horse friendly fire (requires network_compatible = 0 in wse_settings.ini)
server_get_show_crosshair      = 3510 #(server_get_show_crosshair, <destination>), #Stores crosshair visibility status into <destination> (requires network_compatible = 0 in wse_settings.ini)
server_set_show_crosshair      = 3511 #(server_set_show_crosshair, <value>), #Enables or disables the crosshair (requires network_compatible = 0 in wse_settings.ini)
get_server_option_at_connect   = 3512 #(get_server_option_at_connect, <destination>, [<index>]), #Stores option [<index>] into <destination>
server_set_password_rcon       = 3513 #(server_set_password_rcon, <password>), #Sets <password> as server RCON password
execute_server_console_command = 3514 #(execute_server_console_command, <string_register>, <command>), #Executes dedicated server console command <command> and stores result string into <string_register>

store_cur_mission_template_no    = 3600 #(store_cur_mission_template_no, <destination>), #Stores the current mission template into <destination>
set_show_use_tooltip             = 3601 #(set_show_use_tooltip, <tooltip_type>, [<value>]), #Enables or disables use tooltips. See header_common_addon.py for possible types
set_ally_collision_threshold     = 3602 #(set_ally_collision_threshold, <low_boundary>, <high_boundary>), #Changes the animation progress boundaries (in percents) that determine if attacks on allies will collide (default: 45% <= x <= 60%)
particle_system_remove           = 3603 #(particle_system_remove, [<particle_system_no>]), #Removes [<particle_system_no>] (all particle systems if not set or -1) from the current entity (can be used in several in triggers)
get_spectated_agent_no           = 3604 #(get_spectated_agent_no, <destination>), #Stores spectated agent no into <destination>
prop_instance_set_forced_lod     = 3605 #(prop_instance_set_forced_lod, <prop_instance_no>, <lod_level>), #Forces <prop_instance_no>'s LOD level to <lod_level> (0 = auto)
prop_instance_set_variation_id   = 3606 #(prop_instance_set_variation_id, <prop_instance_no>, <value>), #Sets <prop_instance_no>'s variation id to <value>
prop_instance_set_variation_id_2 = 3607 #(prop_instance_set_variation_id_2, <prop_instance_no>, <value>), #Sets <prop_instance_no>'s variation id 2 to <value>
stop_time                        = 3608 #(stop_time, <value>), #Stops/resumes the mission. Works only in singleplayer with cheat mode enabled.
missile_get_path_point_position  = 3609 #(missile_get_path_point_position, <position_register>, <path_point_no>, <missile_no>), #Stores the position of the <missile_no>'s <path_point_no> (0-499) into <position_register>
get_water_level                  = 3610 #(get_water_level, <destination_fixed_point>), #Stores the water level into <destination_fixed_point>
missile_remove_on_hit            = 3611 #(missile_remove_on_hit), #Causes a missile item not to spawn on hit (can be only used inside ti_on_missile_hit)
missile_is_valid                 = 3612 #(missile_is_valid, <missile_no>), #Fails if <missile_no> is not valid
missile_get_cur_position         = 3613 #(missile_get_cur_position, <position_register>, <missile_no>), #Stores <missile_no>'s current position into <position_register>
set_prop_collision_threshold     = 3614 #(set_prop_collision_threshold, <attack_direction>, <low_boundary>, <high_boundary>), #Changes the animation progress boundaries (in percents) that determine if swing attacks on props will collide (default: 40% <= x <= 80% (75% for overheads))

troop_get_skill_points       = 3700 #(troop_get_skill_points, <destination>, <troop_no>), #Stores <troop_no>'s unused skill points into <destination>
troop_set_skill_points       = 3701 #(troop_set_skill_points, <troop_no>, <value>), #Sets <troop_no>'s unused skill points to <value>
troop_get_attribute_points   = 3702 #(troop_get_attribute_points, <destination>, <troop_no>), #Stores <troop_no>'s unused attribute points into <destination>
troop_set_attribute_points   = 3703 #(troop_set_attribute_points, <troop_no>, <value>), #Sets <troop_no>'s unused attribute points to <value>
troop_get_proficiency_points = 3704 #(troop_get_proficiency_points, <destination>, <troop_no>), #Stores <troop_no>'s unused proficiency points into <destination>
troop_set_proficiency_points = 3705 #(troop_set_proficiency_points, <troop_no>, <value>), #Sets <troop_no>'s unused proficiency points to <value>
troop_has_flag               = 3706 #(troop_has_flag, <troop_no>, <flag>), #Fails if <troop_no> doesn't have <flag>
troop_set_skill              = 3707 #(troop_set_skill, <troop_no>, <skill_no>, <value>), #Sets <troop_no>'s <skill_no> to <value>
troop_set_attribute          = 3708 #(troop_set_attribute, <troop_no>, <attribute>, <value>), #Sets <troop_no>'s <attribute> to <value>
troop_set_proficiency        = 3709 #(troop_set_proficiency, <troop_no>, <proficiency>, <value>), #Sets <troop_no>'s <proficiency> to <value>

item_set_thrust_damage      = 3800 #(item_set_thrust_damage, <item_kind_no>, <value>), #Sets <item_kind_no>'s thrust damage to <value>
item_set_thrust_damage_type = 3801 #(item_set_thrust_damage_type, <item_kind_no>, <value>), #Sets <item_kind_no>'s thrust damage type to <value>
item_set_swing_damage       = 3802 #(item_set_swing_damage, <item_kind_no>, <value>), #Sets <item_kind_no>'s thrust damage to <value>
item_set_swing_damage_type  = 3803 #(item_set_swing_damage_type, <item_kind_no>, <value>), #Sets <item_kind_no>'s thrust damage type to <value>
item_set_head_armor         = 3804 #(item_set_head_armor, <item_kind_no>, <value>), #Sets <item_kind_no>'s head armor to <value>
item_set_body_armor         = 3805 #(item_set_body_armor, <item_kind_no>, <value>), #Sets <item_kind_no>'s body armor to <value>
item_set_leg_armor          = 3806 #(item_set_leg_armor, <item_kind_no>, <value>), #Sets <item_kind_no>'s leg armor to <value>
item_set_speed_rating       = 3807 #(item_set_speed_rating, <item_kind_no>, <value>), #Sets <item_kind_no>'s speed rating to <value>
item_set_missile_speed      = 3808 #(item_set_missile_speed, <item_kind_no>, <value>), #Sets <item_kind_no>'s missile speed to <value>

party_stack_get_experience      = 3900 #(party_stack_get_experience, <destination>, <party_no>, <party_stack_no>), #Stores the experience of <party_no>'s <party_stack_no> into <destination>
party_stack_get_num_upgradeable = 3901 #(party_stack_get_num_upgradeable, <destination>, <party_no>, <party_stack_no>), #Stores the amount of upgradeable troops in <party_no>'s <party_stack_no> into <destination>
party_has_flag                  = 3902 #(party_has_flag, <party_no>, <flag>), #Fails if <party_no> doesn't have <flag>
party_heal_members              = 3903 #(party_heal_members, <party_no>, <troop_no>, <number>), #Heals <number> <troop_no> of <party_no>

position_get_vector_to_position = 4100 #(position_get_vector_to_position, <destination_fixed_point>, <dest_position_register>, <position_register_1>, <position_register_2>), #Stores the vector from <position_register_1> to <position_register_2> into <dest_position_register> and its length into <destination_fixed_point>
position_align_to_ground        = 4101 #(position_align_to_ground, <position_register>, [<point_up>], [<set_z_to_ground_level>]), #Aligns <position_register> to the ground (or to the ground normal if [<point_up>] is set)

str_equals                                = 4200 #(str_equals, <string_1>, <string_2>, [<case_insensitive>]), #Fails if <string_1> is not equal to <string_2>
str_contains                              = 4201 #(str_contains, <string_1>, <string_2>, [<case_insensitive>]), #Fails if <string_1> doesn't contain <string_2>
str_starts_with                           = 4202 #(str_starts_with, <string_1>, <string_2>, [<case_insensitive>]), #Fails if <string_1> doesn't start with <string_2>
str_ends_with                             = 4203 #(str_ends_with, <string_1>, <string_2>, [<case_insensitive>]), #Fails if <string_1> doesn't end with <string_2>
str_is_alpha                              = 4204 #(str_is_alpha, <string_1>, [<index>]), #Fails if character [<index>] of <string_1> isn't alphabetic. If [<index>] is not defined or is -1, the entire string is checked
str_is_digit                              = 4205 #(str_is_digit, <string_1>, [<index>]), #Fails if character [<index>] of <string_1> isn't a digit. If [<index>] is not defined or is -1, the entire string is checked
str_is_whitespace                         = 4206 #(str_is_whitespace, <string_1>, [<index>]), #Fails if character [<index>] of <string_1> isn't whitespace. If [<index>] is not defined or is -1, the entire string is checked
str_length                                = 4207 #(str_length, <destination>, <string_1>), #Stores the length of <string_1> into <destination>
str_index_of                              = 4208 #(str_index_of, <destination>, <string_1>, <string_2>, [<start>], [<end>]), #Stores the index of the first occurrence of <string_2> in <string_1> into <destination>. Search bounds can be specified with [<start>] and [<end>]
str_last_index_of                         = 4209 #(str_last_index_of, <destination>, <string_1>, <string_2>, [<start>], [<end>]), #Stores the index of the last occurrence of <string_2> in <string_1> into <destination>. Search bounds can be specified with [<start>] and [<end>]
str_get_char                              = 4210 #(str_get_char, <destination>, <string_1>, [<index>]), #Stores the numeric value of the [<index>]th character in <string_1> into <destination>
str_to_num                                = 4211 #(str_to_num, <destination_fixed_point>, <string_1>, [<use_fixed_point_multiplier>]), #Stores the numeric value of <string_1> into <destination_fixed_point>. Decimal values will be rounded to integers, for more precision set [<use_fixed_point_multiplier>] to non-zero
str_compare                               = 4212 #(str_compare, <destination>, <string_1>, <string_2>, [<case_insensitive>]), #Stores the relationship between <string_1> and <string_2> into <destination> (-1: s1 < s2, 0: s1 = s2, 1: s1 > s2)
str_split                                 = 4213 #(str_split, <destination>, <string_register>, <string_1>, <delimiter>, [<skip_empty>], [<max>]), #Splits <string_1> using <delimiter> into a range of string registers, starting from <string_register>, storing [<max>] substrings at most (default = unlimited), ignoring empty (zero length) substrings if [<skip_empty>] (default = false). Stores the amount of substrings split into <destination>
str_sort                                  = 4214 #(str_sort, <string_register>, [<count>], [<case_insensitive>], [<descending>]), #Sorts a range of [<count>] string registers starting from <string_register>
str_store_lower                           = 4215 #(str_store_lower, <string_register>, <string_1>), #Stores the lowercase version of <string_1> into <string_register>
str_store_upper                           = 4216 #(str_store_upper, <string_register>, <string_1>), #Stores the uppercase version of <string_1> into <string_register>
str_store_trim                            = 4217 #(str_store_trim, <string_register>, <string_1>, [<trim_mode>]), #Stores the whitespace trimmed version of <string_1> into <string_register>. [<trim_mode>]: 0 (default) = trim leading and trailing, 1 = trim leading, 2 = trim trailing
str_store_replace                         = 4218 #(str_store_replace, <string_register>, <string_1>, <string_2>, <string_3>), #Stores <string_1> into <string_register>, replacing occurrences of <string_2> with <string_3>
str_store_md5                             = 4219 #(str_store_md5, <string_register>, <string_1>), #MD5 encrypts <string_1> and stores it into <string_register>
str_store_substring                       = 4220 #(str_store_substring, <string_register>, <string_1>, [<start>], [<length>]), #Stores a substring of <string_1> into <string_register>, starting from [<start>]. If [<length>] is not specified, everything on the right of <start> will be used
str_store_reverse                         = 4221 #(str_store_reverse, <string_register>, <string_1>), #Stores the reverse of <string_register> into <string_1>
str_store_join                            = 4222 #(str_store_join, <string_register>, <start_string_register>, <count>, [<delimiter>]), #Joins <count> string registers starting from string register <start_string_register>, using [<delimiter>] (default = empty string) and stores them into <string_register>
str_store_replace_spaces_with_underscores = 4223 #(str_store_replace_spaces_with_underscores, <string_register>, <string_1>), #Stores <string_1> into <string_register>, replacing all spaces with underscores
str_store_replace_underscores_with_spaces = 4224 #(str_store_replace_underscores_with_spaces, <string_register>, <string_1>), #Stores <string_1> into <string_register>, replacing all underscores with spaces
str_store_multiplayer_profile_name        = 4225 #(str_store_multiplayer_profile_name, <string_register>, <profile_no>), #Stores <profile_no>'s name into <string_register>
str_store_module_setting                  = 4226 #(str_store_module_setting, <string_register>, <setting>), #Stores the string value (empty if not found) of <setting> in module.ini into <string_register>
str_store_server_password_admin           = 4227 #(str_store_server_password_admin, <string_register>), #Stores the server administrator password into <string_register>
str_store_server_password_private         = 4228 #(str_store_server_password_private, <string_register>), #Stores the server private player password into <string_register>
str_store_overlay_text                    = 4229 #(str_store_overlay_text, <string_register>, <overlay_no>), #Stores <overlay_no>'s text into <string_register>
str_store_player_ip                       = 4230 #(str_store_player_ip, <string_register>, <player_no>), #Stores <player_no>'s IP address into <string_register> (works only on servers)
str_store_game_variable                   = 4231 #(str_store_game_variable, <string_register>, <variable>), #Stores the string value (empty if not found) of <variable> in game_variables.txt into <string_register>
str_store_skill_name                      = 4232 #(str_store_skill_name, <string_register>, <skill_no>), #Stores the name of <skill_no> into <string_register>
str_store_float                           = 4233 #(str_store_float, <string_register>, <fp_register>, [<precision>]), #Stores the string representation of <fp_register> into <string_register> showing [<precision>] decimal digits at most
str_sanitize                              = 4234 #(str_sanitize, <string_register>), #Removes invalid characters from <string_register>
str_store_item_id                         = 4235 #(str_store_item_id, <string_register>, <item_no>), #Stores the id of <item_no> into <string_register>
str_is_integer                            = 4236 #(str_is_integer, <string_1>), #Fails if <string_1> isn't a valid integer
str_store_multiplayer_profile_face_keys   = 4237 #(str_store_multiplayer_profile_face_keys, <string_register>, <profile_no>), #Stores <profile_no>'s face keys into <string_register>
str_store_server_password_rcon            = 4238 #(str_store_server_password_rcon, <string_register>), #Stores the server RCON password into <string_register>
str_store_item_mesh_name                  = 4239 #(str_store_item_mesh_name, <string_register>, <item_no>), #Stores the mesh name of <item_no> into <string_register>
str_regex_match                           = 4240 #(str_regex_match, <string_1>, <string_regex>), #Fails if <string_1> does not match <string_regex>
str_regex_search                          = 4241 #(str_regex_search, <string_1>, <string_regex>), #Fails if <string_1> does not contain <string_regex>
str_regex_get_matches                     = 4242 #(str_regex_get_matches, <destination>, <string_register>, <string_1>, <string_regex>, [<max>]), #Stores all matches of <string_regex> that occur in <string_1> into a range of string registers, starting from <string_register>, storing [[<max>]] substrings at most (default = unlimited). Stores the amount of matches into <destination>
str_store_regex_replace                   = 4243 #(str_store_regex_replace, <string_register>, <string_1>, <string_regex>, <string_2>), #Stores <string_1> into <string_register>, replacing occurrences of <string_regex> with <string_2>
str_decode_url                            = 4244 #(str_decode_url, <string_register>, <string_1>), #Decode url encoded <string_1> and stores it into <string_register>

options_get_verbose_casualties  = 4300 #(options_get_verbose_casualties, <destination>), #Stores verbose casualties enabled/disabled into <destination>
options_set_verbose_casualties  = 4301 #(options_set_verbose_casualties, <value>), #Enables or disables verbose casualties
options_get_cheat_mode          = 4302 #(options_get_cheat_mode, <destination>), #Stores cheat mode enabled/disabled into <destination>
options_set_cheat_mode          = 4303 #(options_set_cheat_mode, <value>), #Enables or disables cheat mode
options_get_realistic_headshots = 4304 #(options_get_realistic_headshots, <destination>), #Stores "realistic" headshots enabled/disabled into <destination>
options_set_realistic_headshots = 4305 #(options_set_realistic_headshots, <value>), #Enables or disables "realistic" headshots

fld       = 4400 #(fld, <fp_register>, <value_fixed_point>), #Loads <value_fixed_point> into <fp_register>
fld_str   = 4401 #(fld_str, <fp_register>, <string>), #Parses <string> and loads it into <fp_register>
fld_pos_x = 4402 #(fld_pos_x, <fp_register>, <position_register_no>), #Loads the x component of <position_register_no> into <fp_register>
fld_pos_y = 4403 #(fld_pos_y, <fp_register>, <position_register_no>), #Loads the y component of <position_register_no> into <fp_register>
fld_pos_z = 4404 #(fld_pos_z, <fp_register>, <position_register_no>), #Loads the z component of <position_register_no> into <fp_register>
fst       = 4405 #(fst, <destination_fixed_point>, <fp_register>), #Stores <fp_register> into <destination_fixed_point>
fcpy      = 4406 #(fcpy, <fp_register_1>, <fp_register_2>), #Copies <fp_register_2> into <fp_register_1>
feq       = 4407 #(feq, <destination_fp_register>, <fp_register_1>, <fp_register_2>), #Fails if <fp_register_1> isn't approximately equal to <fp_register_2>
fgt       = 4408 #(fgt, <destination_fp_register>, <fp_register_1>, <fp_register_2>), #Fails if <fp_register_1> isn't greater than <fp_register_2>
flt       = 4409 #(flt, <destination_fp_register>, <fp_register_1>, <fp_register_2>), #Fails if <fp_register_1> isn't less than <fp_register_2>
fge       = 4410 #(fge, <destination_fp_register>, <fp_register_1>, <fp_register_2>), #Fails if <fp_register_1> isn't greater or approximately equal to <fp_register_2>
fle       = 4411 #(fle, <destination_fp_register>, <fp_register_1>, <fp_register_2>), #Fails if <fp_register_1> isn't less or approximately equal to <fp_register_2>
fsub      = 4412 #(fsub, <destination_fp_register>, <fp_register_1>, <fp_register_2>), #Subtracts <fp_register_2> from <fp_register_1> and stores the result into <destination_fp_register>
fmul      = 4413 #(fmul, <destination_fp_register>, <fp_register_1>, <fp_register_2>), #Multiplies <fp_register_1> by <fp_register_2> and stores the result into <destination_fp_register>
fdiv      = 4414 #(fdiv, <destination_fp_register>, <fp_register_1>, <fp_register_2>), #Divides <fp_register_1> by <fp_register_2> and stores the result into <destination_fp_register>
fmin      = 4415 #(fmin, <destination_fp_register>, <fp_register_1>, <fp_register_2>), #Stores the smaller value between <fp_register_1> and <fp_register_2> into <destination_fp_register>
fmax      = 4416 #(fmax, <destination_fp_register>, <fp_register_1>, <fp_register_2>), #Stores the larger value between <fp_register_1> and <fp_register_2> into <destination_fp_register>
fclamp    = 4417 #(fclamp, <destination_fp_register>, <fp_register_1>, <fp_register_2>, <fp_register_3>), #Clamps <fp_register_1> between <fp_register_2> and <fp_register_3> and stores the result into <destination_fp_register>
fsqrt     = 4418 #(fsqrt, <destination_fp_register>, <fp_register>), #Stores the square root of <fp_register> into <destination_fp_register>
fabs      = 4419 #(fabs, <destination_fp_register>, <fp_register>), #Stores the absolute value of <fp_register> into <destination_fp_register>
fceil     = 4420 #(fceil, <destination_fp_register>, <fp_register>), #Stores the ceiling of <fp_register> into <destination_fp_register>
ffloor    = 4421 #(ffloor, <destination_fp_register>, <fp_register>), #Stores the floor of <fp_register> into <destination_fp_register>
fexp      = 4422 #(fexp, <destination_fp_register>, <fp_register>), #Stores e raised to the power of <fp_register> into <destination_fp_register>
fpow      = 4423 #(fpow, <destination_fp_register>, <fp_register_1>, <fp_register_2>), #Stores <fp_register_1> raised to the power of <fp_register_2> into <destination_fp_register>
fln       = 4424 #(fln, <destination_fp_register>, <fp_register>), #Stores the natural logarithm of <fp_register> into <destination_fp_register>
flog      = 4425 #(flog, <destination_fp_register>, <fp_register>, [<base>]), #Stores the base-[<base>] (default: base-10) logarithm of <fp_register> into <destination_fp_register>
fmod      = 4426 #(fmod, <destination_fp_register>, <fp_register_1>, <fp_register_2>), #Stores the remainder of <fp_register_1>/<fp_register_2> into <destination_fp_register>
fsin      = 4427 #(fsin, <destination_fp_register>, <fp_register>), #Stores the sine of <fp_register> into <destination_fp_register>
fcos      = 4428 #(fcos, <destination_fp_register>, <fp_register>), #Stores the cosine of <fp_register> into <destination_fp_register>
ftan      = 4429 #(ftan, <destination_fp_register>, <fp_register>), #Stores the tangent of <fp_register> into <destination_fp_register>
fsinh     = 4430 #(fsinh, <destination_fp_register>, <fp_register>), #Stores the hyperbolic sine of <fp_register> into <destination_fp_register>
fcosh     = 4431 #(fcosh, <destination_fp_register>, <fp_register>), #Stores the hyperbolic cosine of <fp_register> into <destination_fp_register>
ftanh     = 4432 #(ftanh, <destination_fp_register>, <fp_register>), #Stores the hyperbolic tangent of <fp_register> into <destination_fp_register>
fasin     = 4433 #(fasin, <destination_fp_register>, <fp_register>), #Stores the arc sine of <fp_register> into <destination_fp_register>
facos     = 4434 #(facos, <destination_fp_register>, <fp_register>), #Stores the arc cosine of <fp_register> into <destination_fp_register>
fatan     = 4435 #(fatan, <destination_fp_register>, <fp_register>), #Stores the arc tangent of <fp_register> into <destination_fp_register>
fatan2    = 4436 #(fatan2, <destination_fp_register>, <fp_register_1>, <fp_register_2>), #Stores the arc cosine of <fp_register_1>/<fp_register_2> into <destination_fp_register>
feval     = 4437 #(feval, <expression_string>), #Evaluates <expression_string>. See EVAL_README.txt in WSESDK for more information
fadd      = 4438 #(fadd, <destination_fp_register>, <fp_register_1>, <fp_register_2>), #Adds <fp_register_2> to <fp_register_1> and stores the result into <destination_fp_register>

scene_set_flags         = 4500 #(scene_set_flags, <scene_no>, <flags>), #Sets <scene_no>'s flags to <flags>
scene_set_water_level   = 4501 #(scene_set_water_level, <scene_no>, <water_level_fixed_point>), #Sets <scene_no>'s water level to <water_level_fixed_point>
scene_set_bounds        = 4502 #(scene_set_bounds, <scene_no>, <min_x_fixed_point>, <min_y_fixed_point>, <max_x_fixed_point>, <max_y_fixed_point>), #Sets <scene_no>'s bounds to (<min_x_fixed_point>, <min_y_fixed_point>) and (<max_x_fixed_point>, <max_y_fixed_point>)
scene_set_outer_terrain = 4503 #(scene_set_outer_terrain, <scene_no>, <outer_terrain_mesh_name>), #Sets <scene_no>'s outer terrain to <outer_terrain_mesh_name>
scene_set_terrain_seed  = 4504 #(scene_set_terrain_seed, <scene_no>, <value>), #Sets <scene_no>'s terrain generator terrain seed to <value>
scene_set_river_seed    = 4505 #(scene_set_river_seed, <scene_no>, <value>), #Sets <scene_no>'s terrain generator river seed to <value>
scene_set_flora_seed    = 4506 #(scene_set_flora_seed, <scene_no>, <value>), #Sets <scene_no>'s terrain generator flora seed to <value>
scene_set_deep_water    = 4507 #(scene_set_deep_water, <scene_no>, <value>), #Enables or disables terrain generator deep water for <scene_no>
scene_set_place_river   = 4508 #(scene_set_place_river, <scene_no>, <value>), #Enables or disables terrain generator river placement for <scene_no>
scene_set_disable_grass = 4509 #(scene_set_disable_grass, <scene_no>, <value>), #Enables or disables terrain generator grass placement for <scene_no>
scene_set_valley_size   = 4510 #(scene_set_valley_size, <scene_no>, <value>), #Sets <scene_no>'s terrain generator valley size to <value> (0-127)
scene_set_hill_height   = 4511 #(scene_set_hill_height, <scene_no>, <value>), #Sets <scene_no>'s terrain generator hill height to <value> (0-127)
scene_set_ruggedness    = 4512 #(scene_set_ruggedness, <scene_no>, <value>), #Sets <scene_no>'s terrain generator ruggedness to <value> (0-127)
scene_set_vegetation    = 4513 #(scene_set_vegetation, <scene_no>, <value>), #Sets <scene_no>'s terrain generator vegetation to <value> (0-127)
scene_set_size          = 4514 #(scene_set_size, <scene_no>, <x>, <y>), #Sets <scene_no>'s terrain generator map size to (<x>, <y>) (0-1023)
scene_set_region_type   = 4515 #(scene_set_region_type, <scene_no>, <value>), #Sets <scene_no>'s terrain generator region type to <value> (0-15)
scene_set_region_detail = 4516 #(scene_set_region_detail, <scene_no>, <value>), #Sets <scene_no>'s terrain generator region detail to <value> (0-3)

edit_mode_get_num_selected_prop_instances = 4600 #(edit_mode_get_num_selected_prop_instances, <destination>), #Stores the number of selected prop instances into <destination>
edit_mode_get_selected_prop_instance      = 4601 #(edit_mode_get_selected_prop_instance, <destination>, <index>), #Stores the <index>th selected prop instance into instance no into <destination>
edit_mode_select_prop_instance            = 4602 #(edit_mode_select_prop_instance, <prop_instance_no>), #Stores the <1>th selected prop instance into instance no into <prop_instance_no>
edit_mode_deselect_prop_instance          = 4603 #(edit_mode_deselect_prop_instance, <prop_instance_no>), #Stores the <1>th selected prop instance into instance no into <prop_instance_no>
edit_mode_get_highlighted_prop_instance   = 4604 #(edit_mode_get_highlighted_prop_instance, <destination>), #Stores the highlighted prop instance into <destination>
edit_mode_set_highlighted_prop_instance   = 4605 #(edit_mode_set_highlighted_prop_instance, [<prop_instance_no>]), #Stores the <1>th selected prop instance into instance no into [<prop_instance_no>]
edit_mode_set_enabled                     = 4606 #(edit_mode_set_enabled, <value>), #Enables or disables edit mode

update_material = 4700 #(update_material, <material_name>, <new_material_name>), #Updates <material_name> with <new_material_name>

menu_create_new      = 4800 #(menu_create_new, <destination>, <text>, [<mesh_name>], [<flags>], [<script_no>], [<script_param>]), #Creates a dynamic menu and stores its id into <destination>. [<script_no>] (-1 for no script) will be called with params 1 = menu_no, 2 = [<script_param>] when the operations block is executed
menu_add_item        = 4801 #(menu_add_item, <menu_no>, <text>, [<conditions_script_no>], [<consequences_script_no>], [<script_param>]), #Adds a new menu item to <menu_no>. [<conditions_script_no>] and [<consequences_script_no>] (-1 for no script) will be called with params 1 = <menu_no>, 2 = [<script_param>] when the conditions/consequences blocks are executed
menu_clear_items     = 4802 #(menu_clear_items, <menu_no>), #Removes all menu items from <menu_no>
menu_clear_generated = 4803 #(menu_clear_generated), #Removes all dynamic menus

overlay_get_val       = 4900 #(overlay_get_val, <destination>, <overlay_no>), #Stores <overlay_no>'s value into <destination>
presentation_activate = 4901 #(presentation_activate, <presentation_no>), #Activates <presentation_no>. Fails if <presentation_no> is not running

array_create        = 5000 #(array_create, <destination>, <type_id>, <Dim 0>, [<Dim 1>], [<Dim 2>], [<Dim 3>], [<Dim 4>], [<Dim 5>], [<Dim 6>], [<Dim 7>], [<Dim 8>], [<Dim 9>], [<Dim 10>], [<Dim 11>], [<Dim 12>], [<Dim 13>]), #Creates an array object of <type_id> (0: Integer, 1: String, 2: Position) and stores its ID into <destination>. You can specify up to 14 dimensions, from <Dim 0> to [<Dim 13>]. The array will be initialized by default with 0 / empty string / 0-position.
array_free          = 5001 #(array_free, <arrayID>), #Frees array with <arrayID>.
array_copy          = 5002 #(array_copy, <destination>, <source arrayID>), #Copys array with <source arrayID> and stores the new array id into <destination>.
array_save_file     = 5003 #(array_save_file, <arrayID>, <file>), #Saves <arrayID> into a file. For security reasons, <file> is just a name, not a full path, and will be stored into a WSE managed directory.
array_load_file     = 5004 #(array_load_file, <destination>, <file>), #Loads <file> as an array and stores the newly created array's ID into <destination>.
array_delete_file   = 5005 #(array_delete_file, <file>), #Deletes array <file>.
array_set_val       = 5006 #(array_set_val, <arrayID>, <value>, <Index 0>, [<Index 1>], [<Index 2>], [<Index 3>], [<Index 4>], [<Index 5>], [<Index 6>], [<Index 7>], [<Index 8>], [<Index 9>], [<Index 10>], [<Index 11>], [<Index 12>], [<Index 13>]), #Writes <value> to the array with <arrayID> at the specified index. <value> can be an integer, a position register or a string register and must match the type of the array.
array_set_val_all   = 5007 #(array_set_val_all, <arrayID>, <value>), #Writes <value> to all indices of the array with <arrayID>. <value> can be an integer, a position register or a string register and must match the type of the array.
array_get_val       = 5008 #(array_get_val, <destination>, <arrayID>, <Index 0>, [<Index 1>], [<Index 2>], [<Index 3>], [<Index 4>], [<Index 5>], [<Index 6>], [<Index 7>], [<Index 8>], [<Index 9>], [<Index 10>], [<Index 11>], [<Index 12>], [<Index 13>]), #Gets a value from the array with <arrayID> at the specified index and writes it to <destination>. <destination> can be a variable, a position register or a string register and must match the type of the array.
array_push          = 5009 #(array_push, <destination arrayID>, <source>), #Pushes <source> on the array with <destination arrayID>. If <destination arrayID> is a 1D array, <source> can be an int, string, or position register and must match the type of <destination arrayID>. If <destination arrayID> is multidimensional, <source> must be the id of an array with matching type, src dimension count = dest dimension count - 1, and dimension sizes src_dim_0_size = dest_dim_1_size ... src_dim_n_size = dest_dim_n+1_size.
array_pop           = 5010 #(array_pop, <destination>, <arrayID>), #Pops the last value  from the array with <arrayID>. If <arrayID> is a 1D array, <destination> must be a variable, string, or position register and must match the type of <arrayID>. If <arrayID> is multidimensional, a new array with dimension count = src dimension count - 1, dimensions dim_0 = src_dim_1 ... dim_n = src_dim_n+1 will be created and its ID will be stored in <destination>
array_resize_dim    = 5011 #(array_resize_dim, <arrayID>, <dimIndex>, <size>), #Changes the size of the dimension with <dimIndex> of the array with <arrayID> to <size>.
array_get_dim_size  = 5012 #(array_get_dim_size, <destination>, <arrayID>, <dimIndex>), #Gets the size of the dimension with <dimIndex> of the array with <arrayID> and stores it into <destination>.
array_get_dim_count = 5013 #(array_get_dim_count, <destination>, <arrayID>), #Gets the the amount of dimensions of the array with <arrayID> and stores it into <destination>.
array_get_type_id   = 5014 #(array_get_type_id, <destination>, <arrayID>), #Gets the the type id of the array with <arrayID> and stores it into <destination>.
array_sort          = 5015 #(array_sort, <arrayID>, <sortMode>, [<Index 1>], [<Index 2>], [<Index 3>], [<Index 4>], [<Index 5>], [<Index 6>], [<Index 7>], [<Index 8>], [<Index 9>], [<Index 10>], [<Index 11>], [<Index 12>], [<Index 13>]), #Sorts the array with <arrayID> using a stable natural-mergesort algorithm. <sortMode> can be: [sort_m_int_asc or sort_m_int_desc] for int, [sort_m_str_cs_asc, sort_m_str_cs_desc, sort_m_str_ci_asc, sort_m_str_ci_desc] for str (asc=ascending, desc=descending, cs=case sensitive, ci=case insensitive, strings are compared alphabetically, upper before lower case). If the array is multidimensional, only the first dimension will be sorted and you must specify (dim_count - 1) fixed indices that will be used for access.
array_sort_custom   = 5016 #(array_sort_custom, <arrayID>, <cmpScript>, [<Index 1>], [<Index 2>], [<Index 3>], [<Index 4>], [<Index 5>], [<Index 6>], [<Index 7>], [<Index 8>], [<Index 9>], [<Index 10>], [<Index 11>], [<Index 12>], [<Index 13>]), #Sorts the array with <arrayID> using a stable natural-mergesort algorithm. <cmpScript> must compare its two input values (reg0 and reg1 / s0 and s1 / pos0 and pos1) and use (return_values, x) where x is nonzero if the first value goes before or is equal to the second, and zero otherwise. If the array is multidimensional, only the first dimension will be sorted and you must specify (dim_count - 1) fixed indices that will be used for access. The sorting won't be successful if the compare script does not work properly. The algorithm will abort at some point and not go into an infinite loop, it may however take extremely long to finish on big arrays.
array_eq            = 5017 #(array_eq, <arrayID>, <value_1>, <Index 0>, [<Index 1>], [<Index 2>], [<Index 3>], [<Index 4>], [<Index 5>], [<Index 6>], [<Index 7>], [<Index 8>], [<Index 9>], [<Index 10>], [<Index 11>], [<Index 12>], [<Index 13>]), #Fails if the specified value in the array with <arrayID> is not equal to <value_1>. Works for int, str and pos.
array_neq           = 5018 #(array_neq, <arrayID>, <value_1>, <Index 0>, [<Index 1>], [<Index 2>], [<Index 3>], [<Index 4>], [<Index 5>], [<Index 6>], [<Index 7>], [<Index 8>], [<Index 9>], [<Index 10>], [<Index 11>], [<Index 12>], [<Index 13>]), #Fails if the specified value in the array with <arrayID> is equal to <value_1>. Works for int, str and pos.
array_gt            = 5019 #(array_gt, <arrayID>, <value_1>, <Index 0>, [<Index 1>], [<Index 2>], [<Index 3>], [<Index 4>], [<Index 5>], [<Index 6>], [<Index 7>], [<Index 8>], [<Index 9>], [<Index 10>], [<Index 11>], [<Index 12>], [<Index 13>]), #Fails if the specified value in the array with <arrayID> is not greater than <value_1>. Works for int and str. Strings are compared alphabetically, upper before lower case.
array_ge            = 5020 #(array_ge, <arrayID>, <value_1>, <Index 0>, [<Index 1>], [<Index 2>], [<Index 3>], [<Index 4>], [<Index 5>], [<Index 6>], [<Index 7>], [<Index 8>], [<Index 9>], [<Index 10>], [<Index 11>], [<Index 12>], [<Index 13>]), #Fails if the specified value in the array with <arrayID> is not greater or equal to <value_1>. Works for int and str. Strings are compared alphabetically, upper before lower case.
array_lt            = 5021 #(array_lt, <arrayID>, <value_1>, <Index 0>, [<Index 1>], [<Index 2>], [<Index 3>], [<Index 4>], [<Index 5>], [<Index 6>], [<Index 7>], [<Index 8>], [<Index 9>], [<Index 10>], [<Index 11>], [<Index 12>], [<Index 13>]), #Fails if the specified value in the array with <arrayID> is not lower than <value_1>. Works for int and str. Strings are compared alphabetically, upper before lower case.
array_le            = 5022 #(array_le, <arrayID>, <value_1>, <Index 0>, [<Index 1>], [<Index 2>], [<Index 3>], [<Index 4>], [<Index 5>], [<Index 6>], [<Index 7>], [<Index 8>], [<Index 9>], [<Index 10>], [<Index 11>], [<Index 12>], [<Index 13>]), #Fails if the specified value in the array with <arrayID> is not lower or equal to <value_1>. Works for int and str. Strings are compared alphabetically, upper before lower case.

lhs_operations += [
	store_trigger_param,
	val_shr,
	store_shr,
	val_lshr,
	store_lshr,
	val_shl,
	store_shl,
	val_xor,
	store_xor,
	val_not,
	store_not,
	register_get,
	store_wse_version,
	store_current_trigger,
	store_num_return_values,
	store_return_value,
	mtrand,
	get_time,
	timer_get_elapsed_time,
	get_main_party,
	game_key_get_key,
	dict_create,
	dict_get_size,
	dict_get_int,
	agent_get_item_modifier,
	agent_get_item_slot_modifier,
	agent_get_animation_progress,
	agent_get_dna,
	agent_get_ground_scene_prop,
	agent_get_item_slot_hit_points,
	agent_get_wielded_item_slot_no,
	agent_get_scale,
	agent_get_item_slot_flags,
	agent_get_personal_animation,
	multiplayer_get_cur_profile,
	multiplayer_get_num_profiles,
	multiplayer_cur_message_get_int,
	server_map_rotation_get_count,
	server_map_rotation_get_index,
	server_map_rotation_get_map,
	server_get_horse_friendly_fire,
	server_get_show_crosshair,
	get_server_option_at_connect,
	store_cur_mission_template_no,
	get_spectated_agent_no,
	get_water_level,
	troop_get_skill_points,
	troop_get_attribute_points,
	troop_get_proficiency_points,
	party_stack_get_experience,
	party_stack_get_num_upgradeable,
	position_get_vector_to_position,
	str_length,
	str_index_of,
	str_last_index_of,
	str_get_char,
	str_to_num,
	str_compare,
	str_split,
	str_regex_get_matches,
	options_get_verbose_casualties,
	options_get_cheat_mode,
	options_get_realistic_headshots,
	fst,
	edit_mode_get_num_selected_prop_instances,
	edit_mode_get_selected_prop_instance,
	edit_mode_get_highlighted_prop_instance,
	menu_create_new,
	overlay_get_val,
	array_create,
	array_copy,
	array_load_file,
	array_get_val,
	array_pop,
	array_get_dim_size,
	array_get_dim_count,
	array_get_type_id,
]

can_fail_operations += [
	is_vanilla_warband,
	item_slot_gt,
	party_template_slot_gt,
	troop_slot_gt,
	faction_slot_gt,
	quest_slot_gt,
	scene_slot_gt,
	party_slot_gt,
	player_slot_gt,
	team_slot_gt,
	agent_slot_gt,
	scene_prop_slot_gt,
	order_flag_is_active,
	key_released,
	game_key_released,
	dict_is_empty,
	dict_has_key,
	missile_is_valid,
	troop_has_flag,
	party_has_flag,
	str_equals,
	str_contains,
	str_starts_with,
	str_ends_with,
	str_is_alpha,
	str_is_digit,
	str_is_whitespace,
	str_is_integer,
	str_regex_match,
	str_regex_search,
	feq,
	fgt,
	flt,
	fge,
	fle,
	presentation_activate,
	array_eq,
	array_neq,
	array_gt,
	array_ge,
	array_lt,
	array_le,
]
