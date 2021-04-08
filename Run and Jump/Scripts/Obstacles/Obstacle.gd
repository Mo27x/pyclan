extends StaticBody2D

var g_velocity: float = 0

func _process(_delta: float) -> void:
	position.x += g_velocity

func get_height() -> float:
	return $Sprite.texture.get_size().y * scale.y * $Sprite.scale.y

func reset() -> void:
	g_velocity = 0

func start(velocity: float) -> void:
	g_velocity = -velocity
