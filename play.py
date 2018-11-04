#!/usr/bin/env python3

import go
import games
import sys

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
    file_path = "maps/tests/3-3.map"
    # file_path = "maps/tests/4-1.map"
    # file_path = "maps/tests/5-1.map"
    # file_path = "maps/tests/5-2.map"
    # file_path = "maps/tests/5-3.map"
    # file_path = "maps/tests/5-4.map"
    # file_path = "maps/tests/5-5.map"
    # file_path = "maps/tests/5-6.map"


    with open(sys.argv[1]) as f:
    # with open(file_path) as f:
        state = game.load_board(f)

    print("Board loaded.")


    ########################### TEST 2 ###########################
    ########################### TEST 2 ###########################

    ########################### TEST 3 ###########################
    # print("Terminal test = {}".format(game.terminal_test(state)))
    # # new_state = game.result(state, (1, 1, 5)) # 3.1
    # # new_state = game.result(state, (2, 1, 2)) # 3.2
    # new_state = game.result(state, (2, 5, 4)) # 3.3
    # print("Terminal test = {}".format(game.terminal_test(new_state)))
    # print("utility(s, 1)={}".format(game.utility(new_state, 1)))
    # print("utility(s, 2)={}".format(game.utility(new_state, 2)))
    ########################### TEST 3 ###########################

    ########################### TEST 4 ###########################
    # print("actions(s) = {}".format(game.actions(state)))
    ########################### TEST 4 ###########################

    ########################### TEST 5 ###########################
    # if len(sys.argv) == 2:
    #     print("alpha_beta_cutoff_search(s,g) = {}".format(games.alphabeta_cutoff_search(state, game)))
    # else:
    #     print("alpha_beta_cutoff_search(s,g,d={}) = {}".format(sys.argv[2], games.alphabeta_cutoff_search(state, game, d=int(sys.argv[2]))))
    ########################### TEST 5 ###########################





if __name__ == "__main__":
    main()
