import checkingConditions
from numpy import inf

def printBoard(board):
    for i in range(0,9):
        print(board[i]+" ", end='')
        if i == 2 or i == 5 or i == 8:
            print('\n')

def possibleMoves(board):
    moves = []
    for i in range(9):
        if board[i] == '-':
            moves.append(i)
    return moves

def checkWin(currentPlayer, board):
    #checking horizontally
    if (board[0] == board[1] == board[2] == currentPlayer) or (board[3] == board[4] == board[5] == currentPlayer) or (board[6] == board[7] == board[8] == currentPlayer):
        return True
    
    #checking vertically
    elif (board[0] == board[3] == board[6] == currentPlayer) or (board[1] == board[4] == board[7] == currentPlayer) or (board[2] == board[5] == board[8] == currentPlayer):
        return True
        
    #checking right diagonal
    elif board[0] == board[4] == board[8] == currentPlayer:
        return True
    
    #checking left diagonal
    elif board[2] == board[4] == board[6] == currentPlayer:
        return True

def utility(board):
    if checkWin('O',board):
        return 1 
    elif checkWin('X',board):
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


