extends Node2D

onready var play = $background/MarginContainer/VBoxContainer/VBoxContainer/Play
onready var settings = $background/MarginContainer/VBoxContainer/VBoxContainer/Settings
onready var customise = $background/MarginContainer/VBoxContainer/VBoxContainer/Customise

#Start the search for a game
func _on_Play_pressed():
# warning-ignore:return_value_discarded
	get_tree().change_scene("res://Scenes/Game.tscn")
	pass 

#Setting preferences
func _on_Setting_pressed():
# warning-ignore:return_value_discarded
	get_tree().change_scene("res://Scenes/SettingsMenu.tscn")
	pass 

#Customise the charachter
func _on_Customise_pressed():
# warning-ignore:return_value_discarded
	get_tree().change_scene("res://Scenes/Customisable/Customisable.tscn")
