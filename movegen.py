import copy


# This function generates all the possible moves that the input player can make
#   @param:
#   initial_board: the gameboard
#   player: either 'b' or 'w', indicating whose turn it is
#
#   returns a list of newly generated gameboards
def movegen(initial_board, player):
    new_boards = []

    # Nested for loop to find all the pieces of the player
    for i in range(0, len(initial_board)):
        for j in range(0, len(initial_board[i])):
            if initial_board[i][j] == player:
                result = move(initial_board, i, j)
                for board in result:
                    new_boards.append(board)
    return new_boards


# This function determines whether the player is white or black and returns the
# corresponding new boards
#   @param:
#   board: the gameboard
#   row: the row index of the piece that will be moved
#   col: the column index of the piece that will be moved
#
#   returns a list of newly generated gameboards
def move(board, row, col):
    if board[row][col] == 'w':
        return white_move(board, row, col)
    else:
        return black_move(board, row, col)


# This function generates all the new boards when the player holds white
#   @param:
#   board: the gameboard
#   row: the row index of the piece that will be moved
#   col: the column index of the piece that will be moved
#
#   returns a list of newly generated gameboards
def white_move(board, row, col):
    size = len(board)
    forwards = []

    # If the piece is on the first of that row
    if col == 0:
        # Move forward
        if (row < size-1 and board[row+1][0] == '-'):
            forwards.append(forward(board, row, col, row+1, 0))
        # If the piece is in the lower half of the board
        if (row >= (size-1) / 2 and row < size-1
            and board[row+1][col+1] == '-'):
            forwards.append(forward(board, row, col, row+1, col+1))

        # Jump forward
        # If the piece is in the upper half of the board
        if (row < (size - 2) and row != (size-1) / 2 - 1 and
            board[row+1][0] == 'b' and
            board[row+2][0] == '-'):
            forwards.append(jump(board, row, col, row+1, 0, row+2, 0))
        # If the piece is on the line right above the middle line
        if (row == (size-1) / 2 - 1 and
            board[row+1][0] == 'b' and
            board[row+2][1] == '-'):
            forwards.append(jump(board, row, col, row+1, 0, row+2, 1))
        # If the piece is in the lower half of the board
        if (row >= (size-1) / 2 and row < size-2
            and board[row+1][col+1] == 'b' and board[row+2][col+2] == '-'):
            forwards.append(jump(board, row, col, row+1, col+1, row+2, col+2))

    # if the piece is on the last of that row
    elif col == len(board[row])-1:
        # Move forward
        # If the piece is in the upper half of the board
        if (row < (size-1) / 2 and board[row+1][col-1] == '-'):
            forwards.append(forward(board, row, col, row+1, col-1))
        # If the piece is in the lower half of the board
        if (row >= (size-1) / 2 and row < size-1):
            if board[row+1][col] == '-':
                forwards.append(forward(board, row, col, row+1, col))
            if board[row+1][col+1] == '-':
                forwards.append(forward(board, row, col, row+1, col+1))

        # Jump forward
        # If the piece is in the upper half of the board
        if (row < (size-1) / 2 - 1 and
            board[row+1][col-1] == 'b' and
            board[row+2][col-2] == '-'):
            forwards.append(jump(board, row, col, row+1, col-1, row+2, col-2))
        # If the piece is on the line right above the middle line
        if (row == (size-1) / 2 - 1 and
            board[row+1][col-1] == 'b' and
            board[row+2][col-1] == '-'):
            forwards.append(jump(board, row, col, row+1, col-1, row+2, col-1))
        # If the piece is in the lower half of the board
        if (row >= (size-1) / 2 and row < size-2):
            if (board[row+1][col+1] == 'b' and board[row+2][col+2] == '-'):
                forwards.append(jump(board, row, col, row+1, col+1, row+2, col+2))
            if (board[row+1][col] == 'b' and board[row+2][col] == '-'):
                forwards.append(jump(board, row, col, row+1, col, row+2, col))

    # If the piece is in the middle of that row, it can move forward in
    # two directions
    else:
        # If the piece is in the upper half of the board
        if row < (size-1) / 2:
            # Move forward to the left
            if board[row+1][col-1] == '-':
                forwards.append(forward(board, row, col, row+1, col-1))
            # Jump to the left
            if (col > 1 and board[row+1][col-1] == 'b' and board[row+2][col-2] == '-'):
                forwards.append(jump(board, row, col, row+1, col-1, row+2, col-2))
            # If the piece is on the line right above the middle line
            if (col == 1 and row == ((size-1) / 2 - 1)
                and board[row+1][col-1] == 'b'
                and board[row+2][col-1] == '-'):
                forwards.append(jump(board, row, col, row+1, col-1, row+2, col-1))

            # Move forward to the right
            if board[row+1][col] == '-':
                forwards.append(forward(board, row, col, row+1, col))
            # Jump to the right
            if (len(board[row+2]) > col and row != ((size-1) / 2 - 1) and
                board[row+1][col] == 'b' and board[row+2][col] == '-'):
                forwards.append(jump(board, row, col, row+1, col, row+2, col))
            # If the piece is on the line right above the middle line
            if (len(board[row+2]) > (col+1) and row == ((size-1) / 2 - 1)
                and board[row+1][col] == 'b'
                and board[row+2][col+1] == '-'):
                forwards.append(jump(board, row, col, row+1, col, row+2, col+1))

        # If the piece is in the lower half of the board
        else:
            # Move forward to the left
            if (row < size-1 and board[row+1][col] == '-'):
                forwards.append(forward(board, row, col, row+1, col))
            # Jump to the left
            if (row < size-2 and board[row+1][col] == 'b' and board[row+2][col] == '-'):
                forwards.append(jump(board, row, col, row+1, col, row+2, col))

            # Move forward to the right
            if (row < size-1 and board[row+1][col+1] == '-'):
                forwards.append(forward(board, row, col, row+1, col+1))
            # Jump to the right
            if (row < size-2 and
                board[row+1][col+1] == 'b' and board[row+2][col+2] == '-'):
                forwards.append(jump(board, row, col, row+1, col+1, row+2, col+2))
    return forwards


