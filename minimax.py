import checkingConditions
from numpy import inf

def possibleMoves(board):
    moves = []
    for i in range(9):
        if board[i] == '-':
            moves.append(i)
    return moves

def utility(board):
    if checkingConditions.checkWin('O',board):
        return 1 
    elif checkingConditions.checkWin('X',board):
        return -1
    elif checkingConditions.checkDraw(board):
        return 0
    

def isTerminalState(board):
    for i in range(9):
        if board[i] == '-':
            return False
    return True


def Max(board):
    if isTerminalState(board):
        return utility(board), None
    
    bestValue = -inf 
    bestMove = None 

    children = possibleMoves(board)

    for move in children:
        new_board = board.copy()
        new_board[move] = 'O'

        value, _ = Min(new_board)
        bestValue = max(bestValue,value)

        if value >= bestValue:
            bestMove = move
    
    return bestValue , bestMove

def Min(board):

    if isTerminalState(board):
        return utility(board), None
    
    bestValue = inf 
    bestMove = None 

    children = possibleMoves(board)

    for move in children:
        new_board = board.copy()
        new_board[move] = 'X'

        value, _ = Max(new_board)
        bestValue = min(bestValue,value)

        if value <= bestValue:
            bestMove = move
    
    return bestValue , bestMove


def minimax(board):
    _, move= Max(board)
    return move


