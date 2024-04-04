import checkingConditions
from numpy import inf
depth = 0
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


def RecursiveMinimax(board, maximizingPlayer):

    if isTerminalState(board) or checkingConditions.checkGameEnd('X', board) or checkingConditions.checkGameEnd('O', board) or checkingConditions.checkDraw(board):
        return utility(board), None
    
    moves = possibleMoves(board)
    bestMove = None

    if maximizingPlayer:
        bestValue = -float('inf')
        for move in moves:
            board[move] = 'O'
            value, _ = RecursiveMinimax(board, False)
            board[move] = '-'

            if value > bestValue:
                bestValue = value
                bestMove = move

        return bestValue, bestMove
        
        
    else:
        bestValue = float('inf')
        for move in moves:
            board[move] = 'X'
            value, _ = RecursiveMinimax(board, True)
            board[move] = '-'

            if value < bestValue:
                bestValue = value
                bestMove = move
                
        return bestValue, bestMove
    
def minimax(board):
    _, move= RecursiveMinimax(board, True)
    return move


