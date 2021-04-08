extends KinematicBody2D
class_name Player

const Floor = Vector2(0, -1)

var gravity_magnitude : int = ProjectSettings.get_setting("physics/2d/default_gravity")

export var speed :int = 300
export var jump_height : int = -1500

onready var animazioni = $AnimatedSprite
var velocity = Vector2()

func get_input():
	velocity = Vector2()
	if Input.is_action_pressed('right'):
		animazioni.play("Run")
		velocity.x += speed
	if Input.is_action_pressed('left'):
		animazioni.play("Run")
		velocity.x -= speed
	if Input.is_action_pressed('down'):
		velocity.y += speed
	if Input.is_action_pressed('up') && is_on_floor():
		velocity.y = jump_height

	velocity.y +=  gravity_magnitude


func _physics_process(delta):
	get_input()
	velocity = move_and_slide(velocity,Floor)
