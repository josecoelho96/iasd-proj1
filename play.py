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
    file_path = "maps/tests/4-2.map"


    with open(file_path) as f:
        state = game.load_board(f)

    print("Board loaded.")

    print("actions(s) = {}".format(game.actions(state)))


if __name__ == "__main__":
    main()


# print("game.terminal_test(state) = {}".format(game.terminal_test(state)))
# # terminal_test(s) = False
# print("Move: (2, 5, 4)")
# state = game.result(state, (2, 5, 4))
# print("game.terminal_test(state) = {}".format(game.terminal_test(state)))
# # terminal_test(s) = True

# print("utility(s,1) = {}".format(game.utility(state, 1)))
# # utility(s,1) = -1

# print("utility(s,2) = {}".format(game.utility(state, 2)))
# # utility(s,2) = 1