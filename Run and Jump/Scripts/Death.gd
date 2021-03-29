extends CollisionShape2D
class_name Death

func _on_Area2D_body_entered(body):
	if "Player" in body.name:
		print("you are out")
