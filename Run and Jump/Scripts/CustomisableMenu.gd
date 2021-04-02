extends CanvasLayer


func _ready():
	pass


func _on_Save_pressed():
	get_tree().change_scene("res://Scenes/Menu.tscn")

func _on_Exit_pressed():
	get_tree().change_scene("res://Scenes/Menu.tscn")
