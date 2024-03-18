import checkingConditions
import minimax

board = ['-'] * 9


currentPlayer = 'X'
winningPlayer = '-'
valid = False

gameOver = False

# computer is O and player is X

       
def printBoard(board):
    for i in range(0,9):
        print(board[i]+" ", end='')
        if i == 2 or i == 5 or i == 8:
            print('\n')

printBoard(board)

while not gameOver:

    if currentPlayer=='O' :
        print("Computer's turn: \n")
        val = minimax.minimax(board)
        if val != None :
            board[val] = 'O'
        gameOver = checkingConditions.checkGameEnd(currentPlayer, board)
        currentPlayer = 'X'
    else :
        print("Your turn: \n")
        while not valid:
            choice = int(input("What position would you like to mark? (numbered 1 to 9)"))
            if board[choice-1] == '-':
                board[choice-1] = 'X'
                valid = True
            else:
                print("That position has already been marked, choose another. ")
        valid = False
        gameOver = checkingConditions.checkGameEnd(currentPlayer, board)
        currentPlayer = 'O'
    
    print('\n')
    printBoard(board)

    # if not gameOver:
    #     end_game_input = input("Do you want to end the game? (yes/no): ")
    #     if end_game_input.lower() == 'yes':
    #         gameOver = True
    #     elif end_game_input.lower() == 'no':
    #         gameOver = False

    