# This function generates all the new boards when the player holds white
#   @param:
#   board: the gameboard
#   row: the row index of the piece that will be moved
#   col: the column index of the piece that will be moved
#
#   returns a list of newly generated gameboards
def black_move(board, row, col):
    size = len(board)
    forwards = []

    # if the piece is on the first of that row
    if col == 0:
        # Move forward
        # If the piece is in the upper half of the board
        if (row <= (size-1) / 2 and board[row-1][col+1] == '-'):
                forwards.append(forward(board, row, col, row-1, col+1))

        if (row > 0 and board[row-1][0] == '-'):
            forwards.append(forward(board, row, col, row-1, 0))

        # Jump forward
        # If the piece is in the upper half of the board, it can jump right
        if (row <= (size-1) / 2 and row > 1
            and board[row-1][col+1] == 'w' and board[row-2][col+2] == '-'):
            forwards.append(jump(board, row, col, row-1, col+1, row-2, col+2))
        # If the piece is not on the line below the middle and jumps left
        if (row != (size-1) / 2 + 1 and row > 1 and
            board[row-1][0] == 'w' and
            board[row-2][0] == '-'):
            forwards.append(jump(board, row, col, row-1, 0, row-2, 0))
        # If the piece is on the line right below the middle line
        if (row == ((size-1) / 2 + 1) and
            board[row-1][0] == 'w' and
            board[row-2][1] == '-'):
            forwards.append(jump(board, row, col, row-1, 0, row-2, 1))

    # if the piece is on the last of that row
    elif col == len(board[row])-1:
        # Move forward
        # If the piece is in the upper half of the board
        if row <= (size-1) / 2 and row >= 1:
            if board[row-1][col+1] == '-':
                forwards.append(forward(board, row, col, row-1, col+1))
            if board[row-1][col] == '-':
                forwards.append(forward(board, row, col, row-1, col))
        # If the piece is in the lower half of the board
        if (row > (size-1) / 2 and board[row-1][col-1] == '-'):
            forwards.append(forward(board, row, col, row-1, col-1))

        # Jump forward
        # If the piece is in the upper half of the board, it can jump left
        if (row <= (size-1) / 2 and row > 1):
            if (board[row-1][col+1] == 'w' and board[row-2][col+2] == '-'):
                forwards.append(jump(board, row, col, row-1, col+1, row-2, col+2))
            if (board[row-1][col] == 'w' and board[row-2][col] == '-'):
                forwards.append(jump(board, row, col, row-1, col, row-2, col))
        # If the piece is in the lower half of the board
        if (row > ((size-1) / 2 + 1)
            and board[row-1][col-1] == 'w'
            and board[row-2][col-2] == '-'):
            forwards.append(jump(board, row, col, row-1, col-1, row-2, col-2))
        # If the piece is on the line right below the middle line
        if (row == ((size-1) / 2 + 1)
            and board[row-1][col-1] == 'w'
            and board[row-2][col-1] == '-'):
            forwards.append(jump(board, row, col, row-1, col-1, row-2, col-1))

    # If the piece is in the middle of that row, it can move forward in
    # two directions
    else:
        # If the piece is in the upper half of the board
        if row < (size-1) / 2:
            # Move forward to the left
            if row > 0 and board[row-1][col] == '-':
                forwards.append(forward(board, row, col, row-1, col))
            # Jump to the left
            if (row > 1 and board[row-1][col] == 'w' and board[row-2][col] == '-'):
                forwards.append(jump(board, row, col, row-1, col, row-2, col))

            # Move forward to the right
            if row > 0 and board[row-1][col+1] == '-':
                 forwards.append(forward(board, row, col, row-1, col+1))
            # Jump to the right
            if (row > 1 and
                board[row-1][col+1] == 'w' and board[row-2][col+2] == '-'):
                forwards.append(jump(board, row, col, row-1, col+1, row-2, col+2))

        # If the piece is in the lower half of the board
        else:
            # Move forward to the left
            if board[row-1][col-1] == '-':
                forwards.append(forward(board, row, col, row-1, col-1))
            # Jump to the left
            if (col > 1 and board[row-1][col-1] == 'w' and board[row-2][col-2] == '-'):
                forwards.append(jump(board, row, col, row-1, col-1, row-2, col-2))
            # If the piece is on the line right below the middle line
            if (col == 1 and row == ((size-1) / 2 + 1)
                and board[row-1][col-1] == 'w'
                and board[row-2][col-1] == '-'):
                forwards.append(jump(board, row, col, row-1, col-1, row-2, col-1))

            # Move forward to the right
            if board[row-1][col] == '-':
                forwards.append(forward(board, row, col, row-1, col))
            # Jump to the right
            if (len(board[row-2]) > col and row != ((size-1) / 2 + 1) and
                board[row-1][col] == 'w' and board[row-2][col] == '-'):
                forwards.append(jump(board, row, col, row-1, col, row-2, col))
            # If the piece is on the line right below the middle line
            if (row == ((size-1) / 2 + 1) and len(board[row-2]) > (col+1)
                and board[row-1][col] == 'w'
                and board[row-2][col+1] == '-'):
                forwards.append(jump(board, row, col, row-1, col, row-2, col+1))
    return forwards


