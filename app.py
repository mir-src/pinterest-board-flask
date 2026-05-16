from flask import Flask, render_template, request, redirect  
from database.db import get_boards,add_board,delete_board,update_board

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/boards", methods=["GET", "POST"])
def boards_page(): 
    if request.method == "POST":
        add_board(request.form["board_name"])
        return redirect("/boards")

    boards = get_boards()
    return render_template('boards.html', boards=boards)

@app.route("/delete/<id>",methods=["POST"])
def delete_board_route(id):
    delete_board(id)
    return redirect("/boards")

@app.route("/edit/<id>", methods=["POST"])
def edit_board(id):
    update_board(id, request.form["new_name"])
    return redirect("/boards")

if __name__ == "__main__" :
    app.run(debug=True)


