extends Node2D

onready var play = $background/MarginContainer/VBoxContainer/VBoxContainer/Play
onready var settings = $background/MarginContainer/VBoxContainer/VBoxContainer/Settings
onready var customise = $background/MarginContainer/VBoxContainer/VBoxContainer/Customise

func _on_Play_pressed():
	get_tree().change_scene("res://Scenes/Game.tscn")
	pass 

func _on_Setting_pressed():
	get_tree().change_scene("res://Scenes/SettingsMenu.tscn")
	pass 

func _on_Customise_pressed():
	pass 
