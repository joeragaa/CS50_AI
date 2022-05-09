"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if board == initial_state():
        return X
    Xcount = 0
    Ocount = 0
    for row in board:
        for column in row:
            if column == X:
                Xcount+=1
            elif column == O:
                Ocount+=1
    if Xcount > Ocount:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                moves.add((i,j))
    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action[0] not in range(3) or action[1] not in range(3):
        raise Exception("invalid move")
    myboard = copy.deepcopy(board)
    myboard[action[0]][action[1]] = player(myboard)
    return myboard


def transpose(board):
    trans = [list(x) for x in list(zip(*board))]
    return trans


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # check for horizontal match or vertical (using the transpose)
    board_T = transpose(board)
    diagonal = []
    diagonal2 = []
    for i in range(3):
        diagonal.append(board[i][i])
        diagonal2.append(board[i][2-i])
    answers = [x for x in board]
    for x in board_T:
        answers.append(x)
    answers.append(diagonal)
    answers.append(diagonal2)
    if [X, X, X] in answers:
        return X
    elif [O, O, O] in answers:
        return O
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # somebody has won
    if winner(board) != None:
        return True
    # nobody has won but there are still cells to play
    for row in board:
        for column in row:
            if column == EMPTY:
                return False
    # no more moves
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    Winner = winner(board)
    if Winner == X:
        return 1
    elif Winner == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    moves = list(actions(board))
    # if ai has first move play randomly
    if board == initial_state():
        return moves[0]
    values = []
    if player(board) == X:
        for move in moves:
            values.append(min_value(result(board,move)))
        v = max(values)
    if player(board) == O:
        for move in moves:
            values.append(max_value(result(board,move)))
            v = min(values)
    return moves[values.index(v)]


def max_value(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board,action)))
    return v


def min_value(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board,action)))
    return v

