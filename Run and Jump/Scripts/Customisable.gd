extends Node

export var g_path_accessories: String = ""
export var g_path_hair: String = ""
export var g_path_hat: String = ""
export var g_path_head: String = ""
export var g_path_beard: String = ""

func _ready():
	var paths_accessories: Array = _get_full_paths(g_path_accessories)
	var paths_hair: Array = _get_full_paths(g_path_hair)
	var paths_hat: Array = _get_full_paths(g_path_hat)
	var paths_head: Array = _get_full_paths(g_path_head)
	var paths_beard: Array = _get_full_paths(g_path_beard)
	var resource
	for path in paths_accessories:
		resource = load(path)
	for path in paths_hair:
		resource = load(path)
	for path in paths_hat:
		resource = load(path)
	for path in paths_head:
		resource = load(path)
	for path in paths_beard:
		resource = load(path)

func _get_full_paths(path: String) -> Array:
	var files = _list_files_in_directory(path)
	var paths = []
	for file in files:
		paths.append(path + file)
	return paths

func _list_files_in_directory(path: String) -> Array:
	var files: Array = []
	var dir := Directory.new()

	dir.open(path)

	# Initialize stream used to list all files and directories
	dir.list_dir_begin()

	while true:
		var file: String = dir.get_next()
		if file == "":
			break
		elif not file.begins_with("."):
			files.append(file)

	# Close stream
	dir.list_dir_end()

	return files
