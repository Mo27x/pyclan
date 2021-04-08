extends Node

class_name Game

var id
var players = [[[50,523], false, [255,255,255], "player1", 0, 0, id],[[50,523], false, [255,255,255], "player2", 0, 0, id],[[50,523], false, [255,255,255], "player3", 0, 0, id],[[50,523], false, [255,255,255], "player4", 0, 0, id]]
var winner
var deads = [players[0][1],players[1][1],players[2][1],players[3][1]]

func _init(gameId):
	id = gameId
	
func winner():
	var alivePlayers = 0
	var alivePlayer = 0
	var i = 0
	for dead in deads:
		if dead == false:
			alivePlayers += 1
			alivePlayer = i
		i += 1
	if alivePlayers == 1:
		return players[alivePlayer][4]
	return -1
