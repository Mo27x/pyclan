extends Game

var network = NetworkedMultiplayerENet.new()
var port = 1909
var max_player = 10
var games = {}
var idCount = 0

func _ready():
	StartServer()

func StartServer():
	network.create_server(port, max_player)
	get_tree().set_network_peer(network)
	print("Server started")
	
	network.connect("peer_connected", self, "_Peer_Connected")
	network.connect("peer_disconnected", self, "_Peer_Disconnected")

func _Peer_Connected(player_id, player):
	idCount += 1
	var gameId = (idCount - 1) / 2
	if idCount % 2 == 1:
		games[gameId] = Game.new(gameId)
		print("Creating a new game...")
	player[4] = player_id
	player[6] = gameId
	print("User " + str(player_id) + "Connected")

func _Peer_Disconnected(player_id):
	idCount -= 1
	print("User " + str(player_id) + "Disconnected")
	
remote func FetchSkillDamage(skill_name, requester):
	var player_id = get_tree().get_rpc_sender_id()
	var damage = ServerData.skill_data[skill_name].Damage
	rpc_id(player_id, "ReturnSkillDamage", damage, requester)
	print("sending " + str(damage) + " to player" + str(player_id))

remote func GetGame(player):
	for pla in games[player[6]].players:
		if pla.id == player.id:
			pla = player
	return games[player[6]]