# This function moves the piece from the old position to the new position
#   @param:
#   board: the gameboard
#   old_row: the row index of the piece that will be moved
#   old_col: the column index of the piece that will be moved
#   new_row: the row index of the place that the piece will be moved to
#   new_col: the column index of the place that the piece will be moved to
#
#   returns the new gameboard
def forward(board, old_row, old_col, new_row, new_col):
    result = copy.deepcopy(board)
    result[old_row][old_col] = '-'
    result[new_row][new_col] = board[old_row][old_col]
    return result


# This function moves the piece from the old position to the new position,
# jumping over the opponent's piece in the middle
#   @param:
#   board: the gameboard
#   old_row: the row index of the piece that will be moved
#   old_col: the column index of the piece that will be moved
#   middle_row: the row index of the piece that will be removed by this jump
#   middle_col: the column index of the piece that will be removed by this jump
#   new_row: the row index of the place that the piece will be moved to
#   new_col: the column index of the place that the piece will be moved to
#
#   returns the new gameboard
def jump(board, old_row, old_col, middle_row, middle_col, new_row, new_col):
    result = copy.deepcopy(board)
    result[old_row][old_col] = '-'
    result[middle_row][middle_col] = '-'
    result[new_row][new_col] = board[old_row][old_col]
    return result
