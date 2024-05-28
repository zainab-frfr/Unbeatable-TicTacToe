from flask import Flask, render_template, request, jsonify,  redirect, url_for
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
    if ai_move is None:
       return render_template("draw.html")
    else:    
        # Update the board  
        board[ai_move] = 'O'
        
        # Check if the game is over
        game_over = checkGameEnd('O', board)
        # Return the updated board and game over status
        return jsonify({'board': board, 'game_over': game_over})
    

@app.route('/ai_winner', methods =["GET"])
def ai_winner():
    return render_template("ai_winner.html")    

@app.route('/user_winner')
def user_winner():
    return render_template("user_winner.html")

# @app.route('/index', methods = ["GET"])
# def index():
#     return render_template("index.html")

@app.route('/draw', methods = ["GET"])
def draw():
    return render_template("draw.html")

if __name__ == '__main__':
   # Run the app server on localhost:4449
   app.run('localhost', 4449)


