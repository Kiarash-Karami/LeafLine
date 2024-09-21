import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect('forest.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS trees
                 (id INTEGER PRIMARY KEY, date TEXT, duration INTEGER)''')
    conn.commit()
    conn.close()

def add_tree(duration):
    conn = sqlite3.connect('forest.db')
    c = conn.cursor()
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO trees (date, duration) VALUES (?, ?)", (date, duration))
    conn.commit()
    conn.close()

def get_tree_count():
    conn = sqlite3.connect('forest.db')
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM trees")
    count = c.fetchone()[0]
    conn.close()
    return count

def get_total_focus_time():
    conn = sqlite3.connect('forest.db')
    c = conn.cursor()
    c.execute("SELECT SUM(duration) FROM trees")
    total_time = c.fetchone()[0]
    conn.close()
    return total_time if total_time else 0
