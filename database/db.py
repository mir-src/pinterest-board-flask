import sqlite3

# Database Connection
def get_connection():
    conn = sqlite3.connect("database.db")
    return conn 

def init_db():
    conn = get_connection()

    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS boards (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT
    )
    """)

    conn.commit()
    conn.close()

# CRUD Operations
def add_board(name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO boards (name) VALUES (?)",
        (name,)
    )
    conn.commit()
    conn.close()

def get_boards():
    conn = get_connection() 
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM boards ORDER BY ID DESC")
    boards = cursor.fetchall()

    conn.close()
    return boards

def delete_board(board_id): 
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM boards WHERE ID = ?",
        (board_id,)
    )
    conn.commit()
    conn.close()

def update_board(board_id, new_name):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE boards SET name = ? WHERE ID = ?",
        (new_name, board_id)
    )
    conn.commit()
    conn.close()

