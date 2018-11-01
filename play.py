#!/usr/bin/env python3

import go

print("Welcome! Starting game...")

file_path = "maps/statement-map.map"
# file_path = "maps/custom-map1.map"

game = go.Game()

with open(file_path) as f:
    game.load_board(f)

print(game.state)
