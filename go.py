import games

# black = 1
# white = 2

class Game(games.Game):
    """ Atari Go game class."""
    # board_size = -1

    # def __init__(self, f):
    #     self.state = self.load_board(f)

    def to_move(self, s):
        """Returns the player to move next given the state s."""
        return s.to_move

    def terminal_test(self, s):
        """Returns a boolean of whether state s is terminal."""
        raise NotImplementedError

    def utility(self, s, p):
        """Returns the payoff of state s if it is terminal
            (1 if p wins, -1 if p loses, 0 in case of a draw),
            otherwise, its evaluation with respect to player p."""
        raise NotImplementedError

    def actions(self, s):
        """Returns a list of valid moves at state s."""
        raise NotImplementedError

    def result(self, s, a):
        """Returns the sucessor game state after playing move a at state s."""
        raise NotImplementedError

    def load_board(self, f):
        """Loads a board from a file object f (with given format)
            and returns the corresponding state."""

        ############################ AUX FUNCTIONS ############################
        def insert_stone_in_player_strings(reference_point, new_point, stones):
            for string in stones:
                print("[DEBUG] String: {}".format(string))
                if reference_point in string:
                    print("[DEBUG] Reference point match on string: {}".format(string))
                    string.append(new_point)
                    return string

        def search_stone_in_player_strings(reference_point, new_point, stones):
            for string in stones:
                print("[DEBUG] String: {}".format(string))
                if reference_point in string:
                    print("[DEBUG] Reference point match on string: {}".format(string))
                    return string

        def check_if_empty_point(board_map, point):
            return board_map[point[0]][point[1]] == '0'

        def update_player_stones(board_map, player, point, stones):

            i = point[0]
            j = point[1]

            flag_new_string = True # True if stone is isolated and a new string must be created
            updated_string = None
            if i > 0:
                print("[DEBUG] Look at 'i-1'.")
                if board_map[i-1][j] == player:
                    print("[DEBUG] Stone at i-1 is the same type. String found.")
                    flag_new_string = False
                    updated_string = insert_stone_in_player_strings((i-1, j), point, stones)

            if j > 0:
                print("[DEBUG] Look at 'j-1'.")
                if board_map[i][j-1] == player:
                    print("[DEBUG] Stone at j-1 is the same type. String found.")
                    if flag_new_string == False:
                        # Stone was added to group on i-1, merge two lists into a bigger string
                        second_updated_string = search_stone_in_player_strings((i, j-1), point, stones)
                        updated_string += second_updated_string
                        stones.remove(second_updated_string)
                    else:
                        insert_stone_in_player_strings((i, j-1), point, stones)

                    flag_new_string = False

            if flag_new_string:
                print("[DEBUG] New string formed.")
                stones.append([point])

        def update_player_liberties(board_map, stones, liberties):
            for string in stones:
                string_liberties = []
                for stone in string:
                    print("[DEBUG] Check liberties on stone: {}".format(stone))
                    i = stone[0]
                    j = stone[1]

                    if i > 0:
                        print("[DEBUG] Look at 'i-1'.")
                        if check_if_empty_point(board_map, (i-1, j)):
                            string_liberties.append((i-1, j))
                    if i < board_size - 1:
                        print("[DEBUG] Look at 'i+1'.")
                        if check_if_empty_point(board_map, (i+1, j)):
                            string_liberties.append((i+1, j))
                    if j > 0:
                        print("[DEBUG] Look at 'j-1'.")
                        if check_if_empty_point(board_map, (i, j-1)):
                            string_liberties.append((i, j-1))
                    if j < board_size - 1:
                        print("[DEBUG] Look at 'j+1'.")
                        if check_if_empty_point(board_map, (i, j+1)):
                            string_liberties.append((i, j+1))

                liberties.append(string_liberties)
        ############################ AUX FUNCTIONS ############################

        line = f.readline()
        board_size = int(line.split()[0])
        player_to_move = int(line.split()[1])

        board_map = []
        black_player_stones = []
        white_player_stones = []
        black_player_liberties = []
        white_player_liberties = []

        print("[DEBUG] Board size: {}".format(board_size))
        print("[DEBUG] Next to play: {}".format(player_to_move))

        for i in range(board_size):
            print("[DEBUG] Reading line {}.".format(i + 1))
            board_line = f.readline().strip()
            board_map.append(board_line)

        # Get stones lists ready
        for i in range(board_size):
            for j in range(board_size):
                point = (i, j)
                point_state = board_map[i][j]
                print("[DEBUG] [index: (i, j) = {}] | [point state: {}]".format(point, point_state))
                if point_state == '0':
                    # TODO: Check if liberty of any player and others?
                    print("[DEBUG] Empty point.")
                elif point_state == '1':
                    print("[DEBUG] Black player stone found.")
                    update_player_stones(board_map, '1', point, black_player_stones)
                else:
                    print("[DEBUG] White player stone found.")
                    update_player_stones(board_map, '2', point, white_player_stones)

        # Get liberties of each group
        update_player_liberties(board_map, black_player_stones, black_player_liberties)
        update_player_liberties(board_map, white_player_stones, white_player_liberties)


        self.state = State(
            player_to_move, board_map,
            black_player_stones, black_player_liberties,
            white_player_stones, white_player_liberties
        )

class State:
    """ Atari Go state."""
    def __init__(self, to_move, board_map, black_stones, black_liberties, white_stones, white_liberties):
        self.to_move = to_move # player to move
        self.black_stones = black_stones # black player stones
        self.black_liberties = black_liberties # black player liberties
        self.white_stones = white_stones # white player stones
        self.white_liberties = white_liberties # black player liberties
        self.board_map = board_map # current board map

    def __str__(self):
        ret_str = "State information:\n"
        ret_str += "Player to move: {}\n".format(self.to_move)
        ret_str += "Black player stones: {}\n".format(self.black_stones)
        ret_str += "White player stones: {}\n".format(self.white_stones)
        ret_str += "Black player liberties: {}\n".format(self.black_liberties)
        ret_str += "White player liberties: {}\n".format(self.white_liberties)
        ret_str += "Board:\n"
        for i in range(len(self.board_map)):
            ret_str += self.board_map[i] + '\n'

        return ret_str