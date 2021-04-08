extends Node

onready var settingsmenu = load("res://Scenes/SettingsMenu.tscn")

var filePath = "res://Keybinds.ini"
var configfile
var keybinds = {}

func _ready():
	configfile = ConfigFile.new()
	if configfile.load(filePath) == OK:
		for key in configfile.get_section_keys("keybinds"):
			var key_value = configfile.get_value("keybinds", key)
			print(key, " : ", OS.get_scancode_string(key_value))
			if str(key_value) != "":
				keybinds[key] = key_value
			else:
				keybinds[key] = null

		for audio in configfile.get_section_keys("audio"):
			var audio_value = configfile.get_value("audio",audio)
			print(audio, " : ", audio_value)

		for graphic in configfile.get_section_keys("graphics"):
			var graphic_value = configfile.get_value("graphics",graphic)
			print(graphic, " : ", graphic_value)
		
	else:
		print("CONFIG FILE NOT FOUND")
		get_tree().quit()

	set_game_binds()

func set_game_binds():
	for key in keybinds.keys():
		var value = keybinds[key]
		
		var actionlist = InputMap.get_action_list(key)
		if !actionlist.empty():
			InputMap.action_erase_event(key,actionlist[0])

		if value != null:
			var new_key = InputEventKey.new()
			new_key.set_scancode(value)
			InputMap.action_add_event(key,new_key)

func write_Config():
	for key in keybinds.keys():
		var key_value = keybinds[key]
		if key_value != null:
			configfile.set_value("keybinds",key,key_value)
		else:
			configfile.set_value("keybinds",key,"")
	configfile.save(filePath)
