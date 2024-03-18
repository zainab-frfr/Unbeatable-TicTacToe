def printBoard(board):
    for i in range(0,9):
        print(board[i]+" ", end='')
        if i == 2 or i == 5 or i == 8:
            print('\n')