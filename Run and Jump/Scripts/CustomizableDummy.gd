extends Sprite

func _on_ColorPicker_color_changed(color):
	material.set("shader_param/NEWCOLOR1",color)
