#!/usr/bin/env python3

import go
import games

print("Welcome! Starting game...")

# file_path = "maps/statement-map.map"
# file_path = "maps/custom-map1.map"
# file_path = "maps/eye.map"
# file_path = "maps/100.map"
# file_path = "maps/1000.map"
# file_path = "maps/custom-map2.map"
# file_path = "maps/custom-map3.map"
file_path = "maps/custom-map4.map"
# file_path = "maps/custom-map5.map"
# file_path = "maps/custom-map6.map"
# file_path = "maps/custom-map7.map"



game = go.Game()

with open(file_path) as f:
    state = game.load_board(f)

print("Board loaded.")


while not game.terminal_test(state):
    game.display(state)
    print("Valid moves: {}".format(game.actions(game.state)))
    move = input("Your move: ")
    point = move.split()
    state = game.result(state, (1, int(point[0]), int(point[1])))

    computer_move = games.alphabeta_cutoff_search(state, game, d=4, cutoff_test=None, eval_fn=None)
    print(computer_move)
    state = game.result(state, computer_move)
    game.display(state)


# print("Is terminal?: {}".format(game.terminal_test(game.state)))
# print("ut 1. {}".format(game.utility(state, 1)))
# print("ut 2. {}".format(game.utility(state, 2)))
# print("Is terminal?: {}".format(game.terminal_test(game.state)))
# print("ut 1. {}".format(game.utility(state, 1)))
# print("ut 2. {}".format(game.utility(state, 2)))
# game.display(game.state)

# print("AB: {}".format(
