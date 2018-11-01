#!/usr/bin/env python3

import go

print("Welcome! Starting game...")

# file_path = "maps/statement-map.map"
# file_path = "maps/custom-map1.map"
# file_path = "maps/eye.map"
# file_path = "maps/100.map"
# file_path = "maps/1000.map"
# file_path = "maps/custom-map2.map"
file_path = "maps/custom-map3.map"



game = go.Game()

with open(file_path) as f:
    game.load_board(f)

print("Board loaded.")
game.display(game.state)
print("Valid moves: {}".format(game.actions(game.state)))
print("Is terminal?: {}".format(game.terminal_test(game.state)))
