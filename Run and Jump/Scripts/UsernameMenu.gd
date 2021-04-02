extends CanvasLayer

onready var nameContainer = $Panel/MarginContainer/VBoxContainer

var hbox = HBoxContainer.new()
var labelRequest = Label.new()
var labelName = LineEdit.new()
var labelError = Label.new()

func _ready():
	hbox.set_h_size_flags(Control.SIZE_EXPAND_FILL)
	labelRequest.set_h_size_flags(Control.SIZE_EXPAND_FILL)
	labelName.set_h_size_flags(Control.SIZE_EXPAND_FILL)
	labelError.set_h_size_flags(Control.SIZE_EXPAND_FILL)
	
	labelRequest.text = "Inserire un nome utente :"
	
	hbox.add_child(labelRequest)
	hbox.add_child(labelName)
	hbox.add_child(labelError)
	nameContainer.add_child(hbox)

func _input(event):
	if event is InputEventKey:
		if event.pressed and event.scancode == KEY_ENTER or event is InputEventMouseButton:
			labelName.text = ""
			labelName.grab_focus()


func _on_Save_pressed():
	if labelName.text != "":
		#saving of client name here, not implemented
		labelName.text = str(self)
# warning-ignore:return_value_discarded
		get_tree().change_scene("res://Scenes/Menu.tscn")
	else:
		labelError.text = "You have to assign a name for your client" 

func _on_Exit_pressed():
	get_tree().quit()
