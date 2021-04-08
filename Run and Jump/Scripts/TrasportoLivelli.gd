extends Area2D

var g_player_in_portal : bool = false
var g_level_ended : bool = false

func _ready():
	$Sprite.visible = false
	$CollisionShape2D.disabled = true
	if g_player_in_portal == true and g_level_ended == true:
		$Sprite.visible = true
		$CollisionShape2D.disabled = false


func _on_LevelTransport_body_entered(body):
	if "Player" in body.name:
		g_player_in_portal = true
		print("The time has come")

func _on_levelDuration_end_level():
	$Sprite.visible = true
	$CollisionShape2D.disabled = false

