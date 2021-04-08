extends Node2D

onready var backGround1 = $Sprite
onready var backGround2 = $Sprite2

var backGrounds = [["res://Textures/Backgrounds/BackgroundLevel1-1.png","res://Textures/Backgrounds/BackgroundLevel1-2.png"],["res://Textures/Backgrounds/BackgroundLevel2-1.png","res://Textures/Backgrounds/BackgroundLevel2-2.png"]] 

func _random_background():
	var random = backGrounds[randi() % backGrounds.size()]
	backGround1.texture = load(random[0])
	backGround2.texture = load(random[1])

func _on_levelDuration_end_level():
	_random_background()
