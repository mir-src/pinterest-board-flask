from flask import Flask, render_template, request, redirect  
import sqlite3

app = Flask(__name__)

def get_connection():
    conn = sqlite3.connect("database.db")
    return conn

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/boards", methods=["GET", "POST"])
def boards_page(): 
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS boards (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT
    )
    """)
    conn.commit()
    if request.method == "POST":
        board = request.form["board_name"]
        cursor.execute("INSERT INTO boards (name) VALUES (?)", (board,))
        conn.commit()
       
    cursor.execute("SELECT * FROM boards ORDER BY ID DESC")
    boards = cursor.fetchall()

    print(request.method)

    return render_template('boards.html', boards=boards)

@app.route("/delete/<id>",methods=["POST"])
def delete_board(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM boards WHERE ID = ?", (id,))
    conn.commit()
    return redirect("/boards")

@app.route("/edit/<id>", methods=["POST"])
def edit_board(id):
    conn = get_connection()
    cursor = conn.cursor()
    name = request.form["new_name"]
    cursor.execute("UPDATE boards SET name = ? WHERE ID = ?", (name, id))
    conn.commit()
    return redirect("/boards")

if __name__ == "__main__" :
    app.run(debug=True)


