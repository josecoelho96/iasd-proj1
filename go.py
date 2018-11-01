import games

# black = 1
# white = 2

class Game(games.Game):
    """ Atari Go game class."""

    # def __init__(self, f):
    #     self.state = self.load_board(f)

    def to_move(self, s):
        """Returns the player to move next given the state s."""
        return s.to_move

    def terminal_test(self, s):
        """Returns a boolean of whether state s is terminal."""
        # Either no valid actions or some liberty group empty
        for liberty in s.black_liberties:
            if not liberty:
                return True

        for liberty in s.white_liberties:
            if not liberty:
                return True

        # if not returned yet, check actions
        return not self.actions(s)

    def utility(self, s, p):
        """Returns the payoff of state s if it is terminal
            (1 if p wins, -1 if p loses, 0 in case of a draw),
            otherwise, its evaluation with respect to player p."""
        raise NotImplementedError

    def actions(self, s):
        """Returns a list of valid moves at state s."""

        ############################ AUX FUNCTIONS ############################
        def check_point_neighbours_empty(point, board_map, board_size):
            """ Returns True if a neighbour is empty."""
            i = point[0]
            j = point[1]

            if i > 0:
                # Check i-1
                if board_map[i-1][j] == '0':
                    return True
            if i < board_size - 1:
                # Check i+1
                if board_map[i+1][j] == '0':
                    return True
            if j > 0:
                # Check j-1
                if board_map[i][j-1] == '0':
                    return True
            if j < board_size - 1:
                # Check j+1
                if board_map[i][j+1] == '0':
                    return True
            # None of the above, so return False
            return False

        def check_point_neighbours_occupied(point, player, liberties):
            """Returns True if is not the only liberty of a player's group."""

            for liberty in liberties:
                if point in liberty and len(liberty) == 1:
                    # only liberty is this point, do not play there
                    return False

            # None of the liberties matched the condition, so return True
            return True

        def check_if_eye(point, player, board_map, board_size):
            """Return True if position is an eye (circled by enemy)."""

            i = point[0]
            j = point[1]

            other_player = '2' if player == '1' else '1'

            if i > 0:
                # Check i-1
                if board_map[i-1][j] != other_player:
                    return False
            if i < board_size - 1:
                # Check i+1
                if board_map[i+1][j] != other_player:
                    return False
            if j > 0:
                # Check j-1
                if board_map[i][j-1] != other_player:
                    return False
            if j < board_size - 1:
                # Check j+1
                if board_map[i][j+1] != other_player:
                    return False
            # None of the above, so return False
            return True


        ############################ AUX FUNCTIONS ############################

        moves = []
        for i in range(s.board_size):
            for j in range(s.board_size):
                if s.board_map[i][j] == '0':
                    # Empty point. Check if valid move.
                    print("[DEBUG] Empty point.")
                    # Check if the current position has at least an empty neighbour
                    if check_point_neighbours_empty((i, j), s.board_map, s.board_size):
                        print("[DEBUG] Empty neighbour found, valid move.")
                        moves.append((s.to_move, i, j))
                        continue

                    if s.to_move == 1: # Black player
                        # Check if new stone will be circled by enemy stones (eye)
                        if check_if_eye((i, j), '1', s.board_map, s.board_size):
                            print("[DEBUG] Eye. Not a valid move.")
                            continue
                        # Check if is not the only liberty of a player's group.
                        if check_point_neighbours_occupied((i, j), '1', s.black_liberties):
                            print("[DEBUG] All neighbours occupied, but valid position.")
                            moves.append((s.to_move, i, j))
                    else: # White player
                        # Check if new stone will be circled by enemy stones (eye)
                        if check_if_eye((i, j), '2', s.board_map, s.board_size):
                            print("[DEBUG] Eye. Not a valid move.")
                            continue
                        # Check if is not the only liberty of a player's group.
                        if check_point_neighbours_occupied((i, j), '2', s.white_liberties):
                            print("[DEBUG] All neighbours occupied, but valid position.")
                            moves.append((s.to_move, i, j))

        return moves

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
                        second_updated_string = search_stone_in_player_strings((i, j-1), point, stones)
                        # Stone was added to group on i-1, merge two lists into a bigger string
                        # Only if groups are not the same
                        if updated_string != second_updated_string:
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
                            if (i-1, j) not in string_liberties:
                                string_liberties.append((i-1, j))
                    if i < board_size - 1:
                        print("[DEBUG] Look at 'i+1'.")
                        if check_if_empty_point(board_map, (i+1, j)):
                            if (i+1, j) not in string_liberties:
                                string_liberties.append((i+1, j))
                    if j > 0:
                        print("[DEBUG] Look at 'j-1'.")
                        if check_if_empty_point(board_map, (i, j-1)):
                            if (i, j-1) not in string_liberties:
                                string_liberties.append((i, j-1))
                    if j < board_size - 1:
                        print("[DEBUG] Look at 'j+1'.")
                        if check_if_empty_point(board_map, (i, j+1)):
                            if (i, j+1) not in string_liberties:
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
            print("[DEBUG] Processing line {}.".format(i + 1))
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
            player_to_move, board_size, board_map,
            black_player_stones, black_player_liberties,
            white_player_stones, white_player_liberties
        )

class State:
    """ Atari Go state."""
    def __init__(self, to_move, board_size, board_map, black_stones, black_liberties, white_stones, white_liberties):
        self.to_move = to_move # player to move
        self.black_stones = black_stones # black player stones
        self.black_liberties = black_liberties # black player liberties
        self.white_stones = white_stones # white player stones
        self.white_liberties = white_liberties # black player liberties
        self.board_map = board_map # current board map
        self.board_size = board_size # board size

    def __str__(self):
        ret_str = "State information:\n"
        ret_str += "Player to move: {}\n".format(self.to_move)
        ret_str += "Black player stones: {}\n".format(self.black_stones)
        ret_str += "White player stones: {}\n".format(self.white_stones)
        ret_str += "Black player liberties: {}\n".format(self.black_liberties)
        ret_str += "White player liberties: {}\n".format(self.white_liberties)
        ret_str += "Board size: {}\n".format(self.board_size)
        ret_str += "Board:\n"
        for i in range(len(self.board_map)):
            ret_str += self.board_map[i] + '\n'

        return ret_str