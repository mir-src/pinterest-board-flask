from flask import Flask, render_template, request  
import sqlite3

app = Flask(__name__)

boards = []

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/boards", methods=["GET", "POST"])
def boards_page(): 
    if request.method == "POST":
        new_board = request.form["board_name"]
        boards.append(new_board)

    print(request.method)

    return render_template('boards.html', boards=boards)

if __name__ == "__main__" :
    app.run(debug=True)

