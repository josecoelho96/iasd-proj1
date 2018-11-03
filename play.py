#!/usr/bin/env python3

import go
import games


def main():
    print("Welcome! Starting game...")
    game = go.Game()

    # file_path = "maps/statement-map.map"
    # file_path = "maps/custom-map1.map"
    # file_path = "maps/eye.map"
    # file_path = "maps/100.map"
    # file_path = "maps/1000.map"
    # file_path = "maps/custom-map2.map"
    # file_path = "maps/custom-map3.map"
    # file_path = "maps/custom-map4.map"
    # file_path = "maps/custom-map5.map"
    # file_path = "maps/custom-map6.map"
    # file_path = "maps/custom-map7.map"
    # file_path = "maps/tests/3-3.map"
    # file_path = "maps/tests/4-1.map"
    # file_path = "maps/tests/5-1.map"
    # file_path = "maps/tests/5-2.map"
    # file_path = "maps/tests/5-3.map"
    # file_path = "maps/tests/5-4.map"
    # file_path = "maps/tests/5-5.map"
    file_path = "maps/tests/5-6.map"


    with open(file_path) as f:
        state = game.load_board(f)

    print("Board loaded.")
    print("alpha_beta_cutoff_search(s,g) = {}".format(games.alphabeta_cutoff_search(state, game)))
    # print("alpha_beta_cutoff_search(s,g,d=3) = {}".format(games.alphabeta_cutoff_search(state, game, d=3)))


if __name__ == "__main__":
    main()
