# game_logic.py

gameOver = False

def checkDraw(board):
    for i in range(0, 9):
        if board[i] == '-':
            return False
    return True

def checkWin(currentPlayer, board):
    #checking horizontally
    if (board[0] == board[1] == board[2] == currentPlayer) or \
       (board[3] == board[4] == board[5] == currentPlayer) or \
       (board[6] == board[7] == board[8] == currentPlayer):
        return True
    
    #checking vertically
    elif (board[0] == board[3] == board[6] == currentPlayer) or \
         (board[1] == board[4] == board[7] == currentPlayer) or \
         (board[2] == board[5] == board[8] == currentPlayer):
        return True
        
    #checking right diagonal
    elif board[0] == board[4] == board[8] == currentPlayer:
        return True
    
    #checking left diagonal
    elif board[2] == board[4] == board[6] == currentPlayer:
        return True

def checkGameEnd(currentPlayer, board):
    global gameOver
    gameOver = checkWin(currentPlayer, board)
    if not gameOver:
        gameOver = checkDraw(board)
    return gameOver

def possibleMoves(board):
    moves = []
    for i in range(9):
        if board[i] == '-':
            moves.append(i)
    return moves

def utility(board):
    if checkWin('O', board):
        return 1 
    elif checkWin('X', board):
        return -1
    elif checkDraw(board):
        return 0

def isTerminalState(board):
    for i in range(9):
        if board[i] == '-':
            return False
    return True

def RecursiveMinimax(board, maximizingPlayer):
    if isTerminalState(board) or checkGameEnd('X', board) or checkGameEnd('O', board) or checkDraw(board):
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
    _, move = RecursiveMinimax(board, True)
    return move
