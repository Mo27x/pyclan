extends Control

signal end_level

onready var progress = $ProgressBar
onready var time = $ProgressBar/Timer

var progress_value : int = 0

# warning-ignore:unused_argument
func _process(delta):
	progress.value = progress_value
	if progress.max_value == progress_value:
		progress_value = 0
		emit_signal("end_level")

func _on_Timer_timeout():
	progress_value += 1
