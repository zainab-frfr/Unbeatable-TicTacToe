gameOver = False

def checkDraw(board):
    for i in range(0,9):
        if board[i] == '-':
            return False
    return True

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


def checkGameEnd(currentPlayer, board):   
    global gameOver

    gameOver = checkWin(currentPlayer, board)

    if not gameOver:
        gameOver = checkDraw(board)
    
    return gameOver


