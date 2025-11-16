from flask import Flask, request, render_template
import sqlite3
import os

app = Flask(__name__)
DB_PATH = 'comments.db'

def init_db():
    if not os.path.exists(DB_PATH):
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('''CREATE TABLE comments
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      author TEXT NOT NULL,
                      message TEXT NOT NULL,
                      created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
        conn.commit()
        conn.close()

def get_comments():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('SELECT id, author, message, created_at FROM comments ORDER BY id DESC')
    comments = c.fetchall()
    conn.close()
    return comments

def add_comment(author, message):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    # Intentionally vulnerable: no sanitization of author or message
    c.execute('INSERT INTO comments (author, message) VALUES (?, ?)', (author, message))
    conn.commit()
    conn.close()

@app.route('/')
def index():
    comments = get_comments()
    return render_template('index.html', comments=comments)

@app.route('/add', methods=['POST'])
def add():
    author = request.form.get('author', '')
    message = request.form.get('message', '')
    
    if author and message:
        add_comment(author, message)
    
    return render_template('index.html', comments=get_comments())

if __name__ == '__main__':
    init_db()
    app.run(host='127.0.0.1', port=5000, debug=True)
