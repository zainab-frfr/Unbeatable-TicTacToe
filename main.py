import checkingConditions
import minimax

board = ['-'] * 9


currentPlayer = 'X'
winningPlayer = '-'
valid = False
draw = True
gameOver = False

# computer is O and player is X

def printBoard(board):
    for i in range(0,9):
        print(board[i]+" ", end='')
        if i == 2 or i == 5 or i == 8:
            print('\n')


printBoard(board)
print("Computer is O, Player is X.\n ")

while not gameOver:

    if currentPlayer=='O' :
        print("Computer's turn: \n")
        val = minimax.minimax(board)
        if val != None :
            board[val] = 'O'
        gameOver = checkingConditions.checkGameEnd(currentPlayer, board)
        if gameOver and not checkingConditions.checkDraw(board):
            print("\n You lose. \n")
            draw = False
        currentPlayer = 'X'
    else :
        print("Your turn: ")
        while not valid:
            choice = int(input("What position would you like to mark? (numbered 1 to 9)"))
            if board[choice-1] == '-':
                board[choice-1] = 'X'
                valid = True
            else:
                print("That position has already been marked, choose another. ")
        valid = False
        gameOver = checkingConditions.checkGameEnd(currentPlayer, board)
        if gameOver and not checkingConditions.checkDraw(board):
            print("\n You win! \n")
            draw = False
        currentPlayer = 'O'
    
    print('\n')
    printBoard(board)
    print('\n')

if draw :
    print("It's a tie")
