from flask import Flask, render_template, request, jsonify
from game_logic import *

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

# Route to handle the game moves
@app.route('/move', methods=['POST'])
def move():
    # Get the current state of the board
    board = request.json['board']
    # Make the AI move using minimax algorithm
    ai_move = minimax(board)
    # Update the board  
    board[ai_move] = 'O'
    # Check if the game is over
    game_over = checkGameEnd('O', board)
    # Return the updated board and game over status
    return jsonify({'board': board, 'game_over': game_over})


if __name__ == '__main__':
   # Run the app server on localhost:4449
   app.run('localhost', 4449)


