from oskaplayer import oskaplayer
from oskaplayer import convert_format
from movegen import movegen
import random


# This function test the winning rate of the oskaplayer agains a random_player
# Here, we only tested with three board examples with 100 test cases.
#   @param:
#
#   returns:
#           1 if the black wins
#           2 if the white wins
#           -1 f there is a tie
def mass_game():
    board4 = ['wwww','---','--','---','bbbb'];
    board5 = ['wwwww','----','---','--','---','----','bbbbb'];
    board6 = ['wwwwww','-----','----','---','--','---','----','-----','bbbbbb'];

    total_game = 100

    # board4
    white_win_count = 0
    i = 0

    while i < total_game:
        i += 1
        result = game(board4)
        if result == 2:
            white_win_count += 1
        elif result == -1:
            i -= 1

    print("BOARD4 white win rate = {}".format(white_win_count/total_game))

    # board5
    white_win_count = 0
    i = 0

    while i < total_game:
        i += 1
        result = game(board5)
        if result == 2:
            white_win_count += 1
        elif result == -1:
            i -= 1

    print("BOARD5 white win rate = {}".format(white_win_count/total_game))

    # board6
    white_win_count = 0
    i = 0

    while i < total_game:
        i += 1
        result = game(board6)
        if result == 2:
            white_win_count += 1
        elif result == -1:
            i -= 1

    print("BOARD6 white win rate = {}".format(white_win_count/total_game))


# This function determines if there is a win for either player
#   @param:
#   board: the gameboard in the form of a list of strings
#   player: either 'b' or 'w', indicating whose turn it is
#
#   returns:
#           1 if the black wins
#           2 if the white wins
#           -1 f there is a tie
def game(board):
    player = 'w'
    cur_board = board
    while True:
        if player == 'w':
            # Here, I have tested with different values, including 1, 2, 3, 4...
            cur_board = oskaplayer(cur_board, player, 2)
            if cur_board is None:
                return -1
            result = check_win(cur_board, player)
            player = 'b'
        else:
            cur_board = random_player(cur_board)
            result = check_win(cur_board, player)
            player = 'w'

        if result == 1:
            return 1
        if result == 2:
            return 2


# This function determines the next random move for the given player
#   @param:
#   board: the gameboard in the form of a list of strings
#
#   returns the next random move in the form of a gameboard
def random_player(board):
    initial_board = []
    for i in range(0, len(board)):
        new_row = []
        for j in range(0, len(board[i])):
            new_row.append(board[i][j])
        initial_board.append(new_row)

    new_boards = movegen(initial_board, 'b')
    if new_boards == []:
        return board
    choice = int(random.random() * len(new_boards))
    return convert_format(new_boards[choice])


# This function determines if there is a win for either player
#   @param:
#   board: the gameboard in the form of a list of strings
#   player: either 'b' or 'w', indicating whose turn it is
#
#   returns:
#           1 if the black wins
#           2 if the white wins
#           0 if there is not winner currently
def check_win(board, player):
    white_count = 0
    black_count = 0
    white_step = 0
    black_step = 0
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if board[i][j] == 'b':
                black_count += 1
                black_step += i
            if board[i][j] == 'w':
                white_step += len(board) - i - 1
                white_count += 1

    if player == 'w':
        if black_count == 0 or white_step == 0:
            return 2
        elif white_count == 0 or black_step == 0:
            return 1
    else:
        if white_count == 0 or black_step == 0:
            return 1
        elif black_count == 0 or white_step == 0:
            return 2
    return 0
