gameOver = False
win = False
draw = False 
lose = False
winningPlayer = '-'

def checkDraw(board):
    for i in range(0,9):
        if board[i] == '-':
            return False
    return True


def checkGameEnd(currentPlayer, board):   
    #to indicate that global variables being used
    global win,lose,winningPlayer, gameOver

    #checking horizontally
    if (board[0] == board[1] == board[2] == currentPlayer) or (board[3] == board[4] == board[5] == currentPlayer) or (board[6] == board[7] == board[8] == currentPlayer):
        win = True
        winningPlayer = currentPlayer
    
    #checking vertically
    elif (board[0] == board[3] == board[6] == currentPlayer) or (board[1] == board[4] == board[7] == currentPlayer) or (board[2] == board[5] == board[8] == currentPlayer):
        win = True
        winningPlayer = currentPlayer
        
    #checking right diagonal
    elif board[0] == board[4] == board[8] == currentPlayer:
        win = True
        winningPlayer = currentPlayer
    
    
    #checking left diagonal
    elif board[2] == board[4] == board[6] == currentPlayer:
        win = True
        winningPlayer = currentPlayer

    if win:
        gameOver = True
        if currentPlayer == 'O':
            lose = True
            win = False
            winningPlayer = 'O'
    else: 
        gameOver = checkDraw(board)
    
    return gameOver

def returnWinningPlayer():
    return winningPlayer