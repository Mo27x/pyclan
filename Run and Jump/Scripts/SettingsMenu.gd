extends CanvasLayer

onready var optionContainer = $Panel/MarginContainer/VBoxContainer/Options
onready var optionButton = load("res://Scripts/KeyButton.gd")

var keybinds
var buttons = {}

func _ready():
	keybinds = Global.keybinds.duplicate()
	for key in keybinds.keys():
		var hbox =  HBoxContainer.new()
		var label = Label.new()
		var button = Button.new()
		
		hbox.set_h_size_flags(Control.SIZE_EXPAND_FILL)
		label.set_h_size_flags(Control.SIZE_EXPAND_FILL)
		button.set_h_size_flags(Control.SIZE_EXPAND_FILL)
		
		label.text = key
		
		var button_value = keybinds[key]
		
		if button_value != null:
			button.text = OS.get_scancode_string(button_value)
		else:
			button.text = "Unassigned"
		
		button.set_script(optionButton)
		button.key = key
		button.value = button_value
		button.menu = self
		button.toggle_mode = true
		button.focus_mode = Control.FOCUS_NONE
		
		hbox.add_child(label)
		hbox.add_child(button)
		optionContainer.add_child(hbox)
		
		buttons[key] = button

func change_bind(key,value):
	keybinds[key] = value
	for k in keybinds.keys():
		if k != key && value != null && keybinds[k] == value:
			keybinds[k] = null
			buttons[k].value = null
			buttons[k].text = "Unassigned"


func Back():
	get_tree().change_scene("res://Scenes/Menu.tscn")
	get_tree().paused = false


func Save():
	Global.keybinds = keybinds.duplicate()
	Global.set_game_binds()
	Global.write_Config()
	Back()
