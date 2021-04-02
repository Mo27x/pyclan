extends Area2D

export var g_starting_x: int = 1200
var g_player_in_portal : bool = false
var g_level_ended : bool = false

func _ready():
	$Sprite.rotate(130)
	$Sprite.visible = false
	$CollisionShape2D.disabled = true
	if g_player_in_portal == true and g_level_ended == true:
		$Sprite.visible = true
		$CollisionShape2D.disabled = false


func _on_LevelTransport_body_entered(body):
	if "Player" in body.name:
		g_player_in_portal = true

func _on_levelDuration_end_level():
	g_level_ended = true
